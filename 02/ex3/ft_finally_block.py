def water_plants(plant_list):
    """
    Simulates a garden watering system.

    Opens the watering system, waters each plant in the list,
    handles invalid plant names, and always performs cleanup
    using a finally block.
    """
    success = True
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                success = False
                raise Exception
            print(f"Watering {plant}")
    except (Exception):
        print("Error: Cannot water None - invalid plant!")
        success = False
    finally:
        print("Closing watering system (cleanup)")

    if success:
        print("Watering completed successfully!")


def test_watering_system():
    """
    Tests the watering system with valid and invalid plant lists.

    Demonstrates normal execution, error handling,
    and that cleanup always occurs.
    """
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(["tomato", None])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
