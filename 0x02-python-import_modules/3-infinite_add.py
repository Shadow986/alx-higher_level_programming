#!/usr/bin/python3
import sys

def main():
    # Initialize sum to 0
    sum = 0

    # Iterate over all arguments
    for arg in sys.argv[1:]:
        # Add the integer value of the argument to the sum
        sum += int(arg)

    # Print the sum followed by a new line
    print(sum)

# Ensure the code is not executed when imported
if __name__ == "__main__":
    main()
