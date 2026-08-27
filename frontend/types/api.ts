export type Project = {
  id: string;
  name: string;
  description: string;
  language: string;
  stars: number;
  license: string;
};

export type Version = {
  id: string;
  version: string;
  release_date: string;
};

export type Package = {
  id: string;
  name: string;
  ecosystem: string;
};

export type Maintainer = {
  id: string;
  name: string;
  organization: string;
};

export type Tag = {
  id: string;
  name: string;
};

export type Repository = {
  id: string;
  url: string;
  platform: string;
};

export type ProjectDetail = Project & {
  repository: Repository | null;
  maintainer: Maintainer | null;
  tags: Tag[];
  versions: Version[];
};

export type VersionDependencies = Version & { packages: Package[] };

export type DependenciesResponse = {
  project: Project;
  versions: VersionDependencies[];
  packages: Package[];
};

export type ImpactEdge = {
  project_id: string;
  package_id: string;
  package_name: string;
};

export type ImpactResponse = {
  project: Project;
  shared_dependencies: Package[];
  affected_projects: Project[];
  impact_edges: ImpactEdge[];
};

export type SearchResult = {
  id: string;
  name: string;
  result_type: "Project" | "Package";
  description: string | null;
  language: string | null;
  stars: number | null;
  license: string | null;
  ecosystem: string | null;
};