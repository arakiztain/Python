"""
Achievement Tracker System.

This script tracks player achievements using sets and performs
basic analytics such as unions, intersections, and unique achievements.
"""


def ft_achievement_tracker():
    """
    Displays player achievements and performs set-based analytics.
    """
    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_achievements = alice | bob | charlie
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all = alice & bob & charlie
    print(f"\nCommon to all players: {common_all}")

    rare_achievements = {
        ach for ach in all_achievements
        if (ach in alice) + (ach in bob) + (ach in charlie) == 1
    }
    print(f"Rare achievements (1 player): {rare_achievements}")

    print(f"\nAlice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    ft_achievement_tracker()
