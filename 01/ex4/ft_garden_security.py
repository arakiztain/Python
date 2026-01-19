class SecurePlant:
    """
    Represents a secure plant, protecting its sensitive data (height and age)
    against invalid values. Provides methods to safely access and modify
    its attributes.
    """

    def __init__(self, name, height, age):
        """
        Initializes a new secure plant.

        :param name: Name of the plant
        :param height: Initial height in cm
        :param age: Initial age in days
        """
        self._name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0
        print("Plant created:", self._name)

    def get_height(self):
        """Returns the height of the plant in cm."""
        return self._height

    def get_age(self):
        """Returns the age of the plant in days."""
        return self._age

    def set_height(self, new_height):
        """
        Safely sets the height of the plant.
        Rejects negative values with an error message.
        """
        if new_height < 0:
            print(
                f"Invalid operation attempted: "
                f"height {new_height}cm [REJECTED]"
                )
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, new_age):
        """
        Safely sets the age of the plant.
        Rejects negative values with an error message.
        """
        if new_age < 0:
            print(
                f"Invalid operation attempted: "
                f"age {new_age} days [REJECTED]"
                )
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days [OK]")

    def show(self):
        """Prints the current state of the plant."""
        print(
            f"Current plant: {self._name} "
            f"({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 10, 20)
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print()
    plant.show()
