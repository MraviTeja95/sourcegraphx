"use client";

import Link from "next/link";
import { Suspense, useEffect, useRef, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { Header } from "@/components/Header";
import { SearchResults } from "@/components/SearchResults";
import { search } from "@/lib/api";
import type { SearchResult } from "@/types/api";

function SearchContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const urlQuery = (searchParams.get("q") ?? "").trim();
  const inputRef = useRef<HTMLInputElement>(null);
  const [results, setResults] = useState<SearchResult[]>([]);
  const [completedQuery, setCompletedQuery] = useState<string | null>(urlQuery ? null : "");
  const [resultState, setResultState] = useState<"success" | "error" | null>(null);

  useEffect(() => {
    if (!urlQuery) {
      return;
    }
    let active = true;
    search(urlQuery).then((nextResults) => {
      if (!active) return;
      setResults(nextResults);
      setCompletedQuery(urlQuery);
      setResultState("success");
    }).catch(() => {
      if (!active) return;
      setResults([]);
      setCompletedQuery(urlQuery);
      setResultState("error");
    });
    return () => { active = false; };
  }, [urlQuery]);

  const submitSearch = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const trimmed = inputRef.current?.value.trim() ?? "";
    router.push(trimmed ? `/search?q=${encodeURIComponent(trimmed)}` : "/search");
  };

  const status = !urlQuery ? "idle" : completedQuery === urlQuery ? resultState ?? "loading" : "loading";
  const heading = status === "idle" ? "Search the graph" : status === "loading" ? "Searching the graph" : status === "error" ? "Search unavailable" : results.length === 0 ? "No results found" : `Results for “${urlQuery}”`;

  return (
    <div className="app-shell">
      <Header />
      <main className="container search-page">
        <div className="search-page-intro">
          <Link className="back-link" href="/">← Back to explorer</Link>
          <p className="section-kicker">GRAPH SEARCH / PROJECTS + PACKAGES</p>
          <h1>Find what the graph knows.</h1>
          <p>Search across open-source projects and the packages they depend on.</p>
        </div>
        <form className="search-page-form" onSubmit={submitSearch}>
          <label htmlFor="search-page-input">Search projects and packages</label>
          <div className="search-page-input-shell"><span className="search-icon" aria-hidden="true">⌕</span><input key={urlQuery} ref={inputRef} id="search-page-input" defaultValue={urlQuery} placeholder="Try React, Python, or fastapi..." autoComplete="off" /><button type="submit">Search <span aria-hidden="true">↗</span></button></div>
        </form>
        <section className="search-results-section" aria-labelledby="search-results-title">
          <div className="search-results-heading"><div><p className="section-kicker">RESULTS</p><h2 id="search-results-title">{heading}</h2></div>{status === "success" && <span className="count-label">{results.length} matches</span>}</div>
          {status === "idle" && <div className="search-state"><span className="state-mark">⌕</span><strong>Start with a project or package name</strong><span>Results are powered by the live SourceGraphX graph.</span></div>}
          {status === "loading" && <div className="search-state"><span className="spinner" /><strong>Searching...</strong><span>Following names across the project graph.</span></div>}
          {status === "error" && <div className="search-state"><strong>Failed to search the graph</strong><span>Check that the FastAPI backend is running and try again.</span></div>}
          {status === "success" && results.length === 0 && <div className="search-state"><strong>No results found</strong><span>Try a broader project or package name.</span></div>}
          {status === "success" && results.length > 0 && <SearchResults results={results} />}
        </section>
      </main>
      <footer className="container footer"><span>SourceGraphX / graph search</span><span>Projects and packages, connected.</span></footer>
    </div>
  );
}

export default function SearchPage() {
  return <Suspense fallback={<div className="app-shell"><Header /><main className="container search-page"><div className="search-state"><span className="spinner" /><strong>Loading search...</strong></div></main></div>}><SearchContent /></Suspense>;
}