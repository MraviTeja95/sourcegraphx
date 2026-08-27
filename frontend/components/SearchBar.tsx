"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { search } from "@/lib/api";
import type { SearchResult } from "@/types/api";

export function SearchBar() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [searched, setSearched] = useState(false);

  useEffect(() => {
    const trimmed = query.trim();
    if (!trimmed) {
      return;
    }
    const timer = window.setTimeout(async () => {
      setLoading(true);
      try {
        setResults(await search(trimmed));
        setSearched(true);
      } catch {
        setResults([]);
        setSearched(true);
      } finally {
        setLoading(false);
      }
    }, 300);
    return () => window.clearTimeout(timer);
  }, [query]);

  return (
    <div className="search-wrap" id="search">
      <div className="search-input-shell">
        <span className="search-icon" aria-hidden="true">⌕</span>
        <input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search projects or packages..."
          aria-label="Search projects or packages"
        />
        {loading ? <span className="spinner" aria-label="Searching" /> : <kbd>⌘ K</kbd>}
      </div>
      {query && (
        <div className="search-results" role="region" aria-live="polite">
          {results.map((result) => result.result_type === "Project" ? (
            <Link key={`${result.result_type}-${result.id}`} href={`/projects/${result.id}`} className="search-result">
              <span className="result-icon project-icon">P</span>
              <span><strong>{result.name}</strong><small>{result.description}</small></span>
              <em>Project</em>
            </Link>
          ) : (
            <div key={`${result.result_type}-${result.id}`} className="search-result package-result">
              <span className="result-icon package-icon">&lt;/&gt;</span>
              <span><strong>{result.name}</strong><small>{result.ecosystem} package</small></span>
              <em>Package</em>
            </div>
          ))}
          {searched && !loading && results.length === 0 && <p className="search-empty">No projects or packages found.</p>}
        </div>
      )}
    </div>
  );
}