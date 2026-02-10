def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return result1, result2
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplification(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplification


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        result = []
        for spell in spells:
            result.append(spell(*args, **kwargs))
        return result
    return sequence


# =======================================================


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
    print()
    print("Testing spell combiner...")
    spell_comb = spell_combiner(fireball, heal)
    result = spell_comb("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print()
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball_power, 3)
    power = 10
    print(f"Original: {power}, Amplified: {mega_fireball(10)}")

    print()
    print("Testing conditional caster...")
    cast_fireball = conditional_caster(has_mana, fireball_mana)
    print(cast_fireball(15))
    print(cast_fireball(5))

    print()
    print("Teesting spell sequence...")
    combo = spell_sequence([spell1, spell2, spell3])
    print(combo())


if __name__ == "__main__":
    main()
