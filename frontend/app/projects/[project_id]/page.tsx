"use client";

import Link from "next/link";
import { useEffect, useState, type ReactNode } from "react";
import { Header } from "@/components/Header";
import { DependencyGraph } from "@/components/DependencyGraph";
import { getDependencies, getImpact, getProject } from "@/lib/api";
import type { DependenciesResponse, ProjectDetail, ImpactResponse as ProjectImpact } from "@/types/api";

function latestVersion(versions: ProjectDetail["versions"]) {
  return [...versions].sort((a, b) => b.release_date.localeCompare(a.release_date))[0];
}

function MetadataItem({ label, value, children }: { label: string; value?: string; children?: ReactNode }) {
  return <div className="metadata-item"><p className="section-kicker">{label}</p>{value && <strong className="metadata-value">{value}</strong>}{children}</div>;
}

function DetailLoading() {
  return <div className="app-shell"><Header /><main className="container"><div className="detail-loading"><span className="spinner" /><strong>Loading project intelligence...</strong><span>Following project relationships from the graph.</span></div></main></div>;
}

function DetailError() {
  return <div className="app-shell"><Header /><main className="container"><div className="state-box detail-error"><span className="error-code">404 / PROJECT</span><strong>Project not found</strong><span>The requested project does not exist in the SourceGraphX graph.</span><Link href="/">Back to Explore <span aria-hidden="true">→</span></Link></div></main></div>;
}

function DependencyPanel({ dependencies }: { dependencies: DependenciesResponse | null }) {
  if (!dependencies) return <div className="state-box inline-state"><strong>Dependency data unavailable</strong><span>We could not load this project&apos;s dependency relationships.</span></div>;
  return <div className="analysis-content"><div className="analysis-title"><div><p className="section-kicker">GRAPH VIEW / DEPENDS ON</p><h2>Dependency map</h2></div><span className="graph-count">{dependencies.packages.length} packages · {dependencies.versions.length} versions</span></div><p className="graph-context">Explore how this project&apos;s versions connect to package dependencies and identify packages shared across projects.</p><DependencyGraph versions={dependencies.versions} /><div className="version-list"><div className="version-list-heading"><p className="section-kicker">VERSION HISTORY</p><span>Release timeline</span></div>{dependencies.versions.map((version) => <div className="version-row" key={version.id}><span className="version-number">{version.version}</span><span>{version.release_date || "Release date unavailable"}</span><span>{version.packages.length} dependencies</span></div>)}</div></div>;
}

function ImpactPanel({ impact, project }: { impact: ProjectImpact | null; project: ProjectDetail }) {
  if (!impact) return <div className="state-box inline-state"><strong>Impact data unavailable</strong><span>We could not calculate the shared dependency relationships.</span></div>;
  return <div className="analysis-content impact-content"><div className="impact-summary"><span className="impact-symbol">↗</span><div><p className="section-kicker">BLAST RADIUS</p><h2>{impact.affected_projects.length} {impact.affected_projects.length === 1 ? "project shares" : "projects share"} dependencies with {project.name}</h2><p>Shared packages connect this project to potential downstream impact.</p></div></div><div className="impact-flow"><div className="flow-column"><span className="flow-label">SOURCE PROJECT</span><div className="flow-node source-node">{project.name}</div></div><span className="flow-arrow">→</span><div className="flow-column"><span className="flow-label">SHARED PACKAGES</span>{impact.shared_dependencies.map((pkg) => <div className="flow-node package-node" key={pkg.id}>{pkg.name}<small>{pkg.ecosystem}</small></div>)}</div><span className="flow-arrow">→</span><div className="flow-column"><span className="flow-label">AFFECTED PROJECTS</span>{impact.affected_projects.map((affected) => <Link href={`/projects/${affected.id}`} className="flow-node affected-node" key={affected.id}>{affected.name}<small>{affected.language}</small></Link>)}</div></div><div className="impact-edges"><div className="version-list-heading"><p className="section-kicker">IMPACT RELATIONSHIPS</p><span>{impact.impact_edges.length} shared links</span></div>{impact.impact_edges.map((edge) => <div className="impact-edge" key={`${edge.project_id}-${edge.package_id}`}><span className="edge-project">{edge.project_id.replace("project-", "")}</span><span className="edge-arrow">→</span><span className="edge-package">{edge.package_name}</span></div>)}</div></div>;
}

export default function ProjectPage({ params }: { params: Promise<{ project_id: string }> }) {
  const [project, setProject] = useState<ProjectDetail | null>(null);
  const [dependencies, setDependencies] = useState<DependenciesResponse | null>(null);
  const [impact, setImpact] = useState<ProjectImpact | null>(null);
  const [tab, setTab] = useState<"dependencies" | "impact">("dependencies");
  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let active = true;
    params.then(({ project_id }) => Promise.all([getProject(project_id), getDependencies(project_id), getImpact(project_id)]).then(([nextProject, nextDependencies, nextImpact]) => {
      if (!active) return;
      setProject(nextProject);
      setDependencies(nextDependencies);
      setImpact(nextImpact);
    }).catch(() => { if (active) setError(true); }).finally(() => { if (active) setLoading(false); }));
    return () => { active = false; };
  }, [params]);

  if (loading) return <DetailLoading />;
  if (error || !project) return <DetailError />;
  const release = latestVersion(project.versions);
  return <div className="app-shell"><Header /><main className="container detail-page"><Link className="back-link" href="/">← Back to Explore</Link><section className="project-hero"><div className="project-heading"><div className="project-badge">{project.name.slice(0, 2).toUpperCase()}</div><div><p className="section-kicker">PROJECT / {project.language.toUpperCase()}</p><h1>{project.name}</h1><p>{project.description}</p></div></div><div className="hero-actions"><span className="hero-stat"><strong>★ {project.stars.toLocaleString()}</strong><small>stars</small></span>{project.repository && <a className="repo-button" href={project.repository.url} target="_blank" rel="noreferrer">View repository ↗</a>}</div></section><section className="metadata-grid" aria-label="Project metadata"><MetadataItem label="Maintainer" value={project.maintainer?.name}><span>{project.maintainer?.organization}</span></MetadataItem><MetadataItem label="Repository" value={project.repository?.platform}><a className="metadata-link" href={project.repository?.url} target="_blank" rel="noreferrer">{project.repository?.url}</a></MetadataItem><MetadataItem label="License" value={project.license}><span>{project.language}</span></MetadataItem><MetadataItem label="Latest release" value={release?.version}><span>{release?.release_date || "Release date unavailable"}</span></MetadataItem><MetadataItem label="Tags"><div className="tag-list">{project.tags.map((tag) => <span key={tag.id}>#{tag.name}</span>)}</div></MetadataItem></section><div className="detail-layout"><aside className="detail-sidebar"><div className="sidebar-heading"><p className="section-kicker">PROJECT SNAPSHOT</p><span>{project.versions.length} releases</span></div><div className="stat-row"><span>Language</span><strong>{project.language}</strong></div><div className="stat-row"><span>Stars</span><strong>★ {project.stars.toLocaleString()}</strong></div><div className="stat-row"><span>License</span><strong>{project.license}</strong></div></aside><section className="analysis-panel"><div className="tab-bar" role="tablist"><button role="tab" aria-selected={tab === "dependencies"} className={tab === "dependencies" ? "active" : ""} onClick={() => setTab("dependencies")}>Dependency map <span>{dependencies?.packages.length ?? "–"}</span></button><button role="tab" aria-selected={tab === "impact"} className={tab === "impact" ? "active" : ""} onClick={() => setTab("impact")}>Impact analysis <span>{impact?.affected_projects.length ?? "–"}</span></button></div>{tab === "dependencies" ? <DependencyPanel dependencies={dependencies} /> : <ImpactPanel impact={impact} project={project} />}</section></div></main><footer className="container footer"><span>SourceGraphX / project intelligence</span><span>Built for understanding what depends on what.</span></footer></div>;
}
