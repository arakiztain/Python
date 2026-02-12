import sys
import os
import site


def is_virtual_environment():
    """
    Detect if the script is running inside a virtual environment.

    Logic:
    - In a virtual environment, sys.prefix is different from sys.base_prefix.
    - In a global environment, both values are the same.
    """
    try:
        return sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    except Exception as error:
        print(f"Error detecting virtual environment: {error}")
        return False


def get_site_packages_path():
    """
    Safely retrieve the site-packages installation path.
    """
    try:
        paths = site.getsitepackages()
        if paths:
            return paths[0]
        return "Unable to determine site-packages path."
    except Exception as error:
        return f"Error retrieving site-packages path: {error}"


def main():
    print()

    try:
        if not is_virtual_environment():
            print("MATRIX STATUS: You're still plugged in")
            print()
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected")
            print()
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print()
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate  # On Unix")
            print("matrix_env\nScripts\nactivate    # On Windows")
            print()
            print("Then run this program again.")

        else:
            print("MATRIX STATUS: Welcome to the construct")
            print()
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}")
            print()
            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")
            print()
            print("Package installation path:")
            print(get_site_packages_path())

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
