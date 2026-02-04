from typing import List, Dict
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        cards_played = []
        mana_used = 0
        targets_attacked = ['Enemy Player']
        damage_dealt = 0

        for card in sorted(hand, key=lambda c: c.cost):
            if hasattr(card, 'attack'):
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += getattr(card, 'attack', 0)

            elif hasattr(card, 'effect_type'):
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += 3

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        return sorted(available_targets, reverse=True)
