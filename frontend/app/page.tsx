"use client";

import { useEffect, useState } from "react";
import { Header } from "@/components/Header";
import { ProjectCard } from "@/components/ProjectCard";
import { SearchBar } from "@/components/SearchBar";
import { getProjects } from "@/lib/api";
import type { Project } from "@/types/api";

export default function Home() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    getProjects().then(setProjects).catch(() => setError(true)).finally(() => setLoading(false));
  }, []);

  return (
    <div className="app-shell">
      <Header />
      <main>
        <section className="hero container">
          <div className="eyebrow"><span className="eyebrow-line" /> OPEN SOURCE INTELLIGENCE</div>
          <h1>See how the<br /><em>open source</em> world connects.</h1>
          <p className="hero-copy">Explore open-source projects, dependencies, and impact through a graph.</p>
          <SearchBar />
          <div className="hero-note"><span className="pulse" /> Live graph data from CognoDB <span className="note-divider" /> 91 nodes indexed <span className="note-divider" /> 151 relationships</div>
        </section>
        <section className="explorer container" aria-labelledby="explorer-title">
          <div className="section-heading"><div><p className="section-kicker">THE CATALOG</p><h2 id="explorer-title">Explore projects</h2></div><span className="count-label">{loading ? "Loading" : `${projects.length} projects`}</span></div>
          {loading && <div className="project-grid">{[1, 2, 3, 4, 5, 6].map((item) => <div className="skeleton-card" key={item} />)}</div>}
          {error && <div className="state-box"><strong>Couldn&apos;t reach the project catalog.</strong><span>Make sure the FastAPI backend is running on port 8000.</span></div>}
          {!loading && !error && projects.length === 0 && <div className="state-box"><strong>No projects found.</strong><span>The catalog is currently empty.</span></div>}
          {!loading && !error && projects.length > 0 && <div className="project-grid">{projects.map((project, index) => <ProjectCard key={project.id} project={project} index={index} />)}</div>}
        </section>
      </main>
      <footer className="container footer"><span>SourceGraphX / project explorer</span><span>Built for understanding what depends on what.</span></footer>
    </div>
  );
}
