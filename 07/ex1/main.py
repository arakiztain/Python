from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print()
    print("=== DataDeck Deck Builder ===")
    print()

    print("Building deck with different card types...")
    deck = Deck()

    deck.add_card(
        CreatureCard(
            name="Fire Dragon",
            cost=4,
            rarity="Legendary",
            attack=7,
            health=5
        )
    )

    deck.add_card(
        SpellCard(
            name="Lightning Bolt",
            cost=5,
            rarity="Common",
            effect_type="damage"
        )
    )

    deck.add_card(
        ArtifactCard(
            name="Mana Crystal",
            cost=3,
            rarity="Rare",
            durability=3,
            effect="+1 mana per turn"
        )
    )

    print("Deck stats:", deck.get_deck_stats())
    print()

    print("Drawing and playing cards:")
    print()
    deck.shuffle()
    while True:
        try:
            card = deck.draw_card()
            card_type = card.__class__.__name__.replace("Card", "")
            print(f"Drew: {card.name} ({card_type})")
            print("Play Result:", card.play(game_state={}))
            print()
        except IndexError:
            break

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
