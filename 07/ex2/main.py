from ex2.EliteCard import EliteCard


def main() -> None:
    print()
    print("=== DataDeck Ability System ===")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Legendary",
        attack_power=5,
        defense=3
    )

    print()
    print("EliteCard capabilities:")
    print("- Card:", [func for func in dir(EliteCard) if func in [
        'play', 'get_card_info', 'is_playable'
        ]])
    print("- Combatable:", [func for func in dir(EliteCard) if func in [
        'attack', 'defend', 'get_combat_stats'
        ]])
    print("- Magical:", [func for func in dir(EliteCard) if func in [
        'cast_spell', 'channel_mana', 'get_magic_stats'
        ]])
    print()

    print(f"Playing {elite.name} ({type(elite).__name__}):")
    print()

    print("Combat phase:")
    atack_result = elite.attack("Enemy")
    print("Attack Result:", atack_result)
    defend_result = elite.defend(incoming_attack=5)
    print("Defend Result:", defend_result)
    print()

    print("Magic phase:")
    spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", spell_result)
    mana_result = elite.channel_mana(amount=3)
    print("Mana channel:", mana_result)
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
