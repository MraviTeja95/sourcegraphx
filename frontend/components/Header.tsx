import Link from "next/link";

export function Header() {
  return (
    <header className="site-header">
      <Link className="brand" href="/" aria-label="SourceGraphX home">
        <span className="brand-mark" aria-hidden="true">SX</span>
        <span>SourceGraph<span className="brand-accent">X</span></span>
      </Link>
      <nav className="site-nav" aria-label="Primary navigation">
        <Link href="/#explore">Explore</Link>
        <Link href="/search">Search</Link>
        <a href={`${process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000"}/docs`} target="_blank" rel="noreferrer">API docs <span aria-hidden="true">↗</span></a>
      </nav>
      <span className="status-pill"><span className="status-dot" /> API online</span>
    </header>
  );
}