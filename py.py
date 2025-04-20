import time

def get_user_numbers():
    """
    Ask the user to input numbers and store them in a list.
    Ends when the user enters a blank line.
    """
    user_numbers = []
    print("👋 Enter numbers one by one (leave blank to finish):")
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            print("⏳ Processing...\n")
            time.sleep(0.5)
            break
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("⚠️ Please enter a valid integer.")
    return user_numbers

def count_nums(num_lst):
    """
    Count how many times each number appears using a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        time.sleep(0.1)  # Animation: slight delay while counting
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    """
    Print how many times each number appears.
    """
    print("📊 Results:")
    time.sleep(0.3)
    for num in sorted(num_dict):  # Sorted for cleaner output
        print(f"🔢 {num} appears {num_dict[num]} time(s).")
        time.sleep(0.2)

def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

# Python boilerplate
if __name__ == '__main__':
    main()
