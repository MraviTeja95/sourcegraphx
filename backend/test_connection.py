from app.db.connection import driver, verify_connection


try:
    verify_connection()
except Exception as error:
    raise SystemExit(f"CognoDB connection failed: {type(error).__name__}") from error
finally:
    driver.close()

print("CognoDB connection successful!")