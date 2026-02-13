#!/usr/bin/env python3

import sys
import os
import importlib
from typing import Dict, Tuple, Optional

os.environ["MPLCONFIGDIR"] = "/tmp"

PackageStatus = Dict[str, Tuple[str, Optional[str]]]

REQUIRED_PACKAGES = ["pandas", "requests", "matplotlib"]


def detect_environment() -> str:
    """
    Detect the execution environment (Poetry, virtualenv/pip, or system).
    """
    poetry_env = os.getenv("VIRTUAL_ENV") and ".venv" in os.getenv(
        "VIRTUAL_ENV"
        )
    if poetry_env:
        return "Poetry environment detected"

    if hasattr(sys, 'real_prefix') or sys.prefix != sys.base_prefix:
        return "Virtual environment (pip) detected"

    return "System Python (global environment)"


def check_packages() -> PackageStatus:
    """
    Check required dependencies and return their installation status.

    Returns:
        Dictionary mapping package name to a tuple:
        (status, version).
    """
    status: PackageStatus = {}

    for pkg in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(pkg)
            version: Optional[str] = getattr(module, "__version__", "unknown")
            status[pkg] = ("OK", version)
        except ImportError:
            status[pkg] = ("MISSING", None)

    return status


def print_dependency_status(status: PackageStatus) -> None:
    """
    Print dependency status and exit if missing packages are detected.
    """
    print("Checking dependencies:")
    missing = []

    for pkg, (state, version) in status.items():
        if state == "OK":
            print(f"[OK] {pkg} ({version}) - Ready")
        else:
            print(f"[MISSING] {pkg} - Not installed")
            missing.append(pkg)

    if missing:
        print()
        print("Missing dependencies detected:", ", ".join(missing))
        print("Install them using:")
        print("  pip: pip install -r requirements.txt")
        print("  Poetry: poetry install")
        sys.exit(1)


def compare_versions(status: PackageStatus) -> None:
    """
    Display installed package versions.
    """
    print()
    print("Package version summary:")
    for pkg, (state, version) in status.items():
        if state == "OK":
            print(f" - {pkg}: {version}")


def fetch_matrix_data() -> Optional[dict]:
    """
    Fetch simulated Matrix data from a remote API using requests.

    Returns:
        JSON response as dictionary if successful,
        otherwise None.
    """
    import requests

    print("\nFetching Matrix data from remote source...")
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/todos/1",
            timeout=5
        )
        response.raise_for_status()
        print("Network access confirmed.")
        return response.json()
    except Exception:
        print("Remote fetch failed. Switching to local data.")
        return None


def run_analysis() -> None:
    """
    Perform data analysis and generate a visualization.
    """
    import pandas as pd
    import matplotlib.pyplot as plt

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    data = {
        "Agent": ["Smith", "Brown", "Jones", "Neo", "Trinity"],
        "Level": [95, 80, 70, 100, 85],
        "Status": ["active", "active", "inactive", "active", "active"]
    }

    df = pd.DataFrame(data)
    df_active = df[df["Status"] == "active"]

    plt.figure()
    plt.bar(df_active["Agent"], df_active["Level"])
    plt.title("Active Agents in the Matrix")
    plt.xlabel("Agent")
    plt.ylabel("Level")

    print("Generating visualization...")
    plt.savefig("matrix_analysis.png")

    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """
    Main execution function.
    """
    print("LOADING STATUS: Loading programs...")
    print()
    print("Environment:", detect_environment())
    print()

    status = check_packages()
    print_dependency_status(status)
    compare_versions(status)

    fetch_matrix_data()
    run_analysis()


if __name__ == "__main__":
    main()
