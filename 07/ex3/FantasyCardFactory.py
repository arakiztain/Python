from typing import Dict
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creature_types = ['dragon', 'goblin']
        self.spell_types = ['fireball']
        self.artifact_types = ['mana_ring']

    def create_creature(self, name_or_power) -> CreatureCard:
        return CreatureCard(
            name=name_or_power.title(),
            cost=5,
            rarity="Epic",
            attack=5,
            health=5
        )

    def create_spell(self, name_or_effect) -> SpellCard:
        return SpellCard(
            name=name_or_effect.title(),
            cost=3,
            rarity="Rare",
            effect_type="damage"
        )

    def create_artifact(self, name_or_ability) -> ArtifactCard:
        return ArtifactCard(
            name=name_or_ability.title(),
            cost=4,
            rarity="Legendary",
            durability=3,
            effect="Permanent: +1 mana per turn"
        )

    def create_themed_deck(self, size: int) -> Dict:
        deck = {
            'hand': [
                self.create_creature("Fire Dragon"),
                self.create_creature("Goblin Warrior"),
                self.create_artifact("Lightning Bolt")
            ]
        }
        return deck

    def get_supported_types(self) -> Dict:
        return {
            'creatures': self.creature_types,
            'spells': self.spell_types,
            'artifacts': self.artifact_types
        }
