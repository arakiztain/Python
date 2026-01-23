"""
Player Score Analytics.

This script processes player scores passed as command-line arguments
and displays basic statistics such as total, average,
highest, and lowest score.
"""

import sys


def ft_score_analytics():
    """
    Reads player scores from command-line arguments and prints statistics.
    """
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return

    try:
        scores = [int(x) for x in sys.argv[1:]]

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")

    except ValueError:
        print("Error: all scores must be valid integers")


if __name__ == "__main__":
    ft_score_analytics()
