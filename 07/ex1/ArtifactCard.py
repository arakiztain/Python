from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
     ) -> None:

        super().__init__(name, cost, rarity)

        if durability <= 0:
            raise ValueError("Durability must be a positive integer")

        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> Dict:
        self.durability -= 1

        return {
            "artifact": self.name,
            "effect": self.effect,
            "remaining_durability": self.durability,
            "active": self.durability > 0
        }
