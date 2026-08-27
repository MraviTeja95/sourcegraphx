"use client";

import { useState, type PointerEvent, type WheelEvent } from "react";
import type { VersionDependencies } from "@/types/api";

type GraphNode = { id: string; label: string; kind: "version" | "package"; x: number; y: number };

export function DependencyGraph({ versions }: { versions: VersionDependencies[] }) {
  const packages = Array.from(new Map(versions.flatMap((version) => version.packages).map((pkg) => [pkg.id, pkg])).values());
  const visibleVersions = versions.slice(0, 5);
  const nodes: GraphNode[] = [
    ...visibleVersions.map((version, index) => ({ id: version.id, label: `v${version.version}`, kind: "version" as const, x: 125, y: 50 + index * 72 })),
    ...packages.map((pkg, index) => ({ id: pkg.id, label: pkg.name, kind: "package" as const, x: 405 + (index % 2) * 130, y: 42 + Math.floor(index / 2) * 61 })),
  ];
  const [selected, setSelected] = useState<string | null>(null);
  const [view, setView] = useState({ scale: 1, x: 0, y: 0 });
  const [dragStart, setDragStart] = useState<{ x: number; y: number } | null>(null);
  const nodeById = new Map(nodes.map((node) => [node.id, node]));
  const edges = visibleVersions.flatMap((version) => version.packages.map((pkg) => ({ from: version.id, to: pkg.id }))).filter((edge) => nodeById.has(edge.to));
  const handleWheel = (event: WheelEvent<SVGSVGElement>) => {
    event.preventDefault();
    setView((current) => ({ ...current, scale: Math.min(2, Math.max(.75, current.scale - event.deltaY * .001)) }));
  };
  const handlePointerDown = (event: PointerEvent<SVGSVGElement>) => setDragStart({ x: event.clientX, y: event.clientY });
  const handlePointerMove = (event: PointerEvent<SVGSVGElement>) => {
    if (!dragStart) return;
    setView((current) => ({ ...current, x: current.x + (event.clientX - dragStart.x) * .8, y: current.y + (event.clientY - dragStart.y) * .8 }));
    setDragStart({ x: event.clientX, y: event.clientY });
  };

  return (
    <div className="graph-shell">
      <div className="graph-legend"><span><i className="legend-version" /> Versions</span><span><i className="legend-package" /> Packages</span><span className="graph-hint">Click a node to inspect</span></div>
      <svg className="dependency-graph" viewBox="0 0 620 390" role="img" aria-label="Dependency graph showing project versions and packages" onWheel={handleWheel} onPointerDown={handlePointerDown} onPointerMove={handlePointerMove} onPointerUp={() => setDragStart(null)} onPointerLeave={() => setDragStart(null)}>
        <defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M 24 0 L 0 0 0 24" fill="none" stroke="#dfe9e7" strokeWidth="1" /></pattern></defs>
        <rect width="620" height="390" fill="url(#grid)" />
        <g transform={`translate(${view.x} ${view.y}) scale(${view.scale})`}>
          {edges.map((edge) => { const from = nodeById.get(edge.from)!; const to = nodeById.get(edge.to)!; return <line key={`${edge.from}-${edge.to}`} className={selected && selected !== edge.from && selected !== edge.to ? "edge muted" : "edge"} x1={from.x + 58} y1={from.y} x2={to.x - 10} y2={to.y} />; })}
          {nodes.map((node) => <g key={node.id} className={`graph-node ${node.kind} ${selected === node.id ? "selected" : ""}`} onClick={() => setSelected(selected === node.id ? null : node.id)} tabIndex={0} role="button" aria-label={node.label} onKeyDown={(event) => { if (event.key === "Enter" || event.key === " ") setSelected(selected === node.id ? null : node.id); }}><rect x={node.x - (node.kind === "version" ? 58 : 10)} y={node.y - 17} width={node.kind === "version" ? 116 : 122} height="34" rx="4" /><text x={node.x} y={node.y + 5} textAnchor="middle">{node.label.length > 17 ? `${node.label.slice(0, 16)}…` : node.label}</text></g>)}
        </g>
      </svg>
    </div>
  );
}