from typing import Any

from app.db.connection import driver


PROJECT_FIELDS = "project { .id, .name, .description, .language, .stars, .license } AS project"


def _project(record: Any) -> dict:
    return dict(record["project"])


def list_projects() -> list[dict]:
    with driver.session() as session:
        return [dict(record["project"]) for record in session.run(
            f"MATCH (project:Project) RETURN {PROJECT_FIELDS} ORDER BY project.name"
        )]


def get_project(project_id: str) -> dict | None:
    query = f"""
        MATCH (project:Project {{id: $project_id}})
        OPTIONAL MATCH (project)-[:HAS_REPOSITORY]->(repository:Repository)
        OPTIONAL MATCH (project)-[:MAINTAINED_BY]->(maintainer:Maintainer)
        OPTIONAL MATCH (project)-[:TAGGED_WITH]->(tag:Tag)
        OPTIONAL MATCH (project)-[:HAS_VERSION]->(version:Version)
        RETURN {PROJECT_FIELDS},
            repository {{ .id, .url, .platform }} AS repository,
            maintainer {{ .id, .name, .organization }} AS maintainer,
            collect(DISTINCT tag {{ .id, .name }}) AS tags,
            collect(DISTINCT version {{ .id, .version, .release_date }}) AS versions
    """
    with driver.session() as session:
        record = session.run(query, project_id=project_id).single()
        if record is None:
            return None
        result = _project(record)
        result.update({
            "repository": record["repository"],
            "maintainer": record["maintainer"],
            "tags": [dict(tag) for tag in record["tags"] if tag.get("id")],
            "versions": [dict(version) for version in record["versions"] if version.get("id")],
        })
        return result


def get_dependencies(project_id: str) -> dict | None:
    query = f"""
        MATCH (project:Project {{id: $project_id}})
        OPTIONAL MATCH (project)-[:HAS_VERSION]->(version:Version)
        OPTIONAL MATCH (version)-[:DEPENDS_ON]->(package:Package)
        RETURN {PROJECT_FIELDS},
            collect(DISTINCT version {{ .id, .version, .release_date }}) AS versions,
            collect(DISTINCT package {{ .id, .name, .ecosystem }}) AS packages,
            collect(DISTINCT CASE WHEN version IS NOT NULL AND package IS NOT NULL
                THEN {{version: version {{ .id, .version, .release_date }}, package: package {{ .id, .name, .ecosystem }}}}
                END) AS dependency_pairs
    """
    with driver.session() as session:
        record = session.run(query, project_id=project_id).single()
        if record is None:
            return None
        dependency_pairs = [pair for pair in record["dependency_pairs"] if pair is not None]
        versions = []
        for version in record["versions"]:
            if not version.get("id"):
                continue
            version_data = dict(version)
            version_data["packages"] = [
                dict(pair["package"])
                for pair in dependency_pairs
                if pair["version"]["id"] == version["id"]
            ]
            versions.append(version_data)
        return {
            "project": _project(record),
            "versions": versions,
            "packages": [dict(package) for package in record["packages"] if package.get("id")],
        }


def get_impact(project_id: str) -> dict | None:
    query = f"""
        MATCH (project:Project {{id: $project_id}})
        OPTIONAL MATCH (project)-[:HAS_VERSION]->(:Version)-[:DEPENDS_ON]->(package:Package)
        WITH project, collect(DISTINCT package) AS used_packages
        OPTIONAL MATCH (affected:Project)-[:HAS_VERSION]->(:Version)-[:DEPENDS_ON]->(shared:Package)
        WHERE affected <> project AND shared IN used_packages
        WITH project, collect(DISTINCT shared) AS shared_packages,
            collect(DISTINCT CASE WHEN affected IS NOT NULL THEN affected END) AS affected_nodes,
            collect(DISTINCT CASE WHEN affected IS NOT NULL AND shared IS NOT NULL THEN {{
                project_id: affected.id,
                package_id: shared.id,
                package_name: shared.name
            }} END) AS edges
        RETURN {PROJECT_FIELDS},
            [package IN shared_packages WHERE package IS NOT NULL |
                package {{ .id, .name, .ecosystem }}] AS shared_dependencies,
            [affected IN affected_nodes WHERE affected IS NOT NULL |
                affected {{ .id, .name, .description, .language, .stars, .license }}] AS affected_projects,
            [edge IN edges WHERE edge IS NOT NULL | edge] AS impact_edges
    """
    with driver.session() as session:
        record = session.run(query, project_id=project_id).single()
        if record is None:
            return None
        return {
            "project": _project(record),
            "shared_dependencies": [dict(package) for package in record["shared_dependencies"]],
            "affected_projects": [dict(project) for project in record["affected_projects"] if project is not None],
            "impact_edges": [dict(edge) for edge in record["impact_edges"] if edge is not None],
        }


def search(query: str) -> list[dict]:
    cypher = """
        CALL {
            MATCH (project:Project)
            WHERE toLower(project.name) CONTAINS toLower($query)
            RETURN project.id AS id, project.name AS name, 'Project' AS result_type,
                project.description AS description, project.language AS language,
                project.stars AS stars, project.license AS license,
                NULL AS ecosystem
            UNION ALL
            MATCH (package:Package)
            WHERE toLower(package.name) CONTAINS toLower($query)
            RETURN package.id AS id, package.name AS name, 'Package' AS result_type,
                NULL AS description, NULL AS language, NULL AS stars,
                NULL AS license, package.ecosystem AS ecosystem
        }
        RETURN id, name, result_type, description, language, stars, license, ecosystem
        ORDER BY result_type, name
    """
    with driver.session() as session:
        return [dict(record) for record in session.run(cypher, parameters={"query": query})]