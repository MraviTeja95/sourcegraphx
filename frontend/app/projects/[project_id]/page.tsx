"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { Header } from "@/components/Header";
import { DependencyGraph } from "@/components/DependencyGraph";
import { getDependencies, getImpact, getProject } from "@/lib/api";
import type { DependenciesResponse, ImpactResponse, ProjectDetail } from "@/types/api";

export default function ProjectPage({ params }: { params: Promise<{ project_id: string }> }) {
  const [project, setProject] = useState<ProjectDetail | null>(null);
  const [dependencies, setDependencies] = useState<DependenciesResponse | null>(null);
  const [impact, setImpact] = useState<ImpactResponse | null>(null);
  const [tab, setTab] = useState<"dependencies" | "impact">("dependencies");
  const [error, setError] = useState(false);
  const [projectId, setProjectId] = useState("");

  useEffect(() => {
    params.then(({ project_id }) => {
      setProjectId(project_id);
      getProject(project_id).then(setProject).catch(() => setError(true));
      getDependencies(project_id).then(setDependencies).catch(() => undefined);
      getImpact(project_id).then(setImpact).catch(() => undefined);
    });
  }, [params]);

  if (error) return <div className="app-shell"><Header /><main className="container"><div className="state-box detail-error"><strong>Project not found.</strong><span>The requested project does not exist in the graph.</span><Link href="/">Back to explorer</Link></div></main></div>;
  if (!project) return <div className="app-shell"><Header /><main className="container"><div className="detail-loading"><span className="spinner" /> Loading project graph...</div></main></div>;

  return (
    <div className="app-shell">
      <Header />
      <main className="container detail-page">
        <Link className="back-link" href="/">← Back to projects</Link>
        <section className="project-hero">
          <div className="project-heading"><div className="project-badge">{project.name.slice(0, 2).toUpperCase()}</div><div><p className="section-kicker">PROJECT / {project.language.toUpperCase()}</p><h1>{project.name}</h1><p>{project.description}</p></div></div>
          <div className="hero-actions"><a className="repo-button" href={project.repository?.url} target="_blank" rel="noreferrer">View repository ↗</a></div>
        </section>
        <div className="detail-layout">
          <aside className="detail-sidebar">
            <div className="stat-row"><span>Language</span><strong>{project.language}</strong></div><div className="stat-row"><span>Stars</span><strong>★ {project.stars.toLocaleString()}</strong></div><div className="stat-row"><span>License</span><strong>{project.license}</strong></div>
            <div className="side-block"><p className="section-kicker">MAINTAINER</p><strong>{project.maintainer?.name}</strong><span>{project.maintainer?.organization}</span></div>
            <div className="side-block"><p className="section-kicker">TAGS</p><div className="tag-list">{project.tags.map((tag) => <span key={tag.id}>#{tag.name}</span>)}</div></div>
            <div className="side-block"><p className="section-kicker">RELEASES</p><strong>{project.versions.length} versions</strong><span>Latest: {project.versions.at(-1)?.version}</span></div>
          </aside>
          <section className="analysis-panel">
            <div className="tab-bar"><button className={tab === "dependencies" ? "active" : ""} onClick={() => setTab("dependencies")}>Dependency map <span>{dependencies?.packages.length ?? "–"}</span></button><button className={tab === "impact" ? "active" : ""} onClick={() => setTab("impact")}>Impact analysis <span>{impact?.affected_projects.length ?? "–"}</span></button></div>
            {tab === "dependencies" && dependencies && <div className="analysis-content"><div className="analysis-title"><div><p className="section-kicker">GRAPH VIEW / DEPENDS ON</p><h2>Dependency map</h2></div><span className="graph-count">{dependencies.packages.length} packages · {dependencies.versions.length} versions</span></div><DependencyGraph versions={dependencies.versions} /><div className="version-list"><p className="section-kicker">VERSION HISTORY</p>{dependencies.versions.map((version) => <div className="version-row" key={version.id}><span className="version-number">{version.version}</span><span>{version.release_date}</span><span>{version.packages.length} dependencies</span></div>)}</div></div>}
            {tab === "impact" && impact && <div className="analysis-content impact-content"><div className="impact-summary"><span className="impact-symbol">↗</span><div><p className="section-kicker">BLAST RADIUS</p><h2>{impact.affected_projects.length} projects share dependencies with {project.name}</h2><p>These projects may be affected by changes to the shared packages below.</p></div></div><div className="impact-flow"><div className="flow-column"><span className="flow-label">SOURCE PROJECT</span><div className="flow-node source-node">{project.name}</div></div><span className="flow-arrow">→</span><div className="flow-column"><span className="flow-label">SHARED PACKAGES</span>{impact.shared_dependencies.map((pkg) => <div className="flow-node package-node" key={pkg.id}>{pkg.name}<small>{pkg.ecosystem}</small></div>)}</div><span className="flow-arrow">→</span><div className="flow-column"><span className="flow-label">AFFECTED PROJECTS</span>{impact.affected_projects.map((affected) => <Link href={`/projects/${affected.id}`} className="flow-node affected-node" key={affected.id}>{affected.name}<small>{affected.language}</small></Link>)}</div></div></div>}
          </section>
        </div>
        <span className="sr-only">Project id: {projectId}</span>
      </main>
    </div>
  );
}