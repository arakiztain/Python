print("=== Achievement Tracker System ===\n")

alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {
    'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
    'perfectionist'
}

print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===")
all_achievements = alice | bob | charlie
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}")

print(f"\nCommon to all players: {alice & bob & charlie}")
unique_only = {
    ach for ach in all_achievements
    if (ach in alice) + (ach in bob) + (ach in charlie) == 1
}

print(unique_only)
print(f"Rare achievements (1 player): {unique_only}")

print(f"\nAlice vs Bob common: {alice & bob}")
print(f"Alice unique: {alice - bob}")
print(f"Bob unique: {bob - alice}")
