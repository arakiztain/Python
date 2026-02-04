from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print()
    print("=== DataDeck Tournament Platform ===")
    print()

    platform = TournamentPlatform()
    print("Registering Tournament Cards...")
    print()

    card1 = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary", 7, 5)
    card2 = TournamentCard("wizard_001", "Ice Wizard", 4, "Epic", 5, 3)

    platform.register_card(card1)
    platform.register_card(card2)

    for card in [card1, card2]:
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")
        print()

    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", match_result)

    print()
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for idx, entry in enumerate(leaderboard, start=1):
        print(
            f"{idx}. {entry['name']} - Rating: "
            f"{entry['rating']} ({entry['record']})"
            )

    report = platform.generate_tournament_report()
    print()
    print("Platform Report:")
    print(report)

    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
