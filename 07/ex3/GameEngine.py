from typing import List, Dict
from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy
            ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = factory.create_themed_deck(size=3)['hand']
        self.battlefield: List = []

    def simulate_turn(self) -> Dict:
        turn_result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.battlefield.extend(turn_result['cards_played'])
        return turn_result

    def get_engine_status(self) -> Dict:
        return {
            'factory': type(self.factory).__name__,
            'strategy': self.strategy.get_strategy_name(),
            'hand_size': len(self.hand),
            'battlefield_size': len(self.battlefield)
        }
