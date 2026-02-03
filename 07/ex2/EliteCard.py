from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, List


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int
    ) -> None:

        super().__init__(name, cost, rarity)
        self.attack_power: int = attack_power
        self.defense: int = defense
        self.total_mana = 0

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite Card enters the battlefield"
        }

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_attack: int) -> Dict:
        blocked = min(self.defense, incoming_attack)
        damage_taken = incoming_attack - blocked
        still_alive = damage_taken < self.defense
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": still_alive
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack_power": self.attack_power,
            "defense": self.defense
        }

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        mana_used = len(targets)
        self.total_mana -= mana_used
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> Dict:
        self.total_mana += amount
        return {
            "channeled": amount,
            "total_mana": self.total_mana
        }

    def get_magic_stats(self) -> Dict:
        return {
            "total_mana": self.total_mana
        }
