class GardenError(Exception):
    """Base error for garden-related problems."""
    pass


class PlantError(GardenError):
    """Error for plant-related problems."""
    pass


class WaterError(GardenError):
    """Error for watering-related problems."""
    pass


def test_plant_error():
    """
    Function that raises a PlantError.

    Used to simulate a plant-related problem in the garden.
    """
    raise PlantError("The tomato plant is wilting!")


def test_water_error():
    """
    Function that raises a WaterError.

    Used to simulate a watering-related problem in the garden.
    """
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """
    Demonstrates catching custom garden errors.

    - Tests PlantError and WaterError individually.
    - Shows how GardenError can catch all related errors.
    - Prints messages to demonstrate proper error handling.
    """
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")

    try:
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")

    try:
        test_plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        test_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
