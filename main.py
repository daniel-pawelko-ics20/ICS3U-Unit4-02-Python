#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Nov 2021
# Do while loop


def main():
    # main function for creating do while loop

    # variables
    counter = 0
    product_num = 1

    # asking for input
    number = input("Enter a positive integer: ")
    number = int(number)

    # process
    while True:
        counter += 1
        product_num *= counter
        if counter >= number:
            break

    # output
    print(f"The product of all positive numbers from 1 to {number} is {product_num}.")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
