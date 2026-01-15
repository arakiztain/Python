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
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    else:
        print(f"SUCCESS: Archive recovered - ``{content}''")
    finally:
        if archive == "standard_archive.txt":
            print("STATUS: Normal operations resumed\n")
        else:
            print("STATUS: Crisis handled, system stable\n" if archive == "lost_archive.txt" else "STATUS: Crisis handled, security maintained\n")

print("All crisis scenarios handled successfully. Archives secure.")
