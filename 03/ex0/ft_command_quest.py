"""
Command Quest: A simple script to display command-line arguments.
"""

import sys


def main():
    """
    Reads and displays command-line arguments passed to the program.
    """
    print("=== Command Quest ===")

    total_args = len(sys.argv)

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {total_args}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {total_args - 1}")

        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"Argument {i}: {arg}")

        print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
