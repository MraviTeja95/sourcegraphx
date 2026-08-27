import type {
  DependenciesResponse,
  ImpactResponse,
  Project,
  ProjectDetail,
  SearchResult,
} from "@/types/api";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

async function request<T>(path: string): Promise<T> {
  const response = await fetch(`${API_URL}${path}`);
  if (!response.ok) {
    throw new Error(response.status === 404 ? "Project not found" : "The API request failed");
  }
  return response.json() as Promise<T>;
}

export function getProjects() {
  return request<Project[]>("/api/projects");
}

export function getProject(id: string) {
  return request<ProjectDetail>(`/api/projects/${encodeURIComponent(id)}`);
}

export function getDependencies(id: string) {
  return request<DependenciesResponse>(`/api/projects/${encodeURIComponent(id)}/dependencies`);
}

export function getImpact(id: string) {
  return request<ImpactResponse>(`/api/projects/${encodeURIComponent(id)}/impact`);
}

export function search(query: string) {
  return request<SearchResult[]>(`/api/search?q=${encodeURIComponent(query)}`);
}