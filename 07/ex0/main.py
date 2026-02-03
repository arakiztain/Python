from CreatureCard import CreatureCard

class DummyTarget:
	def __init__(self, name: str) -> None:
		self.name: str = name


def main() -> None:
	print()
	print("=== DataDeck Card Foundatuion ===")
	print()

	print("Testing Abstract Base Class Design:")
	print()

	fire_dragone = CreatureCard(
		name="Fire Dragon",
		cost=5,
		rarity="Epic",
		attack=7,
		health=5
	)
	print("CreatureCard Info:")
	print(fire_dragone.get_card_info())
	print()

	available_mana = 6
	print(f"Playing {fire_dragone.name} with {available_mana} mana available:")
	print(f"Playable: {fire_dragone.is_playable(available_mana)}")
	if fire_dragone.is_playable(available_mana):
		play_result = fire_dragone.play(game_state={})
		print("Play Result:", play_result)
	print()

	goblin = DummyTarget(name="Goblin Warrior")
	print(f"{fire_dragone.name} attacks {goblin.name}:")
	print(f"Attack Result:", fire_dragone.attack_target(goblin))
	print()

	low_mana = 3
	print(f"Testing insufficient mana ({low_mana} available):")
	print(f"Playable: {fire_dragone.is_playable(low_mana)}")

	print()
	print("Abstract pattern succesfully demonstrated!")


if __name__ == "__main__":
	main()