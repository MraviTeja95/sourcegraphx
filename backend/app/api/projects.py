from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from app.services import project_service


router = APIRouter(prefix="/api", tags=["projects"])


class Project(BaseModel):
    id: str
    name: str
    description: str
    language: str
    stars: int
    license: str


class Version(BaseModel):
    id: str
    version: str
    release_date: str


class Package(BaseModel):
    id: str
    name: str
    ecosystem: str


class Maintainer(BaseModel):
    id: str
    name: str
    organization: str


class Tag(BaseModel):
    id: str
    name: str


class Repository(BaseModel):
    id: str
    url: str
    platform: str


class ProjectDetail(Project):
    repository: Repository | None
    maintainer: Maintainer | None
    tags: list[Tag]
    versions: list[Version]


class VersionDependencies(Version):
    packages: list[Package]


class DependenciesResponse(BaseModel):
    project: Project
    versions: list[VersionDependencies]
    packages: list[Package]


class ImpactEdge(BaseModel):
    project_id: str
    package_id: str
    package_name: str


class ImpactResponse(BaseModel):
    project: Project
    shared_dependencies: list[Package]
    affected_projects: list[Project]
    impact_edges: list[ImpactEdge]


class SearchResult(BaseModel):
    id: str
    name: str
    result_type: str
    description: str | None = None
    language: str | None = None
    stars: int | None = None
    license: str | None = None
    ecosystem: str | None = None


def _not_found(project_id: str) -> HTTPException:
    return HTTPException(status_code=404, detail=f"Project '{project_id}' not found")


@router.get("/projects", response_model=list[Project])
def list_projects() -> list[dict]:
    return project_service.list_projects()


@router.get("/projects/{project_id}", response_model=ProjectDetail)
def get_project(project_id: str) -> dict:
    project = project_service.get_project(project_id)
    if project is None:
        raise _not_found(project_id)
    return project


@router.get("/projects/{project_id}/dependencies", response_model=DependenciesResponse)
def get_dependencies(project_id: str) -> dict:
    dependencies = project_service.get_dependencies(project_id)
    if dependencies is None:
        raise _not_found(project_id)
    return dependencies


@router.get("/projects/{project_id}/impact", response_model=ImpactResponse)
def get_impact(project_id: str) -> dict:
    impact = project_service.get_impact(project_id)
    if impact is None:
        raise _not_found(project_id)
    return impact


@router.get("/search", response_model=list[SearchResult])
def search_projects_and_packages(q: str = Query(min_length=1)) -> list[dict]:
    if not q.strip():
        raise HTTPException(status_code=400, detail="Query parameter 'q' must not be blank")
    return project_service.search(q.strip())