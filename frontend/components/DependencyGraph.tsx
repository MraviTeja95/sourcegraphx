"use client";

import { useEffect, useRef, useState, type PointerEvent } from "react";
import type { VersionDependencies } from "@/types/api";

const VIEWBOX_WIDTH = 620;
const VIEWBOX_HEIGHT = 390;
const MIN_ZOOM = 0.6;
const MAX_ZOOM = 2.5;
const DRAG_THRESHOLD = 5;

type GraphNode = { id: string; label: string; displayLabel: string; kind: "version" | "package"; x: number; y: number; width: number; height: number };
type Transform = { scale: number; x: number; y: number };
type PointerState = { startX: number; startY: number; originX: number; originY: number; dragging: boolean };

function pointerToViewbox(viewport: HTMLDivElement | null, event: { clientX: number; clientY: number }) {
  const rect = viewport?.getBoundingClientRect();
  if (!rect) return { x: VIEWBOX_WIDTH / 2, y: VIEWBOX_HEIGHT / 2 };
  return { x: ((event.clientX - rect.left) / rect.width) * VIEWBOX_WIDTH, y: ((event.clientY - rect.top) / rect.height) * VIEWBOX_HEIGHT };
}

function getInitialTransform(nodes: GraphNode[]): Transform {
  const bounds = nodes.reduce((current, node) => ({
    left: Math.min(current.left, node.x - node.width / 2),
    right: Math.max(current.right, node.x + node.width / 2),
    top: Math.min(current.top, node.y - node.height / 2),
    bottom: Math.max(current.bottom, node.y + node.height / 2),
  }), { left: Infinity, right: -Infinity, top: Infinity, bottom: -Infinity });
  if (!Number.isFinite(bounds.left)) return { scale: 1, x: 0, y: 0 };
  const padding = 42;
  const scale = Math.min(1, (VIEWBOX_WIDTH - padding * 2) / (bounds.right - bounds.left), (VIEWBOX_HEIGHT - padding * 2) / (bounds.bottom - bounds.top));
  return { scale, x: (VIEWBOX_WIDTH - (bounds.left + bounds.right) * scale) / 2, y: (VIEWBOX_HEIGHT - (bounds.top + bounds.bottom) * scale) / 2 };
}

export function DependencyGraph({ versions }: { versions: VersionDependencies[] }) {
  const viewportRef = useRef<HTMLDivElement>(null);
  const pointerRef = useRef<PointerState | null>(null);
  const suppressClickRef = useRef(false);
  const getNodeWidth = (label: string, kind: GraphNode["kind"]) => Math.min(kind === "version" ? 136 : 158, Math.max(kind === "version" ? 112 : 84, label.length * 8 + 24));
  const displayLabel = (label: string, width: number) => label.length * 7.2 <= width - 18 ? label : `${label.slice(0, Math.max(3, Math.floor((width - 32) / 7.2)))}...`;
  const packages = Array.from(new Map(versions.flatMap((version) => version.packages).map((pkg) => [pkg.id, pkg])).values());
  const visibleVersions = versions.slice(0, 5);
  const nodes: GraphNode[] = [
    ...visibleVersions.map((version, index) => { const label = `v${version.version}`; const width = getNodeWidth(label, "version"); return { id: version.id, label, displayLabel: displayLabel(label, width), kind: "version" as const, x: 125, y: 50 + index * 72, width, height: 34 }; }),
    ...packages.map((pkg, index) => { const label = pkg.name; const width = getNodeWidth(label, "package"); return { id: pkg.id, label, displayLabel: displayLabel(label, width), kind: "package" as const, x: 405 + (index % 2) * 130, y: 42 + Math.floor(index / 2) * 61, width, height: 34 }; }),
  ];
  const nodeById = new Map(nodes.map((node) => [node.id, node]));
  const edges = visibleVersions.flatMap((version) => version.packages.map((pkg) => ({ from: version.id, to: pkg.id }))).filter((edge) => nodeById.has(edge.to));
  const [selected, setSelected] = useState<string | null>(null);
  const [view, setView] = useState<Transform>(() => getInitialTransform(nodes));
  const [dragging, setDragging] = useState(false);

  useEffect(() => {
    const viewport = viewportRef.current;
    if (!viewport) return;
    const handleWheel = (event: globalThis.WheelEvent) => {
      if (!event.ctrlKey) return;
      event.preventDefault();
      const cursor = pointerToViewbox(viewport, event);
      setView((current) => {
        const nextScale = Math.min(MAX_ZOOM, Math.max(MIN_ZOOM, current.scale * Math.exp(-event.deltaY * 0.001)));
        const worldX = (cursor.x - current.x) / current.scale;
        const worldY = (cursor.y - current.y) / current.scale;
        return { scale: nextScale, x: cursor.x - worldX * nextScale, y: cursor.y - worldY * nextScale };
      });
    };
    viewport.addEventListener("wheel", handleWheel, { passive: false });
    return () => viewport.removeEventListener("wheel", handleWheel);
  }, []);
  const handlePointerDown = (event: PointerEvent<SVGSVGElement>) => {
    pointerRef.current = { startX: event.clientX, startY: event.clientY, originX: view.x, originY: view.y, dragging: false };
    try {
      event.currentTarget.setPointerCapture(event.pointerId);
    } catch {
      return;
    }
  };
  const handlePointerMove = (event: PointerEvent<SVGSVGElement>) => {
    const pointer = pointerRef.current;
    if (!pointer) return;
    const dx = event.clientX - pointer.startX;
    const dy = event.clientY - pointer.startY;
    if (!pointer.dragging && Math.hypot(dx, dy) < DRAG_THRESHOLD) return;
    pointer.dragging = true;
    suppressClickRef.current = true;
    setDragging(true);
    const rect = viewportRef.current?.getBoundingClientRect();
    const factor = rect ? VIEWBOX_WIDTH / rect.width : 1;
    setView((current) => ({ ...current, x: pointer.originX + dx * factor, y: pointer.originY + dy * factor }));
  };
  const handlePointerUp = (event: PointerEvent<SVGSVGElement>) => {
    if (event.currentTarget.hasPointerCapture(event.pointerId)) event.currentTarget.releasePointerCapture(event.pointerId);
    pointerRef.current = null;
    setDragging(false);
    window.setTimeout(() => { suppressClickRef.current = false; }, 0);
  };
  const selectNode = (id: string) => {
    if (!suppressClickRef.current) setSelected(selected === id ? null : id);
  };

  return (
    <div className={`graph-shell ${dragging ? "is-dragging" : ""}`}>
      <div className="graph-legend"><span><i className="legend-version" /> Versions</span><span><i className="legend-package" /> Packages</span><span className="graph-hint">Drag to pan · Ctrl + scroll to zoom · click to inspect</span></div>
      <div className="graph-viewport" ref={viewportRef}>
        <svg className="dependency-graph" viewBox={`0 0 ${VIEWBOX_WIDTH} ${VIEWBOX_HEIGHT}`} role="img" aria-label="Dependency graph showing project versions and packages" onPointerDown={handlePointerDown} onPointerMove={handlePointerMove} onPointerUp={handlePointerUp} onPointerCancel={handlePointerUp}>
          <defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M 24 0 L 0 0 0 24" fill="none" stroke="#dfe9e7" strokeWidth="1" /></pattern><linearGradient id="graphBg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stopColor="#f5faf7" /><stop offset="100%" stopColor="#eef5f0" /></linearGradient></defs>
          <rect width={VIEWBOX_WIDTH} height={VIEWBOX_HEIGHT} fill="url(#graphBg)" /><rect width={VIEWBOX_WIDTH} height={VIEWBOX_HEIGHT} fill="url(#grid)" />
          <g transform={`translate(${view.x} ${view.y}) scale(${view.scale})`}>
            {edges.map((edge) => { const from = nodeById.get(edge.from)!; const to = nodeById.get(edge.to)!; return <line key={`${edge.from}-${edge.to}`} className={selected && selected !== edge.from && selected !== edge.to ? "edge muted" : "edge"} x1={from.x + from.width / 2} y1={from.y} x2={to.x - to.width / 2} y2={to.y} />; })}
            {nodes.map((node) => <g key={node.id} className={`graph-node ${node.kind} ${selected === node.id ? "selected" : ""}`} onClick={() => selectNode(node.id)} tabIndex={0} role="button" aria-label={node.label} onKeyDown={(event) => { if (event.key === "Enter" || event.key === " ") selectNode(node.id); }}><rect x={node.x - node.width / 2} y={node.y - node.height / 2} width={node.width} height={node.height} rx="4" /><text x={node.x} y={node.y + 5} textAnchor="middle">{node.displayLabel}</text></g>)}
          </g>
        </svg>
      </div>
    </div>
  );
}
