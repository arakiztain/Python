def mage_counter() -> callable:
    i: int = 0
    def counter():
        nonlocal i
        i += 1
        return i
    return counter


def spell_accumulator(initial_power: int) -> callable:
    power: int = initial_power
    def accumulator():
        nonlocal power
        power += 1
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    ...


def memory_vault() -> dict[str, callable]:
    ...



def main() -> None:
    print()
    print("Testing mage counter...")
    count = mage_counter()
    for i in range(1, 4):
        call = count()
        print(f"Call {i}: {call}")

    print()
    print("Testing spell accumulator...")
    power_count = spell_accumulator(2)
    for i in range(1, 4):
        call = power_count()
        print(f"Call {i}: {call}")

    print()
    print("Testing enchantment fatory...")

if __name__ == "__main__":
    main()