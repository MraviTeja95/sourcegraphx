import Link from "next/link";
import type { SearchResult } from "@/types/api";

function formatStars(stars: number | null) {
  return stars === null ? null : stars >= 1000 ? `${Math.round(stars / 100) / 10}k stars` : `${stars} stars`;
}

export function SearchResults({ results }: { results: SearchResult[] }) {
  return (
    <div className="search-result-list" aria-live="polite">
      {results.map((result) => {
        const isProject = result.result_type === "Project";
        const content = (
          <>
            <span className={`result-symbol ${isProject ? "result-project" : "result-package"}`} aria-hidden="true">{isProject ? "P" : "&lt;/&gt;"}</span>
            <span className="search-result-main">
              <strong>{result.name}</strong>
              <span className="search-result-description">{isProject ? result.description : `${result.ecosystem ?? "Unknown"} package`}</span>
              <span className="search-result-id">{result.id}</span>
            </span>
            <span className="search-result-meta">
              <span className={`type-badge ${isProject ? "type-project" : "type-package"}`}>{result.result_type}</span>
              {result.ecosystem && <span>{result.ecosystem}</span>}
              {isProject && formatStars(result.stars) && <span>{formatStars(result.stars)}</span>}
            </span>
            {isProject && <span className="result-arrow" aria-hidden="true">↗</span>}
          </>
        );
        return isProject ? <Link className="search-result-row" href={`/projects/${result.id}`} key={`${result.result_type}-${result.id}`}>{content}</Link> : <div className="search-result-row" key={`${result.result_type}-${result.id}`}>{content}</div>;
      })}
    </div>
  );
}