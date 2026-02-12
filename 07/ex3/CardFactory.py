from abc import ABC, abstractmethod
from typing import Dict
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power) -> CreatureCard:
        ...

    @abstractmethod
    def create_spell(self, name_or_effect) -> SpellCard:
        ...

    @abstractmethod
    def create_artifact(self, name_or_ability) -> ArtifactCard:
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        ...

    @abstractmethod
    def get_supported_types(self) -> Dict:
        ...
