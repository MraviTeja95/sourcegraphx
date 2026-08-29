"use client";

import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { Header } from "@/components/Header";
import { ProjectCard } from "@/components/ProjectCard";
import { getProject, getProjects } from "@/lib/api";
import type { ProjectDetail } from "@/types/api";

export default function Home() {
  const [projects, setProjects] = useState<ProjectDetail[]>([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [displayLimit, setDisplayLimit] = useState(10);
  const gridRef = useRef<HTMLDivElement>(null);
  const router = useRouter();

  useEffect(() => {
    getProjects()
      .then((catalog) => Promise.all(catalog.map((project) => getProject(project.id))))
      .then(setProjects)
      .catch(() => setError(true))
      .finally(() => setLoading(false));
  }, []);

  // Scroll-reveal for project cards
  useEffect(() => {
    if (loading || error || projects.length === 0) return;
    const grid = gridRef.current;
    if (!grid) return;
    const cards = grid.querySelectorAll('.project-card');
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: '0px 0px -40px 0px' }
    );
    cards.forEach((card) => observer.observe(card));
    return () => observer.disconnect();
  }, [loading, error, projects, displayLimit]);

  const normalizedQuery = query.trim().toLowerCase();
  const searchSuggestions = normalizedQuery ? projects.filter((project) => {
    return [project.name, project.description, project.maintainer?.name, project.maintainer?.organization, ...project.tags.map((tag) => tag.name)]
      .filter(Boolean)
      .some((value) => value!.toLowerCase().includes(normalizedQuery));
  }) : [];

  return (
    <div className="app-shell">
      <Header />
      <main>
        <section className="hero container">
          <div className="eyebrow"><span className="eyebrow-line" /> OPEN SOURCE INTELLIGENCE</div>
          <h1>See how the<br /><em>open source</em> world connects.</h1>
          <p className="hero-copy">Explore open-source projects, dependencies, and impact through a graph.</p>
          <div className="search-wrap" id="search">
            <form className="search-input-shell" onSubmit={(e) => {
              e.preventDefault();
              const trimmed = query.trim();
              if (trimmed) router.push(`/search?q=${encodeURIComponent(trimmed)}`);
              else router.push("/search");
            }}>
              <span className="search-icon" aria-hidden="true">⌕</span>
              <label className="sr-only" htmlFor="project-search">Search projects by name, description, maintainer, or tag</label>
              <input id="project-search" value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Filter projects by name, maintainer, or tag..." autoComplete="off" />
              {query ? <button className="clear-search" type="button" onClick={() => setQuery("")} aria-label="Clear project search">×</button> : <kbd>⌘ K</kbd>}
            </form>
            {query && (
              <div className="search-results" role="region" aria-live="polite">
                {searchSuggestions.map((project) => (
                  <Link key={`project-${project.id}`} href={`/projects/${project.id}`} className="search-result">
                    <span className="result-icon project-icon">P</span>
                    <span><strong>{project.name}</strong><small>{project.description}</small></span>
                    <em>Project</em>
                  </Link>
                ))}
                {searchSuggestions.length === 0 && <p className="search-empty">No projects found.</p>}
              </div>
            )}
          </div>
          <div className="hero-note"><span className="pulse" /> Live graph data from CognoDB <span className="note-divider" /> 91 nodes indexed <span className="note-divider" /> 151 relationships</div>
        </section>
        <section className="explorer container" id="explore" aria-labelledby="explorer-title">
          <div className="section-heading"><div><p className="section-kicker">THE CATALOG</p><h2 id="explorer-title">Explore projects</h2></div><span className="count-label">{loading ? "Loading" : `${projects.length} projects`}</span></div>
          {loading && <><div className="loading-label" aria-live="polite">Loading projects...</div><div className="project-grid">{[1, 2, 3, 4, 5, 6].map((item) => <div className="skeleton-card" key={item} />)}</div></>}
          {error && <div className="state-box"><strong>Failed to load projects</strong><span>Make sure the FastAPI backend is running on port 8000.</span></div>}
          {!loading && !error && projects.length === 0 && <div className="state-box"><strong>No projects found.</strong><span>The catalog is currently empty.</span></div>}
          {!loading && !error && projects.length > 0 && (
            <>
              <div className="project-grid" ref={gridRef}>
                {projects.slice(0, displayLimit).map((project) => <ProjectCard key={project.id} project={project} />)}
              </div>
              {projects.length > displayLimit && (
                <div style={{ marginTop: "44px", textAlign: "center" }}>
                  <button type="button" onClick={() => setDisplayLimit((prev) => prev + 10)} className="repo-button">Show More Projects</button>
                </div>
              )}
            </>
          )}
        </section>
      </main>
      <footer className="container footer"><span>SourceGraphX / project explorer</span><span>Built for understanding what depends on what.</span></footer>
    </div>
  );
}
