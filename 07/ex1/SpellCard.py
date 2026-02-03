from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str
    ) -> None:

        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self._describe_effect()
        }

    def resolve_effect(self, targets: List) -> Dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": len(targets),
            "resolved": True
        }

    def _describe_effect(self) -> str:
        effects = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to target",
            "buff": "Increase target stats",
            "debuff": "Reduce target stats"
        }
        return effects.get(self.effect_type, "Unknown magical effect")
