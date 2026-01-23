"""
Game Coordinate System.

This script demonstrates working with 3D coordinates, calculating distances,
parsing coordinates from strings, handling errors, and tuple unpacking.
"""

import math


def calculate_distance(point_a, point_b):
    """
    Calculates the Euclidean distance between two 3D points.
    """
    return math.sqrt(
        (point_b[0] - point_a[0]) ** 2 +
        (point_b[1] - point_a[1]) ** 2 +
        (point_b[2] - point_a[2]) ** 2
    )


def ft_coordinate_system():
    """
    Runs coordinate calculations and parsing demonstrations.
    """
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)
    position = (10, 20, 5)

    distance = calculate_distance(origin, position)

    print(f"Position created: {position}")
    print(f"Distance between {origin} and {position}: {round(distance, 2)}")

    s = "3,4,0"
    print(f'\nParsing coordinates: "{s}"')

    try:
        parsed = tuple(int(x) for x in s.split(","))
        print(f"Parsed position: {parsed}")

        distance2 = calculate_distance(origin, parsed)
        print(f"Distance between {origin} and {parsed}: {round(distance2, 2)}")

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    invalid = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid}"')

    try:
        tuple(int(x) for x in invalid.split(","))

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
