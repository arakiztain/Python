print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")


file = open("new_discovery.txt", "w")
print(f"Initializing new storage unit: {file.name}")

print("Storage unit created successfully...\n")
print("Inscribing preservation data...")

line1 = "{[}ENTRY 001{]} New quantum algorithm discovered"
line2 = "{[}ENTRY 002{]} Efficiency increased by 347 %"
line3 = "{[}ENTRY 003{]} Archived by Data Archivist trainee"

file.write(line1 + "\n")
file.write(line2 + "\n")
file.write(line3 + "\n")

print(line1)
print(line2)
print(line3)


file.close()

print("\nData inscription complete. Storage unit sealed.")
print(f"Archive '{file.name}' ready for long-term preservation.")
