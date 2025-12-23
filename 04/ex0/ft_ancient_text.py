print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
with open('ancient_fragment.txt', 'r') as file:
    data = file.read()
print(f"Accessing Storage Vault: {file.name}")
print("Connection established...\n")

texto_original = data

texto_formateado = texto_original.replace("[", "{[}").replace("]", "{]}")

print(texto_formateado)
file.close()
print("\nData recovery complete. Storage unit disconnected.")
