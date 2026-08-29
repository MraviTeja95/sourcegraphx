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

DEPENDENCY_METADATA = {
    "version-react-18": [("loose-envify", "npm", "^1.1.0", "runtime")],
    "version-react-19": [],
    "version-next-14": [
        ("busboy", "npm", "1.6.0", "runtime"), ("postcss", "npm", "8.4.31", "runtime"),
        ("@next/env", "npm", "14.2.31", "runtime"), ("styled-jsx", "npm", "5.1.1", "runtime"),
        ("graceful-fs", "npm", "^4.2.11", "runtime"), ("@swc/helpers", "npm", "0.5.5", "runtime"),
        ("caniuse-lite", "npm", "^1.0.30001579", "runtime"),
        ("react", "npm", "^18.2.0", "peer"), ("react-dom", "npm", "^18.2.0", "peer"),
    ],
    "version-next-15": [
        ("postcss", "npm", "8.4.31", "runtime"), ("@next/env", "npm", "15.5.2", "runtime"),
        ("styled-jsx", "npm", "5.1.6", "runtime"), ("@swc/helpers", "npm", "0.5.15", "runtime"),
        ("caniuse-lite", "npm", "^1.0.30001579", "runtime"), ("react", "npm", "^18.2.0 || ^19.0.0", "peer"),
        ("react-dom", "npm", "^18.2.0 || ^19.0.0", "peer"), ("sharp", "npm", "^0.34.3", "optional"),
    ],
    "version-vue-2": [("csstype", "npm", "^3.1.0", "runtime"), ("@vue/compiler-sfc", "npm", "2.7.16", "runtime")],
    "version-vue-3": [
        ("@vue/shared", "npm", "3.5.20", "runtime"), ("@vue/runtime-dom", "npm", "3.5.20", "runtime"),
        ("@vue/compiler-dom", "npm", "3.5.20", "runtime"), ("@vue/compiler-sfc", "npm", "3.5.20", "runtime"),
        ("@vue/server-renderer", "npm", "3.5.20", "runtime"), ("typescript", "npm", "*", "peer"),
    ],
    "version-angular-18": [("tslib", "npm", "^2.3.0", "runtime"), ("rxjs", "npm", "^6.5.3 || ^7.4.0", "peer"), ("zone.js", "npm", "~0.14.10", "peer")],
    "version-angular-20": [("tslib", "npm", "^2.3.0", "runtime"), ("rxjs", "npm", "^6.5.3 || ^7.4.0", "peer"), ("zone.js", "npm", "~0.15.0", "peer"), ("@angular/compiler", "npm", "20.1.6", "peer")],
    "version-django-4": [("asgiref", "pypi", "<4,>=3.6.0", "runtime"), ("sqlparse", "pypi", ">=0.3.1", "runtime"), ("tzdata", "pypi", "*", "runtime", "sys_platform == 'win32'")],
    "version-django-5": [("asgiref", "pypi", ">=3.8.1", "runtime"), ("sqlparse", "pypi", ">=0.3.1", "runtime"), ("tzdata", "pypi", "*", "runtime", "sys_platform == 'win32'")],
    "version-fastapi-0-1": [("starlette", "pypi", "<0.47.0,>=0.40.0", "runtime"), ("pydantic", "pypi", ">=1.7.4,<3.0.0", "runtime"), ("typing-extensions", "pypi", ">=4.8.0", "runtime")],
    "version-fastapi-0-2": [("starlette", "pypi", "<0.48.0,>=0.40.0", "runtime"), ("pydantic", "pypi", ">=1.7.4,<3.0.0", "runtime"), ("typing-extensions", "pypi", ">=4.8.0", "runtime")],
    "version-flask-2": [
        ("Werkzeug", "pypi", ">=2.3.7", "runtime"), ("Jinja2", "pypi", ">=3.1.2", "runtime"),
        ("itsdangerous", "pypi", ">=2.1.2", "runtime"), ("click", "pypi", ">=8.1.3", "runtime"), ("blinker", "pypi", ">=1.6.2", "runtime"),
    ],
    "version-flask-3": [
        ("blinker", "pypi", ">=1.9.0", "runtime"), ("click", "pypi", ">=8.1.3", "runtime"),
        ("itsdangerous", "pypi", ">=2.2.0", "runtime"), ("Jinja2", "pypi", ">=3.1.2", "runtime"),
        ("MarkupSafe", "pypi", ">=2.1.1", "runtime"), ("Werkzeug", "pypi", ">=3.1.0", "runtime"),
    ],
    "version-express-4": [
        ("qs", "npm", "6.13.0", "runtime"), ("depd", "npm", "2.0.0", "runtime"), ("etag", "npm", "~1.8.1", "runtime"),
        ("send", "npm", "0.19.0", "runtime"), ("vary", "npm", "~1.1.2", "runtime"), ("debug", "npm", "2.6.9", "runtime"),
        ("fresh", "npm", "0.5.2", "runtime"), ("cookie", "npm", "0.7.1", "runtime"), ("accepts", "npm", "~1.3.8", "runtime"),
        ("methods", "npm", "~1.1.2", "runtime"), ("type-is", "npm", "~1.6.18", "runtime"), ("parseurl", "npm", "~1.3.3", "runtime"),
        ("statuses", "npm", "2.0.1", "runtime"), ("encodeurl", "npm", "~2.0.0", "runtime"), ("proxy-addr", "npm", "~2.0.7", "runtime"),
        ("body-parser", "npm", "1.20.3", "runtime"), ("escape-html", "npm", "~1.0.3", "runtime"), ("http-errors", "npm", "2.0.0", "runtime"),
        ("on-finished", "npm", "2.4.1", "runtime"), ("safe-buffer", "npm", "5.2.1", "runtime"), ("utils-merge", "npm", "1.0.1", "runtime"),
        ("content-type", "npm", "~1.0.4", "runtime"), ("finalhandler", "npm", "1.3.1", "runtime"), ("range-parser", "npm", "~1.2.1", "runtime"),
        ("serve-static", "npm", "1.16.2", "runtime"), ("array-flatten", "npm", "1.1.1", "runtime"), ("path-to-regexp", "npm", "0.1.12", "runtime"),
        ("setprototypeof", "npm", "1.2.0", "runtime"), ("cookie-signature", "npm", "1.0.6", "runtime"), ("merge-descriptors", "npm", "1.0.3", "runtime"),
        ("content-disposition", "npm", "0.5.4", "runtime"),
    ],
    "version-express-5": [
        ("qs", "npm", "^6.14.0", "runtime"), ("etag", "npm", "^1.8.1", "runtime"), ("once", "npm", "^1.4.0", "runtime"),
        ("send", "npm", "^1.1.0", "runtime"), ("vary", "npm", "^1.1.2", "runtime"), ("debug", "npm", "^4.4.0", "runtime"),
        ("fresh", "npm", "^2.0.0", "runtime"), ("cookie", "npm", "^0.7.1", "runtime"), ("router", "npm", "^2.2.0", "runtime"),
        ("accepts", "npm", "^2.0.0", "runtime"), ("type-is", "npm", "^2.0.1", "runtime"), ("parseurl", "npm", "^1.3.3", "runtime"),
        ("statuses", "npm", "^2.0.0", "runtime"), ("encodeurl", "npm", "^2.0.0", "runtime"), ("mime-types", "npm", "^3.0.0", "runtime"),
        ("proxy-addr", "npm", "^2.0.7", "runtime"), ("body-parser", "npm", "^2.2.0", "runtime"), ("escape-html", "npm", "^1.0.3", "runtime"),
        ("http-errors", "npm", "^2.0.0", "runtime"), ("on-finished", "npm", "^2.4.1", "runtime"), ("content-type", "npm", "^1.0.5", "runtime"),
        ("finalhandler", "npm", "^2.1.0", "runtime"), ("range-parser", "npm", "^1.2.1", "runtime"), ("serve-static", "npm", "^2.2.0", "runtime"),
        ("cookie-signature", "npm", "^1.2.1", "runtime"), ("merge-descriptors", "npm", "^2.0.0", "runtime"), ("content-disposition", "npm", "^1.0.0", "runtime"),
    ],
    "version-tensorflow-2-15": [
        ("absl-py", "pypi", ">=1.0.0", "runtime"), ("astunparse", "pypi", ">=1.6.0", "runtime"), ("flatbuffers", "pypi", ">=23.5.26", "runtime"),
        ("gast", "pypi", ">=0.2.1,!=0.5.0,!=0.5.1,!=0.5.2", "runtime"), ("google-pasta", "pypi", ">=0.1.1", "runtime"),
        ("h5py", "pypi", ">=2.9.0", "runtime"), ("libclang", "pypi", ">=13.0.0", "runtime"), ("ml-dtypes", "pypi", "~=0.3.1", "runtime"),
        ("numpy", "pypi", ">=1.23.5,<2.0.0", "runtime"), ("opt-einsum", "pypi", ">=2.3.2", "runtime"), ("packaging", "pypi", "*", "runtime"),
        ("protobuf", "pypi", ">=3.20.3,<5.0.0dev", "runtime"), ("setuptools", "pypi", "*", "runtime"), ("six", "pypi", ">=1.12.0", "runtime"),
        ("termcolor", "pypi", ">=1.1.0", "runtime"), ("typing-extensions", "pypi", ">=3.6.6", "runtime"), ("wrapt", "pypi", ">=1.11.0,<1.15", "runtime"),
        ("tensorflow-io-gcs-filesystem", "pypi", ">=0.23.1", "runtime"), ("grpcio", "pypi", ">=1.24.3,<2.0", "runtime"),
        ("tensorboard", "pypi", ">=2.15,<2.16", "runtime"), ("tensorflow-estimator", "pypi", ">=2.15.0,<2.16", "runtime"), ("keras", "pypi", ">=2.15.0,<2.16", "runtime"),
    ],
    "version-tensorflow-2-19": [
        ("absl-py", "pypi", ">=1.0.0", "runtime"), ("astunparse", "pypi", ">=1.6.0", "runtime"), ("flatbuffers", "pypi", ">=24.3.25", "runtime"),
        ("gast", "pypi", ">=0.2.1,!=0.5.0,!=0.5.1,!=0.5.2", "runtime"), ("google-pasta", "pypi", ">=0.1.1", "runtime"),
        ("libclang", "pypi", ">=13.0.0", "runtime"), ("opt-einsum", "pypi", ">=2.3.2", "runtime"), ("packaging", "pypi", "*", "runtime"),
        ("protobuf", "pypi", ">=3.20.3,<6.0.0dev", "runtime"), ("requests", "pypi", ">=2.21.0,<3", "runtime"), ("setuptools", "pypi", "*", "runtime"),
        ("six", "pypi", ">=1.12.0", "runtime"), ("termcolor", "pypi", ">=1.1.0", "runtime"), ("typing-extensions", "pypi", ">=3.6.6", "runtime"),
        ("wrapt", "pypi", ">=1.11.0", "runtime"), ("grpcio", "pypi", ">=1.24.3,<2.0", "runtime"), ("tensorboard", "pypi", "~=2.19.0", "runtime"),
        ("keras", "pypi", ">=3.5.0", "runtime"), ("numpy", "pypi", ">=1.26.0,<2.2.0", "runtime"), ("h5py", "pypi", ">=3.11.0", "runtime"), ("ml-dtypes", "pypi", ">=0.5.1,<1.0.0", "runtime"),
    ],
    "version-pytorch-2-5": [("filelock", "pypi", "*", "runtime"), ("typing-extensions", "pypi", ">=4.8.0", "runtime"), ("networkx", "pypi", "*", "runtime"), ("jinja2", "pypi", "*", "runtime"), ("fsspec", "pypi", "*", "runtime"), ("sympy", "pypi", "==1.13.1", "runtime")],
    "version-pytorch-2-7": [("filelock", "pypi", "*", "runtime"), ("typing-extensions", "pypi", ">=4.10.0", "runtime"), ("setuptools", "pypi", "*", "runtime"), ("sympy", "pypi", ">=1.13.3", "runtime"), ("networkx", "pypi", "*", "runtime"), ("jinja2", "pypi", "*", "runtime"), ("fsspec", "pypi", "*", "runtime")],
}


def _package_id(name: str, ecosystem: str) -> str:
    for package in PACKAGES:
        if package["name"].lower() == name.lower() and package["ecosystem"] == ecosystem:
            return package["id"]
    prefix = "npm" if ecosystem == "npm" else "pypi"
    normalized = "".join(character if character.isalnum() else "-" for character in name.lower()).strip("-")
    return f"package-{prefix}-{normalized}"


def _extend_package_catalog() -> None:
    existing = {(package["name"].lower(), package["ecosystem"]) for package in PACKAGES}
    for dependencies in DEPENDENCY_METADATA.values():
        for dependency in dependencies:
            name, ecosystem = dependency[0], dependency[1]
            if (name.lower(), ecosystem) not in existing:
                PACKAGES.append({"id": _package_id(name, ecosystem), "name": name, "ecosystem": ecosystem})
                existing.add((name.lower(), ecosystem))


_extend_package_catalog()

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
    _run(session, "MATCH ()-[relationship:DEPENDS_ON]->() DELETE relationship")
    _run(session, """
        MATCH (project:Project), (version:Version)
        WHERE version.project_id = project.id
        MERGE (project)-[:HAS_VERSION]->(version)
    """)
    _run(session, """
        UNWIND $rows AS row
        MATCH (version:Version {id: row.version_id}), (package:Package {id: row.package_id})
        MERGE (version)-[dependency:DEPENDS_ON]->(package)
        SET dependency.version_constraint = row.version_constraint,
            dependency.dependency_type = row.dependency_type,
            dependency.environment_marker = row.environment_marker
    """, {"rows": [
        {"version_id": version_id, "package_id": _package_id(name, ecosystem), "version_constraint": constraint, "dependency_type": dependency_type, "environment_marker": marker if len(dependency) > 4 else None}
        for version_id, dependencies in DEPENDENCY_METADATA.items()
        for dependency in dependencies
        for name, ecosystem, constraint, dependency_type, *marker in [dependency]
    ]})
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
    dependencies_per_version = session.run("""
        MATCH (version:Version)
        OPTIONAL MATCH (version)-[:DEPENDS_ON]->(package:Package)
        RETURN version.id AS version_id, version.version AS version, count(package) AS dependency_count
        ORDER BY version_id
    """).data()
    zero_dependency_versions = session.run("MATCH (version:Version) WHERE NOT (version)-[:DEPENDS_ON]->() RETURN count(version) AS count").single()["count"]
    self_dependencies = session.run("""
        MATCH (project:Project)-[:HAS_VERSION]->(version:Version)-[:DEPENDS_ON]->(package:Package)
        WHERE toLower(package.name) = toLower(project.name)
        RETURN count(*) AS count
    """).single()["count"]
    duplicate_mappings = session.run("""
        MATCH (version:Version)-[:DEPENDS_ON]->(package:Package)
        WITH version.id AS version_id, package.id AS package_id, count(*) AS mapping_count
        WHERE mapping_count > 1
        RETURN count(*) AS count
    """).single()["count"]
    dangling_references = session.run("""
        MATCH (source)-[dependency:DEPENDS_ON]->(target)
        WHERE NOT source:Version OR NOT target:Package
        RETURN count(dependency) AS count
    """).single()["count"]
    shared_dependency_packages = session.run("""
        MATCH (first_project:Project)-[:HAS_VERSION]->(:Version)-[:DEPENDS_ON]->(package:Package)<-[:DEPENDS_ON]-(:Version)<-[:HAS_VERSION]-(second_project:Project)
        WHERE first_project <> second_project
        RETURN count(DISTINCT package) AS count
    """).single()["count"]
    return {"total_nodes": total_nodes, "total_relationships": total_relationships, "labels": labels, "relationship_types": relationship_types, "missing": missing, "versions_with_dependencies": versions_with_dependencies, "analysis_paths": analysis_paths, "shared_dependency_packages": shared_dependency_packages, "dependencies_per_version": dependencies_per_version, "zero_dependency_versions": zero_dependency_versions, "self_dependencies": self_dependencies, "duplicate_mappings": duplicate_mappings, "dangling_references": dangling_references}