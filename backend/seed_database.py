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
    except Exception as error:
        raise SystemExit(f"Seed failed: {type(error).__name__}") from None
    finally:
        driver.close()


if __name__ == "__main__":
    main()