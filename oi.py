import random
import time

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    
    print("🤖 I am thinking of a number between 1 and 99...")
    time.sleep(1)

    # Get user's first guess
    guess = int(input("🎯 Enter your guess: "))

    # Repeat until user guesses correctly
    while guess != secret_number:
        print("🧠 Thinking...", end="", flush=True)
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)
        print()

        if guess < secret_number:
            print("🔽 Your guess is too low!")
        else:
            print("🔼 Your guess is too high!")

        print()  # Space before next guess
        time.sleep(0.5)
        guess = int(input("🔁 Try another guess: "))

    # Congratulate when guessed right
    print("🎉 Congrats! The number was:", secret_number)
    print("✨ You cracked the code!")

if __name__ == '__main__':
    main()
