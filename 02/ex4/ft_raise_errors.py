def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Checks whether a plant is healthy based on its name, water level,
    and daily sunlight hours.

    Parameters:
    - plant_name (str): Name of the plant. Must not be empty.
    - water_level (int): Water level from 1 to 10.
    - sunlight_hours (int): Sunlight exposure from 2 to 12 hours.

    Raises:
    - ValueError: If any parameter is out of the allowed range or invalid.
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low (min 1)")

    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")

    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """
    Runs a series of tests to validate the behavior of the
    check_plant_health function with both valid and invalid inputs.
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 6)
    except ValueError as e:
        print(e)

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        check_plant_health("lettuce", 15, 6)
    except ValueError as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("carrots", 5, 0)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


test_plant_checks()
