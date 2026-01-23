"""
Achievement Inventory System.

This script manages a game inventory using nested dictionaries.
It displays player inventories, processes transactions, and
performs inventory analytics.
"""


def ft_inventory_system():
    """
    Runs inventory display, updates, and analytics.
    """
    print("=== Achievement Inventory System ===")
    print("\n=== Alice's Inventory ===")

    inventory = {
        'players': {
            'alice': {
                'items': {
                    'pixel_sword': 1, 'code_bow': 1,
                    'health_byte': 1, 'quantum_ring': 3
                },
                'total_value': 1875,
                'item_count': 6
            },
            'bob': {
                'items': {
                    'code_bow': 3, 'pixel_sword': 2
                },
                'total_value': 900,
                'item_count': 5
            },
            'charlie': {
                'items': {
                    'pixel_sword': 1, 'code_bow': 1
                },
                'total_value': 350,
                'item_count': 2
            },
            'diana': {
                'items': {
                    'code_bow': 3, 'pixel_sword': 3,
                    'health_byte': 3, 'data_crystal': 3
                },
                'total_value': 4125,
                'item_count': 12
            }
        },
        'catalog': {
            'pixel_sword': {
                'type': 'weapon', 'value': 150, 'rarity': 'common'
            },
            'quantum_ring': {
                'type': 'accessory', 'value': 500, 'rarity': 'rare'
            },
            'health_byte': {
                'type': 'consumable', 'value': 25, 'rarity': 'common'
            },
            'data_crystal': {
                'type': 'material', 'value': 1000, 'rarity': 'legendary'
            },
            'code_bow': {
                'type': 'weapon', 'value': 200, 'rarity': 'uncommon'
            }
        }
    }

    players = inventory["players"]
    catalog = inventory["catalog"]

    alice_items = players["alice"]["items"]
    bob_items = players["bob"]["items"]

    for item, qty in alice_items.items():
        item_info = catalog[item]
        value = qty * item_info["value"]
        print(
            f"{item} ({item_info['type']}, {item_info['rarity']}): "
            f"{qty}x @ {item_info['value']} gold each = {value} gold"
        )

    print(f"\nInventory value: {players['alice']['total_value']} gold")
    print(f"Item count: {players['alice']['item_count']}")

    categories = {}
    for item_name, qty in alice_items.items():
        item_type = catalog[item_name]["type"]
        categories[item_type] = categories.get(item_type, 0) + qty

    output = ", ".join(f"{t}({c})" for t, c in categories.items())
    print(f"Categories: {output}")

    print("\n=== Transaction: alice gives Bob 2 quantum rings ===")
    alice_items["quantum_ring"] = 1
    bob_items["quantum_ring"] = 2

    players["alice"]["total_value"] = 875
    players["bob"]["total_value"] = 1900
    players["alice"]["item_count"] = 4
    players["bob"]["item_count"] = 7

    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    print(f"Alice quantum rings: {alice_items['quantum_ring']}")
    print(f"Bob quantum rings: {bob_items['quantum_ring']}")

    print("\n=== Inventory Analytics ===")

    most_valuable = max(players.items(), key=lambda p: p[1]["total_value"])
    print(
        f"Most valuable player: {most_valuable[0]} "
        f"({most_valuable[1]['total_value']} gold)"
    )

    most_items = max(players.items(), key=lambda p: p[1]["item_count"])
    print(
        f"Most items: {most_items[0]} "
        f"({most_items[1]['item_count']} items)"
    )

    rare_items = {
        name for name, info in catalog.items()
        if info["rarity"] == "rare"
    }

    rare_found = {
        item
        for item in rare_items
        for pdata in players.values()
        if item in pdata["items"]
    }

    print("Rarest items:", ", ".join(rare_found))


if __name__ == "__main__":
    ft_inventory_system()
