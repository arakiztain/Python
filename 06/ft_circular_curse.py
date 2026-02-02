from alchemy.grimoire import record_spell, validate_ingredients

print()
print("=== Circular Curse Breaking ===")
print()

print("Testing ingredient validation:")
print('validate_ingredients("fire air"):', validate_ingredients("fire air"))
print(
    'validate_ingredients("dragon_scales"):',
    validate_ingredients("dragon_scales")
)
print()

print("Testing spell recording with validation:")
print(
    'record_spell("Fireball", "fire air"):',
    record_spell("Fireball", "fire air")
)
print(
    'record_spell("Dark Magic", "shadow"):',
    record_spell("Dark Magic", "shadow")
)
print()

print("Testing late import technique:")
print(
    'record_spell("Lightning", "air"):',
    record_spell("Lightning", "air")
)
print()

print("Circular dependency curse avoided using late imports!")
print("All spells processed safely!")
