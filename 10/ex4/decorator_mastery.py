from functools import wraps
import time
from typing import Any
import random


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.6f} seconds")
        return result
    return wrapper


def power_validator(min_power: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(args[0], int):
                power = args[0]
            else:
                power = args[-1]
            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Decorator factory to retry failed spells."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... (attempt {attempt}/"
                            f"{max_attempts})"
                            )
                    else:
                        return (
                            f"Spell casting failed after {max_attempts}"
                            " attempts"
                            )
        return wrapper
    return decorator


class MageGuild:
    def __init__(self, mage_name: str):
        if not self.validate_mage_name(mage_name):
            raise ValueError("Invalid mage name")
        self.mage_name = mage_name

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# =================================================================


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


@power_validator(10)
def fireball_power(power: int) -> str:
    return f"Fireball power {power}"


@retry_spell(5)
def unstable_fireball():
    """Hechizo que falla aleatoriamente"""
    if random.random() < 0.7:
        raise ValueError("Oops, spell fizzled")
    return "Fireball cast successfully!"


def main() -> None:
    print()
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print()
    print("Testing power validator...")
    print(f"Result: {fireball_power(20)}")
    print(f"Result: {fireball_power(9)}")

    print()
    print("Testing retry spell...")
    print(unstable_fireball())

    print()
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    mage = MageGuild("Merlin")
    print(mage.cast_spell("Fireball", 20))
    print(mage.cast_spell("Ice Shard", 5))


if __name__ == "__main__":
    main()
