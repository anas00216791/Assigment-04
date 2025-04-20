"""
Program: Dice Simulator
------------------------
Simulates rolling two dice, three times. Prints the
results of each die roll and their total. Demonstrates
how variable scope works in Python.
"""

import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their individual values and total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Rolled: die1 = {die1}, die2 = {die2} → Total = {total}")

def main():
    # This die1 is local to main() and is unaffected by roll_dice()
    die1 = 10
    print(f"die1 in main() starts as: {die1}")

    # Roll dice three times
    roll_dice()
    roll_dice()
    roll_dice()

    print(f"die1 in main() after rolls is still: {die1}")

# Call main() when this script runs
if __name__ == '__main__':
    main()
