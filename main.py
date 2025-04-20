def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total = 0
    for number in numbers:
        total += number
    return total

# No need to edit beyond this point
def main():
    numbers = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers = add_many_numbers(numbers)  # Find the sum of the list
    print(f"The sum is: {sum_of_numbers}")  # Print out the sum

if __name__ == '__main__':
    main()
