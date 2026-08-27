import Link from "next/link";
import type { Project } from "@/types/api";

function formatStars(stars: number) {
  return stars >= 1000 ? `${Math.round(stars / 100) / 10}k` : stars.toString();
}

export function ProjectCard({ project, index }: { project: Project; index: number }) {
  return (
    <Link href={`/projects/${project.id}`} className="project-card" style={{ "--delay": `${index * 45}ms` } as React.CSSProperties}>
      <div className="card-topline"><span className="language-dot" /> {project.language}<span className="card-arrow" aria-hidden="true">↗</span></div>
      <h2>{project.name}</h2>
      <p>{project.description}</p>
      <div className="card-meta"><span>★ {formatStars(project.stars)}</span><span className="license">{project.license}</span></div>
    </Link>
  );
}