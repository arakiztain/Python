import sys
import site
import os


def virtual_environment():
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


print()
if not virtual_environment():
    print("MATRIX STATUS: You're still plugged in")
    print()
    print("Current Python: " + sys.executable)
    print("Virtual environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machine can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate     # On Windows")
    print()
    print("Then run this program again")

else:
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print("Current Python: " + sys.executable)
    print("Virtual environment: " + os.path.basename(sys.prefix))
    print("Environment path: " + sys.prefix)
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()

    print("Package installation path:")
    print(site.getsitepackages()[0])
