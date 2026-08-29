from app.db.connection import driver
from app.services.seed import collect_validation, seed


def main() -> None:
    try:
        with driver.session() as session:
            seed(session)
            validation = collect_validation(session)

        print("Seed completed successfully.")
        print(f"Projects: {validation['labels'][0]['count'] if validation['labels'] and validation['labels'][0]['label'] == 'Project' else next(item['count'] for item in validation['labels'] if item['label'] == 'Project')}")
        for label, plural in (("Version", "Versions"), ("Package", "Packages"), ("Maintainer", "Maintainers"), ("Tag", "Tags"), ("Repository", "Repositories")):
            print(f"{plural}: {next(item['count'] for item in validation['labels'] if item['label'] == label)}")
        print(f"Relationships: {validation['total_relationships']}")
        print(f"Total nodes: {validation['total_nodes']}")
        for item in validation["relationship_types"]:
            print(f"{item['type']}: {item['count']}")
        for name, count in validation["missing"].items():
            print(f"{name}: {count}")
        print(f"Versions with dependencies: {validation['versions_with_dependencies']}")
        print(f"Dependency analysis paths: {validation['analysis_paths']}")
        print(f"Shared dependency packages: {validation['shared_dependency_packages']}")
        print("Dependencies per version:")
        for item in validation["dependencies_per_version"]:
            print(f"  {item['version_id']}: {item['dependency_count']}")
        print(f"Versions with zero dependencies: {validation['zero_dependency_versions']}")
        print(f"Self-dependencies: {validation['self_dependencies']}")
        print(f"Suspicious duplicate mappings: {validation['duplicate_mappings']}")
        print(f"Dangling dependency references: {validation['dangling_references']}")
    except Exception as error:
        raise SystemExit(f"Seed failed: {type(error).__name__}") from None
    finally:
        driver.close()


if __name__ == "__main__":
    main()