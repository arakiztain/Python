print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")
with open('classified_data.txt', 'r') as file:
    print("Vault connection established wth failsafe protocols\n")

    print("SECURE EXTRACTION:")
    data = file.read()

    new_text = data.replace("[", "{[}").replace("]", "{]}")

    print(new_text)

with open('security_protocols.txt') as file:
    data = file.read()

    new_text = data.replace("[", "{[}").replace("]", "{]}")
    print("\nSECURE PRESERVATION:")
    print(new_text)

print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
    