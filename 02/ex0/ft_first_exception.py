def check_temperature(temp_str):
    """
    Validate and check a temperature reading for plants.
    Args:
        temp_str (str): Temperature input as a string.
    Prints a message depending on whether the temperature is valid,
    too high, too low, or not a number.
    """
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """
    Test the check_temperature function with various inputs.
    """
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
