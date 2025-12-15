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
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    
    try:
        print("Testing FileNotFoundError...")
        with open("missing.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    
    try:
        print("Testing KeyError...")
        my_dict = {"rose": 1}
        value = my_dict["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")
        

def test_error_types():
    """
    Runs the garden_operations function and demonstrates error handling.
    
    Prints a header, runs all error tests, and shows that the program continues 
    execution after each error.
    """
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error handling tests completed - program didn't crash!")


if __name__ == "__main__":
    test_error_types()
