from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        raise ValueError("Spells list cannot be empty")

    operations = {
        "Sum": add,
        "Product": mul,
        "Max": max,
        "Min": min
    }

    if operation not in operations:
        raise ValueError("Invalid operation")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(
            base_enchantment,
            power=50,
            element="lightning"
            )
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast(spell: Any):
        return f"Unknown spell type: {spell}"

    @cast.register
    def _(spell: int):
        return f"Damage spell hits for {spell} HP"

    @cast.register
    def _(spell: str):
        return f"Enchantment applied: {spell}"

    @cast.register
    def _(spell: list):
        results = [cast(s) for s in spell]
        return f"Multi-cast results: {results}"

    return cast


# =========================================================================


def base_enchantment(target: str, power: int, element: str) -> str:
    return f"{target} enchanted with {element} power {power}"


def main() -> None:
    print()
    print("Testing spell reducer...")
    spells = [10, 20, 40, 30]
    operators = ["Sum", "Product", "Max"]
    print("\n".join(f"{op}: {spell_reducer(spells, op)}" for op in operators))

    print()
    print("Testing partial enchanter...")
    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire_enchant"]("Sword"))
    print(enchants["ice_enchant"]("Shield"))
    print(enchants["lightning_enchant"]("Armor"))

    print()
    print("Testing memoized_fibonacci...")
    print("\n".join(f"Fib[{x}]: {memoized_fibonacci(x)}" for x in [10, 15]))

    print()
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(50))
    print(dispatcher("Flaming Sword"))
    print(dispatcher([10, "Ice Shield", 20]))


if __name__ == "__main__":
    main()
