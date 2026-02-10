from typing import Any


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
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, callable]:
    memory: dict = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


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
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Axe"))

    print()
    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("spell", "Fireball")
    vault["store"]("power", 42)
    print(vault["recall"]("spell"))
    print(vault["recall"]("power"))
    print(vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
