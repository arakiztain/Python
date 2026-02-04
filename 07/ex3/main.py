from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print()
    print("=== DataDeck Game Engine ===")
    print()

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory=factory, strategy=strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print("Available types:", factory.get_supported_types())
    print()

    print("Simulating aggressive turn...")
    print("Hand:", [f"{c.name} ({c.cost})" for c in engine.hand])
    print()

    turn_result = engine.simulate_turn()
    print("Turn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", turn_result)
    print()

    report = {
        'turns_simulated': 1,
        'strategy_used': strategy.get_strategy_name(),
        'total_damage': turn_result['damage_dealt'],
        'cards_created': len(engine.hand)
    }
    print("Game Report:", report)
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
