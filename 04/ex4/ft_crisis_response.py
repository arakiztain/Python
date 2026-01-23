"""
ft_crisis_response.py

A crisis response system for the Cyber Archives.
Attempts to access multiple archive files, handling exceptions
gracefully to simulate different crisis scenarios (lost files,
security restrictions, and routine access). Ensures safe file
operations using 'with' statements.
"""

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

archives_to_access = [
    "lost_archive.txt",
    "classified_vault.txt",
    "standard_archive.txt"
]

for archive in archives_to_access:
    print(f"CRISIS ALERT: Attempting access to '{archive}'...")
    try:
        with open(archive, "r") as vault:
            content = vault.read().strip()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    else:
        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed\n")

print("All crisis scenarios handled successfully. Archives secure.")
