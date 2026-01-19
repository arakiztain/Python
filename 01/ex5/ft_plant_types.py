class Plant:
    """Base class for all plants: stores common attributes."""

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show_base(self):
        """Return a string with the basic info."""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """Flower class: inherits Plant, adds color and bloom() method."""

    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def show(self):
        return (
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
                )


class Tree(Plant):
    """Tree class: inherits Plant, adds
    trunk_diameter and produce_shade() method."""

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        radius = self.trunk_diameter / 2
        shade_area = 3.14 * (radius ** 2) / 25
        print(f"{self.name} provides {shade_area:.0f} square meters of shade.")

    def show(self):
        return (
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
            )


class Vegetable(Plant):
    """Vegetable class: inherits Plant, adds
    harvest season and nutritional value."""

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional_info(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def show(self):
        return (
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
                )


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 1460, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 40, 60, "spring", "vitamin A")

    plants = [rose, tulip, oak, pine, tomato, carrot]

    for p in plants:
        print(p.show())
        if isinstance(p, Flower):
            p.bloom()
        elif isinstance(p, Tree):
            p.produce_shade()
        elif isinstance(p, Vegetable):
            p.nutritional_info()
        print()
