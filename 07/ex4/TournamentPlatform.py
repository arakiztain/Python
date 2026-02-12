from typing import Dict, List
from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform:
    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        c1 = self.cards.get(card1_id)
        c2 = self.cards.get(card2_id)

        if not c1 or not c2:
            raise ValueError("Card ID no registrado en la plataforma")

        score1 = c1.attack_power + c1.rating + random.randint(0, 10)
        score2 = c2.attack_power + c2.rating + random.randint(0, 10)

        if score1 >= score2:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List[Dict]:
        sorted_cards = sorted(
            self.cards.values(),
            key=lambda x: x.rating,
            reverse=True
            )
        leaderboard = []
        for card in sorted_cards:
            leaderboard.append({
                "name": card.name,
                "rating": card.rating,
                "record": f"{card.wins}-{card.losses}"
            })
        return leaderboard

    def generate_tournament_report(self) -> Dict:
        total_cards = len(self.cards)
        avg_rating = sum(
            card.rating for card in self.cards.values()
            ) / total_cards if total_cards else 0
        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": int(avg_rating),
            "platform_status": "active"
        }
