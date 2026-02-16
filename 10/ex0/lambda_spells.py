def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Sort magical artifacts by power level in descending order.

    Args:
        artifacts: List of artifact dictionaries containing
                   'name', 'power', and 'type'.

    Returns:
        A sorted list of artifacts by descending power.
        Returns an empty list if input is invalid.
    """
    if not artifacts:
        return []

    try:
        return sorted(
            artifacts,
            key=lambda artifact: artifact["power"],
            reverse=True
        )
    except (KeyError, TypeError):
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    Filter mages whose power is greater than or equal to min_power.

    Args:
        mages: List of mage dictionaries containing
               'name', 'power', and 'element'.
        min_power: Minimum power threshold.

    Returns:
        A list of mages meeting the minimum power requirement.
        Returns an empty list if input is invalid.
    """
    if not mages:
        return []

    try:
        return list(
            filter(
                lambda mage: mage["power"] >= min_power,
                mages
            )
        )
    except (KeyError, TypeError):
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transform spell names by adding decorative prefixes and suffixes.

    Args:
        spells: List of spell names.

    Returns:
        A list of transformed spell names.
        Returns an empty list if input is invalid.
    """
    if not spells:
        return []

    try:
        return list(
            map(
                lambda spell: f"* {spell} *",
                spells
            )
        )
    except TypeError:
        return []


def mage_stats(mages: list[dict]) -> dict:
    """
    Calculate power statistics for a list of mages.

    Args:
        mages: List of mage dictionaries containing 'power'.

    Returns:
        A dictionary with:
            - 'max_power': Highest power level
            - 'min_power': Lowest power level
            - 'avg_power': Average power (rounded to 2 decimals)
        Returns zeros if input is empty or invalid.
    """
    if not mages:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0.0
        }

    try:
        max_power = max(
            mages,
            key=lambda mage: mage["power"]
        )["power"]

        min_power = min(
            mages,
            key=lambda mage: mage["power"]
        )["power"]

        total_power = sum(
            map(lambda mage: mage["power"], mages)
        )

        avg_power = round(total_power / len(mages), 2)

        return {
            "max_power": max_power,
            "min_power": min_power,
            "avg_power": avg_power
        }

    except (KeyError, TypeError, ZeroDivisionError):
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0.0
        }


def main() -> None:
    """Run example tests for lambda spell functions."""
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
    ]

    mages = [
        {"name": "Rowan", "power": 59, "element": "fire"},
        {"name": "Riley", "power": 52, "element": "lightning"},
        {"name": "Riley", "power": 86, "element": "shadow"},
        {"name": "Ember", "power": 86, "element": "ice"},
        {"name": "Rowan", "power": 68, "element": "water"}
    ]

    spells = ["fireball", "heal", "shield"]

    print()
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for i in range(len(sorted_artifacts) - 1):
        print(
            f"{sorted_artifacts[i]['name']} "
            f"({sorted_artifacts[i]['power']} power) comes before "
            f"{sorted_artifacts[i + 1]['name']} "
            f"({sorted_artifacts[i + 1]['power']} power)"
        )

    print()
    print("Testing power filter...")
    filtered_mages = power_filter(mages, 80)
    if filtered_mages:
        print("Mages with power >= 80:")
        for mage in filtered_mages:
            print(
                f"- {mage['name']} ({mage['element']} element) "
                f"with {mage['power']} power"
            )
    else:
        print("No mages found with power >= 80")

    print()
    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    print()
    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(
        f"Maximum power: {stats['max_power']}\n"
        f"Minimum power: {stats['min_power']}\n"
        f"Average power: {stats['avg_power']:.2f}"
    )


if __name__ == "__main__":
    main()
