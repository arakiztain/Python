print("=== Achievement Inventory System ===")

print("\n=== Alice's Inventory ===")

inventory = {
    'players': {
        'alice': {
            'items': {
                'pixel_sword': 1, 'code_bow': 1, 'health_byte': 1,
                'quantum_ring': 3
            }, 'total_value': 1875, 'item_count': 6
        },
        'bob': {
            'items': {
                'code_bow': 3, 'pixel_sword': 2
            }, 'total_value': 900, 'item_count': 5
        },
        'charlie': {
            'items': {
                'pixel_sword': 1, 'code_bow': 1
            }, 'total_value': 350, 'item_count': 2
        },
        'diana': {
            'items': {
                'code_bow': 3, 'pixel_sword': 3, 'health_byte': 3,
                'data_crystal': 3
            }, 'total_value': 4125, 'item_count': 12
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

alice_items = inventory.get("players").get("alice").get("items")
bob_items = inventory.get("players").get("bob").get("items")
cat = inventory.get("catalog")
players = inventory.get("players")
for x in alice_items.keys():
    print(
        f"{x} ({cat.get(x).get('type')}, {cat.get(x).get('rarity')}): "
        f"{alice_items[x]}x @ {cat.get(x).get('value')} gold each = "
        f"{alice_items[x] * cat.get(x).get('value')} gold"
    )

print(
    f"\nInventory value: "
    f"{inventory.get('players').get('alice').get('total_value')} gold"
    )
print(f"Item count: {inventory.get('players').get('alice').get('item_count')}")
# categories
categories = {}

for name, item in cat.items():
    tipo = item["type"]
    if tipo in categories:
        categories[tipo] += 1
    else:
        categories[tipo] = 1


output = ", ".join(f"{tipo}({count})" for tipo, count in categories.items())
print(f"Categories: {output}")

print("\n=== Transaction: alice gives Bob 2 potions ===")
# update
alice_items.update({"quantum_ring": 1})
bob_items.update({"quantum_ring": 2})
inventory.get("players").get("alice").update({"total_value": 875})
inventory.get("players").get("bob").update({"total_value": 1900})
inventory.get("players").get("alice").update({"item_count": 4})
inventory.get("players").get("bob").update({"item_count": 7})
print("Transaction successful!")

print("\n=== Updated Inventories ===")
print(f"Alice quantum rings: {alice_items['quantum_ring']}")
print(f"Bob quantum rings: {bob_items['quantum_ring']}")

print("\n=== Inventory Analytics ===")
# max gold
max_player = None
max_value = -1
for player, item in inventory.get("players").items():
    if item["total_value"] > max_value:
        max_value = item["total_value"]
        max_player = player

print(f"Most valuable player: {max_player} ({max_value} gold)")
# max items
count_player = None
count_value = -1
for player, item in inventory.get("players").items():
    if item["item_count"] > count_value:
        count_value = item["item_count"]
        count_player = player

print(f"Most item: {count_player} ({count_value} items)")

# rarest
rare_list = [name for name, item in cat.items() if item["rarity"] == "rare"]

rarest_items_found = set()

for rare_item in rare_list:
    for player, pdata in players.items():
        if rare_item in pdata.get("items", {}):
            rarest_items_found.add(rare_item)

print("Rarest items:", ", ".join(rarest_items_found))
