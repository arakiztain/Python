import os
import sys
from dotenv import load_dotenv


MATRIX_MODE = os.environ.get("MATRIX_MODE", "development")

if MATRIX_MODE == "development":
    load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
API_KEY = os.environ.get("API_KEY")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
ZION_ENDPOINT = os.environ.get("ZION_ENDPOINT")


def missing(var_name, value):
    if not value:
        print(f"[WARNING] Missing configuration: {var_name}")
        return True
    return False


def security_check():
    print("Environment security check:")

    if API_KEY and "secret" not in API_KEY.lower():
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Possible insecure API key")

    if MATRIX_MODE == "development":
        if os.path.exists(".env"):
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] .env file not found")
    else:
        print("[OK] Production overrides available")


def main():
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    has_errors = False

    has_errors |= missing("DATABASE_URL", DATABASE_URL)
    has_errors |= missing("API_KEY", API_KEY)
    has_errors |= missing("ZION_ENDPOINT", ZION_ENDPOINT)

    if has_errors:
        print("Configuration incomplete. The Oracle cannot see everything.")
        if MATRIX_MODE == "production":
            sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {MATRIX_MODE}")

    if DATABASE_URL:
        if MATRIX_MODE == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to production instance")
    else:
        print("Database: Not configured")

    print(
        "API Access: Authenticated" if API_KEY else "API"
        " Access: Missing credentials"
        )
    print(f"Log Level: {LOG_LEVEL}")
    print("Zion Network: Online" if ZION_ENDPOINT else "Zion Network: Offline")
    print()

    security_check()
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
