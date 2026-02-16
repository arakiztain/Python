def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """
    Combine two spells into a single spell that returns both results.
    """
    if not callable(spell1) or not callable(spell2):
        return lambda *args, **kwargs: ("Invalid spell", "Invalid spell")

    def combined(*args, **kwargs):
        return spell1(*args, **kwargs), spell2(*args, **kwargs)

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    Amplify the result of a spell by a multiplier.
    """
    if not callable(base_spell) or not isinstance(multiplier, int):
        return lambda *args, **kwargs: 0

    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    Cast a spell only if condition evaluates to True.
    """
    if not callable(condition) or not callable(spell):
        return lambda *args, **kwargs: "Spell fizzled"

    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[callable]) -> callable:
    """
    Execute a sequence of spells and return their results as a list.
    """
    if not spells or not all(callable(spell) for spell in spells):
        return lambda *args, **kwargs: []

    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]

    return sequence


# ======================================================
# Example spells for testing output
# ======================================================


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def fireball_power(power: int) -> int:
    return power


def has_mana(mana: int) -> bool:
    return mana >= 10


def fireball_mana(mana: int) -> int:
    return mana - 10


def spell1() -> str:
    return "Spell 1"


def spell2() -> str:
    return "Spell 2"


def spell3() -> str:
    return "Spell 3"


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print()
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball_power, 3)
    power = 10
    print(f"Original: {power}, Amplified: {mega_fireball(power)}")

    print()
    print("Testing conditional caster...")
    cast = conditional_caster(has_mana, fireball_mana)
    print(cast(15))
    print(cast(5))

    print()
    print("Testing spell sequence...")
    combo = spell_sequence([spell1, spell2, spell3])
    print(combo())


if __name__ == "__main__":
    main()
