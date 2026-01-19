class Plant:
    """
    Base class representing a generic plant.

    Attributes:
        name (str): Name of the plant.
        height (int): Current height of the plant in centimeters.
    """

    def __init__(self, name, height):
        """
        Initialize a plant with a name and an initial height.

        Args:
            name (str): Plant name.
            height (int): Initial height in centimeters.
        """
        self.name = name
        self.height = height

    def grow(self):
        """
        Increase the plant height by one centimeter.
        """
        self.height += 1
        print(f"{self.name} grew 1cm")

    def description(self):
        """
        Return a textual description of the plant.
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Represents a plant that produces flowers.
    """

    def __init__(self, name, height, color):
        """
        Initialize a flowering plant.

        Args:
            name (str): Plant name.
            height (int): Initial height.
            color (str): Flower color.
        """
        super().__init__(name, height)
        self.color = color

    def description(self):
        """
        Return a description including flower information.
        """
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """
    Special flowering plant that awards prize points.
    """

    def __init__(self, name, height, color, prize_points):
        """
        Initialize a prize flower.

        Args:
            name (str): Plant name.
            height (int): Initial height.
            color (str): Flower color.
            prize_points (int): Prize points associated with the plant.
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def description(self):
        """
        Return a detailed description including prize points.
        """
        return (
            f"{self.name}: {self.height}cm, {self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    """
    Manages a garden and its plants, including analytics and reporting.
    """

    total_gardens = 0

    class GardenStats:
        """
        Utility class providing statistical calculations for gardens.
        """

        @staticmethod
        def validate_height(plant):
            """
            Validate that a plant has a positive height.

            Args:
                plant (Plant): Plant to validate.

            Returns:
                bool: True if height is valid, False otherwise.
            """
            return plant.height > 0

        @staticmethod
        def count_types(plants):
            """
            Count plant types in a garden.

            Args:
                plants (list): List of plant objects.

            Returns:
                tuple: Counts of regular, flowering and prize plants.
            """
            regular = flowering = prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def total_growth(plants):
            """
            Calculate total growth based on number of plants.

            Args:
                plants (list): List of plant objects.

            Returns:
                int: Total growth value.
            """
            return len(plants)

    def __init__(self, owner):
        """
        Initialize a garden manager.

        Args:
            owner (str): Owner of the garden.
        """
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        """
        Add a plant to the garden.

        Args:
            plant (Plant): Plant to add.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self):
        """
        Make all plants in the garden grow.
        """
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        """
        Print a detailed garden report.
        """
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.description()}")
            if isinstance(plant, PrizeFlower):
                print()

        regular, flowering, prize = self.GardenStats.count_types(self.plants)
        print(
            f"Plants added: {len(self.plants)}, "
            f"Total growth: {self.GardenStats.total_growth(self.plants)}cm"
        )
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, {prize} prize flowers"
        )
        print()
        print(
            f"Height validation test: "
            f"{self.GardenStats.validate_height(self.plants[0])}"
        )

    @classmethod
    def create_garden_network(cls, *gardens):
        """
        Create a network analysis across multiple gardens.

        The score for each garden is calculated as the sum of:
        - The height of all plants in the garden
        - Additional points for prize flowers, calculated as
        prize_points multiplied by 4

        Args:
            *gardens: Variable number of GardenManager instances.

        Returns:
            dict: Mapping of garden owners to their total garden scores.
        """
        scores = {}
        for garden in gardens:
            total = 0
            for plant in garden.plants:
                total += plant.height
                if isinstance(plant, PrizeFlower):
                    total += plant.prize_points * 4
            scores[garden.owner] = total
        return scores


print("=== Garden Management System Demo ===")
print()

alice = GardenManager("Alice")
bob = GardenManager("Bob")

alice.add_plant(Plant("Oak Tree", 100))
alice.add_plant(FloweringPlant("Rose", 25, "red"))
alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
print()

bob.plants.append(Plant("Hidden Plant", 92))

alice.help_grow()
print()

alice.report()

scores = GardenManager.create_garden_network(alice, bob)
print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")
print(f"Total gardens managed: {GardenManager.total_gardens}")
