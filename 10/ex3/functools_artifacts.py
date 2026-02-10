from functools import reduce, partial
from operator import add, mul
from typing import List


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
	...


def memoized_fibonacci(n: int) -> int:
	...


def spell_dispatcher() -> callable:
	...


def main() -> None:
	print()
	print("Testing spell reducer...")
	spells = [10, 20, 40, 30]
	operators = ["Sum", "Product", "Max"]
	print("\n".join(f"{op}: {spell_reducer(spells, op)}" for op in operators))

	print()
	print("Testing partial enchanter...")

if __name__ == "__main__":
	main()