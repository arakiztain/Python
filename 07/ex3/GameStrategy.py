from abc import ABC, abstractmethod
from typing import List, Dict


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        ...

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        ...
