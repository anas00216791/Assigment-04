import time

import time
import sys

def main():
    # This for-loop starts at 0 and counts up to 19 (total 20 numbers)
    for i in range(20):
        print(i * 2)
        time.sleep(0.2)  # Add a short delay of 0.2 seconds

# Call the main function
if __name__ == "__main__":
    main()
    for i in range(20):
        print(f"Loading: {i * 2}", end='\r', flush=True)
        time.sleep(0.3)
    print("\nDone!")

if __name__ == "__main__":
    main()
    for i in range(20):
        print(f"Loading: {i * 2}", end='\r', flush=True)
        time.sleep(0.3)
    print("\nDone!")
    for i in range(20):
        print(f"Loading: {i * 2}", end='\r', flush=True)
        time.sleep(0.3)
    print("\nDone!")