"""Module that creates plant objects using a factory pattern."""


class Plant:
    """Represents a plant with basic attributes."""

    def __init__(self, name, height, age):
        """Initialize a plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


class PlantFactory:
    """Factory class to create multiple Plant instances."""

    def __init__(self, configs):
        """Initialize the factory with plant configuration data."""
        self.configs = configs
        self.plants = []

    def create_all(self):
        """Create all plants from the configuration list."""
        for plant_data in self.configs:
            name = plant_data[0]
            height = plant_data[1]
            age = plant_data[2]
            plant = Plant(name, height, age)
            self.plants.append(plant)
            print("Created:", name, f"({height}cm,", age, "days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    configs = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    factory = PlantFactory(configs)
    factory.create_all()
    print()
    print("Total plants created:", len(factory.plants))
