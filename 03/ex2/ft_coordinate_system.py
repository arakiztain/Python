import math

print("=== Game Coordinate System ===")

origin = (0, 0, 0)
position = (10, 20, 5)

distance = math.sqrt(
    (position[0] - origin[0]) ** 2 +
    (position[1] - origin[1]) ** 2 +
    (position[2] - origin[2]) ** 2
)

print(f"Position created: {position}")
print(f"Distance between {origin} and {position}: {round(distance, 2)}")

s = "3,4,0"
print(f'\nParsing coordinates: "{s}"')

try:
    parsed = tuple(int(x) for x in s.split(","))
    print(f"Parsed position: {parsed}")

    distance2 = math.sqrt(
        (parsed[0] - origin[0]) ** 2 +
        (parsed[1] - origin[1]) ** 2 +
        (parsed[2] - origin[2]) ** 2
    )

    print(f"Distance between {origin} and {parsed}: {distance2}")

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
