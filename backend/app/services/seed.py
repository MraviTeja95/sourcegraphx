from neo4j import Session


PROJECTS = [
    {"id": "project-react", "name": "React", "description": "A library for building user interfaces", "language": "JavaScript", "stars": 231000, "license": "MIT"},
    {"id": "project-nextjs", "name": "Next.js", "description": "The React framework for the web", "language": "TypeScript", "stars": 132000, "license": "MIT"},
    {"id": "project-vue", "name": "Vue", "description": "The progressive JavaScript framework", "language": "TypeScript", "stars": 211000, "license": "MIT"},
    {"id": "project-angular", "name": "Angular", "description": "A web framework for building applications", "language": "TypeScript", "stars": 98000, "license": "MIT"},
    {"id": "project-django", "name": "Django", "description": "The web framework for perfectionists with deadlines", "language": "Python", "stars": 84000, "license": "BSD-3-Clause"},
    {"id": "project-fastapi", "name": "FastAPI", "description": "A modern high-performance web framework for Python", "language": "Python", "stars": 94000, "license": "MIT"},
    {"id": "project-flask", "name": "Flask", "description": "A lightweight WSGI web application framework", "language": "Python", "stars": 69000, "license": "BSD-3-Clause"},
    {"id": "project-express", "name": "Express", "description": "Fast, unopinionated web framework for Node.js", "language": "JavaScript", "stars": 67000, "license": "MIT"},
    {"id": "project-tensorflow", "name": "TensorFlow", "description": "An end-to-end open source machine learning platform", "language": "C++", "stars": 188000, "license": "Apache-2.0"},
    {"id": "project-pytorch", "name": "PyTorch", "description": "An open source machine learning framework", "language": "Python", "stars": 84000, "license": "BSD-3-Clause"},
]

VERSIONS = [
    {"id": "version-react-18", "project_id": "project-react", "version": "18.3.1", "release_date": "2024-04-26"},
    {"id": "version-react-19", "project_id": "project-react", "version": "19.1.1", "release_date": "2025-04-28"},
    {"id": "version-next-14", "project_id": "project-nextjs", "version": "14.2.31", "release_date": "2025-06-04"},
    {"id": "version-next-15", "project_id": "project-nextjs", "version": "15.5.2", "release_date": "2025-08-18"},
    {"id": "version-vue-3", "project_id": "project-vue", "version": "3.5.20", "release_date": "2025-08-14"},
    {"id": "version-vue-2", "project_id": "project-vue", "version": "2.7.16", "release_date": "2024-06-14"},
    {"id": "version-angular-18", "project_id": "project-angular", "version": "18.2.13", "release_date": "2024-11-19"},
    {"id": "version-angular-20", "project_id": "project-angular", "version": "20.1.6", "release_date": "2025-08-13"},
    {"id": "version-django-4", "project_id": "project-django", "version": "4.2.24", "release_date": "2025-05-07"},
    {"id": "version-django-5", "project_id": "project-django", "version": "5.2.5", "release_date": "2025-08-06"},
    {"id": "version-fastapi-0-1", "project_id": "project-fastapi", "version": "0.115.14", "release_date": "2025-06-20"},
    {"id": "version-fastapi-0-2", "project_id": "project-fastapi", "version": "0.116.1", "release_date": "2025-08-05"},
    {"id": "version-flask-2", "project_id": "project-flask", "version": "2.3.3", "release_date": "2023-09-19"},
    {"id": "version-flask-3", "project_id": "project-flask", "version": "3.1.1", "release_date": "2025-05-13"},
    {"id": "version-express-4", "project_id": "project-express", "version": "4.21.2", "release_date": "2024-10-15"},
    {"id": "version-express-5", "project_id": "project-express", "version": "5.1.0", "release_date": "2025-03-31"},
    {"id": "version-tensorflow-2-15", "project_id": "project-tensorflow", "version": "2.15.1", "release_date": "2024-01-12"},
    {"id": "version-tensorflow-2-19", "project_id": "project-tensorflow", "version": "2.19.1", "release_date": "2025-03-15"},
    {"id": "version-pytorch-2-5", "project_id": "project-pytorch", "version": "2.5.1", "release_date": "2024-11-12"},
    {"id": "version-pytorch-2-7", "project_id": "project-pytorch", "version": "2.7.1", "release_date": "2025-06-04"},
]

PACKAGES = [
    {"id": "package-react", "name": "react", "ecosystem": "npm"},
    {"id": "package-react-dom", "name": "react-dom", "ecosystem": "npm"},
    {"id": "package-scheduler", "name": "scheduler", "ecosystem": "npm"},
    {"id": "package-next", "name": "next", "ecosystem": "npm"},
    {"id": "package-sharp", "name": "sharp", "ecosystem": "npm"},
    {"id": "package-typescript", "name": "typescript", "ecosystem": "npm"},
    {"id": "package-vue", "name": "vue", "ecosystem": "npm"},
    {"id": "package-vue-router", "name": "vue-router", "ecosystem": "npm"},
    {"id": "package-pinia", "name": "pinia", "ecosystem": "npm"},
    {"id": "package-angular-core", "name": "@angular/core", "ecosystem": "npm"},
    {"id": "package-rxjs", "name": "rxjs", "ecosystem": "npm"},
    {"id": "package-zone", "name": "zone.js", "ecosystem": "npm"},
    {"id": "package-django", "name": "Django", "ecosystem": "pypi"},
    {"id": "package-asgiref", "name": "asgiref", "ecosystem": "pypi"},
    {"id": "package-sqlparse", "name": "sqlparse", "ecosystem": "pypi"},
    {"id": "package-fastapi", "name": "fastapi", "ecosystem": "pypi"},
    {"id": "package-starlette", "name": "starlette", "ecosystem": "pypi"},
    {"id": "package-pydantic", "name": "pydantic", "ecosystem": "pypi"},
    {"id": "package-flask", "name": "Flask", "ecosystem": "pypi"},
    {"id": "package-werkzeug", "name": "Werkzeug", "ecosystem": "pypi"},
    {"id": "package-jinja", "name": "Jinja2", "ecosystem": "pypi"},
    {"id": "package-click", "name": "click", "ecosystem": "pypi"},
    {"id": "package-express", "name": "express", "ecosystem": "npm"},
    {"id": "package-body-parser", "name": "body-parser", "ecosystem": "npm"},
    {"id": "package-debug", "name": "debug", "ecosystem": "npm"},
    {"id": "package-lodash", "name": "lodash", "ecosystem": "npm"},
    {"id": "package-tensorflow", "name": "tensorflow", "ecosystem": "pypi"},
    {"id": "package-numpy", "name": "numpy", "ecosystem": "pypi"},
    {"id": "package-keras", "name": "keras", "ecosystem": "pypi"},
    {"id": "package-pytorch", "name": "torch", "ecosystem": "pypi"},
    {"id": "package-pytest", "name": "pytest", "ecosystem": "pypi"},
]

MAINTAINERS = [
    {"id": "maintainer-meta", "name": "Meta Open Source", "organization": "Meta"},
    {"id": "maintainer-vercel", "name": "Vercel Core Team", "organization": "Vercel"},
    {"id": "maintainer-evan", "name": "Evan You", "organization": "Vue Project"},
    {"id": "maintainer-angular", "name": "Angular Team", "organization": "Google"},
    {"id": "maintainer-django", "name": "Django Software Foundation", "organization": "DSF"},
    {"id": "maintainer-tiangolo", "name": "Sebastian Ramirez", "organization": "FastAPI"},
    {"id": "maintainer-pallets", "name": "Pallets Team", "organization": "Pallets"},
    {"id": "maintainer-express", "name": "Express Technical Committee", "organization": "OpenJS Foundation"},
    {"id": "maintainer-google", "name": "TensorFlow Team", "organization": "Google"},
    {"id": "maintainer-pytorch", "name": "PyTorch Team", "organization": "Linux Foundation"},
]

TAGS = [
    {"id": "tag-web", "name": "web"},
    {"id": "tag-frontend", "name": "frontend"},
    {"id": "tag-backend", "name": "backend"},
    {"id": "tag-javascript", "name": "javascript"},
    {"id": "tag-typescript", "name": "typescript"},
    {"id": "tag-python", "name": "python"},
    {"id": "tag-machine-learning", "name": "machine-learning"},
    {"id": "tag-framework", "name": "framework"},
    {"id": "tag-open-source", "name": "open-source"},
    {"id": "tag-high-performance", "name": "high-performance"},
]

REPOSITORIES = [
    {"id": "repo-react", "project_id": "project-react", "url": "https://github.com/facebook/react", "platform": "GitHub"},
    {"id": "repo-nextjs", "project_id": "project-nextjs", "url": "https://github.com/vercel/next.js", "platform": "GitHub"},
    {"id": "repo-vue", "project_id": "project-vue", "url": "https://github.com/vuejs/core", "platform": "GitHub"},
    {"id": "repo-angular", "project_id": "project-angular", "url": "https://github.com/angular/angular", "platform": "GitHub"},
    {"id": "repo-django", "project_id": "project-django", "url": "https://github.com/django/django", "platform": "GitHub"},
    {"id": "repo-fastapi", "project_id": "project-fastapi", "url": "https://github.com/fastapi/fastapi", "platform": "GitHub"},
    {"id": "repo-flask", "project_id": "project-flask", "url": "https://github.com/pallets/flask", "platform": "GitHub"},
    {"id": "repo-express", "project_id": "project-express", "url": "https://github.com/expressjs/express", "platform": "GitHub"},
    {"id": "repo-tensorflow", "project_id": "project-tensorflow", "url": "https://github.com/tensorflow/tensorflow", "platform": "GitHub"},
    {"id": "repo-pytorch", "project_id": "project-pytorch", "url": "https://github.com/pytorch/pytorch", "platform": "GitHub"},
]

PROJECT_TAGS = [
    ("project-react", "tag-frontend"), ("project-react", "tag-javascript"), ("project-react", "tag-open-source"),
    ("project-nextjs", "tag-frontend"), ("project-nextjs", "tag-typescript"), ("project-nextjs", "tag-web"),
    ("project-vue", "tag-frontend"), ("project-vue", "tag-javascript"), ("project-vue", "tag-framework"),
    ("project-angular", "tag-frontend"), ("project-angular", "tag-typescript"), ("project-angular", "tag-framework"),
    ("project-django", "tag-backend"), ("project-django", "tag-python"), ("project-django", "tag-web"),
    ("project-fastapi", "tag-backend"), ("project-fastapi", "tag-python"), ("project-fastapi", "tag-high-performance"),
    ("project-flask", "tag-backend"), ("project-flask", "tag-python"), ("project-flask", "tag-web"),
    ("project-express", "tag-backend"), ("project-express", "tag-javascript"), ("project-express", "tag-web"),
    ("project-tensorflow", "tag-machine-learning"), ("project-tensorflow", "tag-python"), ("project-tensorflow", "tag-high-performance"),
    ("project-pytorch", "tag-machine-learning"), ("project-pytorch", "tag-python"), ("project-pytorch", "tag-high-performance"),
]

VERSION_PACKAGES = [
    ("version-react-18", ["package-react", "package-react-dom", "package-scheduler", "package-typescript"]),
    ("version-react-19", ["package-react", "package-react-dom", "package-scheduler", "package-typescript"]),
    ("version-next-14", ["package-next", "package-react", "package-react-dom", "package-sharp", "package-typescript"]),
    ("version-next-15", ["package-next", "package-react", "package-react-dom", "package-sharp", "package-typescript"]),
    ("version-vue-3", ["package-vue", "package-vue-router", "package-pinia", "package-typescript"]),
    ("version-vue-2", ["package-vue", "package-vue-router", "package-typescript"]),
    ("version-angular-18", ["package-angular-core", "package-rxjs", "package-zone", "package-typescript"]),
    ("version-angular-20", ["package-angular-core", "package-rxjs", "package-zone", "package-typescript"]),
    ("version-django-4", ["package-django", "package-asgiref", "package-sqlparse", "package-click"]),
    ("version-django-5", ["package-django", "package-asgiref", "package-sqlparse", "package-click"]),
    ("version-fastapi-0-1", ["package-fastapi", "package-starlette", "package-pydantic", "package-click"]),
    ("version-fastapi-0-2", ["package-fastapi", "package-starlette", "package-pydantic", "package-click"]),
    ("version-flask-2", ["package-flask", "package-werkzeug", "package-jinja", "package-click"]),
    ("version-flask-3", ["package-flask", "package-werkzeug", "package-jinja", "package-click"]),
    ("version-express-4", ["package-express", "package-body-parser", "package-debug", "package-lodash"]),
    ("version-express-5", ["package-express", "package-body-parser", "package-debug", "package-lodash"]),
    ("version-tensorflow-2-15", ["package-tensorflow", "package-numpy", "package-keras", "package-pytest"]),
    ("version-tensorflow-2-19", ["package-tensorflow", "package-numpy", "package-keras", "package-pytest"]),
    ("version-pytorch-2-5", ["package-pytorch", "package-numpy", "package-pytest", "package-typescript"]),
    ("version-pytorch-2-7", ["package-pytorch", "package-numpy", "package-pytest", "package-typescript"]),
]

CONSTRAINTS = [
    "CREATE CONSTRAINT project_id_unique IF NOT EXISTS FOR (n:Project) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT version_id_unique IF NOT EXISTS FOR (n:Version) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT package_id_unique IF NOT EXISTS FOR (n:Package) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT maintainer_id_unique IF NOT EXISTS FOR (n:Maintainer) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT tag_id_unique IF NOT EXISTS FOR (n:Tag) REQUIRE n.id IS UNIQUE",
    "CREATE CONSTRAINT repository_id_unique IF NOT EXISTS FOR (n:Repository) REQUIRE n.id IS UNIQUE",
]


def _run(session: Session, query: str, parameters: dict | None = None) -> None:
    session.run(query, parameters or {}).consume()


def _create_nodes(session: Session) -> None:
    node_queries = [
        ("Project", PROJECTS), ("Version", VERSIONS), ("Package", PACKAGES),
        ("Maintainer", MAINTAINERS), ("Tag", TAGS), ("Repository", REPOSITORIES),
    ]
    for label, rows in node_queries:
        properties = "row += row"
        _run(session, f"UNWIND $rows AS row MERGE (node:{label} {{id: row.id}}) SET node += row", {"rows": rows})


def _create_relationships(session: Session) -> None:
    _run(session, """
        MATCH (project:Project), (version:Version)
        WHERE version.project_id = project.id
        MERGE (project)-[:HAS_VERSION]->(version)
    """)
    _run(session, """
        UNWIND $rows AS row
        MATCH (version:Version {id: row.version_id}), (package:Package {id: row.package_id})
        MERGE (version)-[:DEPENDS_ON]->(package)
    """, {"rows": [{"version_id": version_id, "package_id": package_id} for version_id, package_ids in VERSION_PACKAGES for package_id in package_ids]})
    _run(session, """
        MATCH (project:Project), (maintainer:Maintainer)
        WHERE maintainer.id = CASE project.id
            WHEN 'project-react' THEN 'maintainer-meta'
            WHEN 'project-nextjs' THEN 'maintainer-vercel'
            WHEN 'project-vue' THEN 'maintainer-evan'
            WHEN 'project-angular' THEN 'maintainer-angular'
            WHEN 'project-django' THEN 'maintainer-django'
            WHEN 'project-fastapi' THEN 'maintainer-tiangolo'
            WHEN 'project-flask' THEN 'maintainer-pallets'
            WHEN 'project-express' THEN 'maintainer-express'
            WHEN 'project-tensorflow' THEN 'maintainer-google'
            WHEN 'project-pytorch' THEN 'maintainer-pytorch'
        END
        MERGE (project)-[:MAINTAINED_BY]->(maintainer)
    """)
    _run(session, """
        UNWIND $rows AS row
        MATCH (project:Project {id: row.project_id}), (tag:Tag {id: row.tag_id})
        MERGE (project)-[:TAGGED_WITH]->(tag)
    """, {"rows": [{"project_id": project_id, "tag_id": tag_id} for project_id, tag_id in PROJECT_TAGS]})
    _run(session, """
        UNWIND $rows AS row
        MATCH (project:Project {id: row.project_id}), (repository:Repository {id: row.id})
        MERGE (project)-[:HAS_REPOSITORY]->(repository)
    """, {"rows": REPOSITORIES})


def seed(session: Session) -> None:
    for constraint in CONSTRAINTS:
        _run(session, constraint)
    _create_nodes(session)
    _create_relationships(session)


def collect_validation(session: Session) -> dict:
    total_nodes = session.run("MATCH (node) RETURN count(node) AS count").single()["count"]
    total_relationships = session.run("MATCH ()-[relationship]->() RETURN count(relationship) AS count").single()["count"]
    labels = session.run("MATCH (node) UNWIND labels(node) AS label RETURN label, count(*) AS count ORDER BY label").data()
    relationship_types = session.run("MATCH ()-[relationship]->() RETURN type(relationship) AS type, count(*) AS count ORDER BY type").data()
    missing = {
        "projects_without_versions": session.run("MATCH (project:Project) WHERE NOT (project)-[:HAS_VERSION]->() RETURN count(project) AS count").single()["count"],
        "projects_without_maintainers": session.run("MATCH (project:Project) WHERE NOT (project)-[:MAINTAINED_BY]->() RETURN count(project) AS count").single()["count"],
        "projects_without_repositories": session.run("MATCH (project:Project) WHERE NOT (project)-[:HAS_REPOSITORY]->() RETURN count(project) AS count").single()["count"],
        "projects_without_tags": session.run("MATCH (project:Project) WHERE NOT (project)-[:TAGGED_WITH]->() RETURN count(project) AS count").single()["count"],
    }
    versions_with_dependencies = session.run("MATCH (version:Version)-[:DEPENDS_ON]->() RETURN count(DISTINCT version) AS count").single()["count"]
    analysis_paths = session.run("MATCH path=(project:Project)-[:HAS_VERSION]->(:Version)-[:DEPENDS_ON]->(:Package) RETURN count(path) AS count").single()["count"]
    shared_dependency_packages = session.run("""
        MATCH (first_project:Project)-[:HAS_VERSION]->(:Version)-[:DEPENDS_ON]->(package:Package)<-[:DEPENDS_ON]-(:Version)<-[:HAS_VERSION]-(second_project:Project)
        WHERE first_project <> second_project
        RETURN count(DISTINCT package) AS count
    """).single()["count"]
    return {"total_nodes": total_nodes, "total_relationships": total_relationships, "labels": labels, "relationship_types": relationship_types, "missing": missing, "versions_with_dependencies": versions_with_dependencies, "analysis_paths": analysis_paths, "shared_dependency_packages": shared_dependency_packages}