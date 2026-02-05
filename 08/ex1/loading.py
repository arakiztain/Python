import sys
import os

os.environ['MPLCONFIGDIR'] = '~/sgoinfre/'

def check_packages():
    """Verifica si los paquetes necesarios están instalados y devuelve dict con estado."""
    status = {}
    try:
        import pandas as pd
        status['pandas'] = ('OK', pd.__version__, "Data manipulation ready")
    except ImportError:
        status['pandas'] = ('MISSING', None, "Data manipulation not available")
    try:
        import requests
        status['requests'] = ('OK', requests.__version__, "Network access ready")
    except ImportError:
        status['requests'] = ('MISSING', None, "Network access not available")
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        status['matplotlib'] = ('OK', matplotlib.__version__, "Visualization ready")
    except ImportError:
        status['matplotlib'] = ('MISSING', None, "Visualization not available")
    return status

def print_dependency_status(status):
    """Muestra mensajes de dependencia al estilo esperado"""
    print("Checking dependencies:")
    missing = []
    for pkg, (state, version, msg) in status.items():
        if state == "OK":
            print(f"[OK] {pkg} ({version}) - {msg}")
        else:
            print(f"[MISSING] {pkg} - {msg}")
            missing.append(pkg)
    if missing:
        print()
        print("Missing dependencies detected:", ", ".join(missing))
        print("Install them using:")
        print("  pip: pip install -r requirements.txt")
        print("  Poetry: poetry install")
        sys.exit(1)

def run_analysis():
    """Simula análisis de datos y genera visualización"""
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
    plt.bar(df_active["Agent"], df_active["Level"], color="green")
    plt.title("Active Agents in the Matrix")
    plt.ylabel("Level")
    plt.xlabel("Agent")
    print("Generating visualization...")
    plt.show()

    print()
    print("Analysis complete!")
    print("Results saved to:", os.environ['MPLCONFIGDIR'])

def main():
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    status = check_packages()
    print_dependency_status(status)
    run_analysis()

if __name__ == "__main__":
    main()
