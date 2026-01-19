"""Simple plant growth simulation module."""


class Plant:
    """Represents a plant that can grow and age."""

    def __init__(self, name, height_cm, age_days):
        """Initialize the plant with name, height, and age."""
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def get_info(self):
        """Print the current information of the plant."""
        print(
            f"{self.name.capitalize()}: "
            f"{self.height_cm}cm, {self.age_days} days old"
        )

    def grow(self):
        """Increase the plant height by 1 cm."""
        self.height_cm += 1

    def age(self, days):
        """Increase the plant age by the given number of days."""
        self.age_days += days


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height_cm

    print("=== Day 1 ===")
    rose.get_info()

    days_to_simulate = 4
    for _ in range(days_to_simulate - 1):
        rose.grow()
        rose.age(1)

    print(f"=== Day {days_to_simulate} ===")
    rose.get_info()

    growth = rose.height_cm - initial_height
    print(f"Growth this week: +{growth}cm")
