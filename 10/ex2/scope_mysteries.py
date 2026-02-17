from typing import Any, Callable


def mage_counter() -> Callable:
    """
    Create a closure that counts how many times it is called.
    """
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """
    Create a closure that accumulates power over time.
    """
    total_power: int = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        try:
            total_power += amount
        except TypeError:
            return total_power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """
    Create an enchantment function for a specific type.
    """

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    """
    Create a memory vault with private storage using closure.
    """
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
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
        call = power_count(2)
        print(f"Call {i}: {call}")

    print()
    print("Testing enchantment factory...")
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
