from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
            self,
            card_id: str,
            name: str,
            cost: int,
            rarity: str,
            attack_power: int,
            defense: int
            ) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.attack_power = attack_power
        self.defense = defense
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament Card enters the battlefield"
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

    def calculate_rating(self) -> int:
        self.rating = 1200 + 16 * self.wins - 16 * self.losses
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> Dict:
        return {
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> Dict:
        return {
            "card_id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
