import random
from typing import List, Dict
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        # del obj[i] by index | list.remove(value) by value
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                del self.cards[i]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck")
        return self.cards.pop(0)

    def get_deck_info(self) -> Dict:
        total = len(self.cards)
        stats = {
            "total_cards": total,
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0.0
        }

        if total == 0:
            return stats

        total_cost = 0

        for card in self.cards:
            class_name = card.__class__.__name__
            if "Creature" in class_name:
                stats["creatures"] += 1
            elif "Spell" in class_name:
                stats["spells"] += 1
            elif "Artifact" in class_name:
                stats["artifacts"] += 1

        total_cost += card.cost

        stats["avg_cost"] = round(total_cost / total, 2)
        return stats
