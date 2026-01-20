def garden_operations():
    """
    Demonstrates common Python errors in garden operations.
    Each block triggers a specific error:
    - ValueError when converting a non-numeric string to int
    - ZeroDivisionError when dividing by zero
    - FileNotFoundError when opening a non-existent file
    - KeyError when accessing a missing key in a dictionary
    All errors are caught to prevent the program from crashing.
    """
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        _ = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        with open("missing.txt", "r") as f:
            _ = f.read()
    except FileNotFoundError as f:
        print(f"Caught FileNotFoundError: No such file '{f.filename}'\n")

    try:
        print("Testing KeyError...")
        my_dict = {"rose": 1}
        _ = my_dict["missing_plant"]
    except KeyError as k:
        print(f"Caught KeyError: '{k}'\n")


def test_error_types():
    """
    Runs the garden_operations function and demonstrates error handling.
    Prints a header, runs all error tests, and shows that the program continues
    execution after each error.
    """
    print("=== Garden Error Types Demo ===\n")
    try:
        garden_operations()
        print("Testing multiple errors together...")
        int(None)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as e:
        print(f"Caught {e}")
    except Exception:
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
