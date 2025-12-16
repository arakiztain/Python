import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")

total_args = len(sys.argv)

if total_args == 1:
    print("No arguments provided!")
    print(f"Total arguments: {total_args}")
else:
    print(f"Arguments received: {total_args - 1}")

    i = 1
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1

    print(f"Total arguments: {total_args}")
