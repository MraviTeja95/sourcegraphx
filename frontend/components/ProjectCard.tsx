import Link from "next/link";
import type { ProjectDetail } from "@/types/api";

function formatStars(stars: number) {
  return stars >= 1000 ? `${Math.round(stars / 100) / 10}k` : stars.toString();
}

export function ProjectCard({ project }: { project: ProjectDetail }) {
  const latestVersion = [...project.versions].sort((a, b) => b.release_date.localeCompare(a.release_date))[0];
  return (
    <article className="project-card reveal-on-scroll">
      <div className="card-topline"><span className="language-dot" /> {project.language}<span className="card-arrow" aria-hidden="true">↗</span></div>
      <h2>{project.name}</h2>
      <p>{project.description}</p>
      <div className="card-details"><span><b>Latest</b>{latestVersion?.version ?? "—"}</span><span><b>Maintainer</b>{project.maintainer?.name ?? "—"}</span><span><b>Repository</b>{project.repository?.platform ?? "—"}</span></div>
      <div className="card-tags">{project.tags.slice(0, 3).map((tag) => <span key={tag.id}>#{tag.name}</span>)}</div>
      <div className="card-meta"><span>★ {formatStars(project.stars)}</span><span className="license">{project.license}</span></div>
      <Link href={`/projects/${project.id}`} className="view-project">View Project <span aria-hidden="true">→</span></Link>
    </article>
  );
}