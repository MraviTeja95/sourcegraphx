import os
from pathlib import Path

from dotenv import load_dotenv
from neo4j import Driver, GraphDatabase


load_dotenv(Path(__file__).resolve().parents[2] / ".env")


def _required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


_uri = _required_setting("COGNODB_URI")
_username = _required_setting("COGNODB_USERNAME")
_password = _required_setting("COGNODB_PASSWORD")

driver: Driver = GraphDatabase.driver(_uri, auth=(_username, _password))


def verify_connection() -> None:
    with driver.session() as session:
        record = session.run("RETURN 1 AS connected").single()
        if record is None or record["connected"] != 1:
            raise RuntimeError("CognoDB connection verification returned an unexpected result")