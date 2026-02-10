def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda m: m["power"])["power"],
        'min_power': min(mages, key=lambda m: m["power"])["power"],
        'avg_power': round(sum(m["power"] for m in mages) / len(mages), 2)
    }


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
    ]

    mages = [
        {'name': 'Rowan', 'power': 59, 'element': 'fire'},
        {'name': 'Riley', 'power': 52, 'element': 'lightning'},
        {'name': 'Riley', 'power': 86, 'element': 'shadow'},
        {'name': 'Ember', 'power': 86, 'element': 'ice'},
        {'name': 'Rowan', 'power': 68, 'element': 'water'}
    ]

    spells = ["fireball", "heal", "shield"]

    print()
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for i in range(len(sorted_artifacts) - 1):
        print(
            f"{sorted_artifacts[i]['name']} ({sorted_artifacts[i]['power']} "
            f"power) comes before {sorted_artifacts[i+1]['name']} "
            f"({sorted_artifacts[i+1]['power']} power)"
            )

    print()
    print("Testing power filter...")
    filtered_mages = power_filter(mages, 80)
    if filtered_mages:
        print("Mages with power >= 80:")
        for mage in filtered_mages:
            print(
                f"- {mage['name']} ({mage['element']} element) with"
                f" {mage['power']} power")

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
