class GardenError(Exception):
    """Base class for all garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception raised for errors related to plant operations."""
    pass


class WaterError(GardenError):
    """Exception raised for errors related to the watering system."""
    pass


class GardenManager:
    """
    A simple manager for a garden that can add plants, water them,
    and check their health using custom error handling.

    Attributes:
        plants (dict): Dictionary storing plants with their water
        and sunlight levels.
    """

    def __init__(self):
        """Initialize an empty garden with no plants."""
        self.plants = {}

    def add_plant(self, name, water_level, sunlight_hours):
        """
        Add a new plant to the garden.

        Args:
            name (str): The name of the plant. Must not be empty.
            water_level (int): Initial water level for the plant.
            sunlight_hours (int): Daily sunlight exposure for the plant.

        Raises:
            PlantError: If the plant name is empty.
        """
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {
            "water": water_level,
            "sun": sunlight_hours
        }
        print(f"Added {name} successfully")

    def water_plants(self):
        """
        Water all plants in the garden.

        Raises:
            WaterError: If there are no plants to water.

        Notes:
            This method always closes the watering system
            using a `finally` block
            to ensure proper cleanup.
        """
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name):
        """
        Check the health of a specific plant based on water
        and sunlight levels.

        Args:
            name (str): Name of the plant to check.

        Raises:
            PlantError: If the plant does not exist or has
            water/sunlight levels outside acceptable ranges.
        """
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")
        if water < 1:
            raise PlantError(f"Water level {water} is too low (min 1)")
        if sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too high (max 12)")
        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")


if __name__ == "__main__":
    """
    Test the GardenManager by adding plants, watering them,
    checking their health, and demonstrating error recovery
    using custom exceptions.
    """
    print("=== Garden Management System ===\n")

    garden = GardenManager()

    print("Adding plants to garden...")
    plants_to_add = [
        ("tomato", 5, 8),
        ("lettuce", 15, 6),
        ("", 3, 6)
    ]

    for plant in plants_to_add:
        try:
            garden.add_plant(*plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Watering error: {e}")

    print("\nChecking plant health...")
    for plant in garden.plants:
        try:
            garden.check_plant_health(plant)
        except PlantError as e:
            print(f"Error checking {plant}: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")
