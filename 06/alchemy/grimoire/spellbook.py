def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    valdiation = validate_ingredients(ingredients)

    if "VALID" in valdiation:
        return f"Spell recorded: {spell_name} ({valdiation})"

    return f"Spell rejected: {spell_name} ({valdiation})"
