from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    lead = lead_to_gold()
    healing = healing_potion()
    return f"Philosopher's Stone created by combining: {lead} and {healing}"


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
