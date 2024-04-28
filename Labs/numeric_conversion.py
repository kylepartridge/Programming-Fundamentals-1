# Define a menu function
def menu():
    print("Decoding Menu\n-------------")
    print("1. Decode hexadecimal\n2. Decode binary")
    print("3. Convert binary to hexadecimal\n4. Quit")
    print()


# Decodes a single hexadecimal digit and returns its value
def hex_char_decode(digit):
    decimal = 0
# If digit is above 9, assign its respective letter. Return the decimal value.
    if digit in range(0, 10):
        decimal = digit
    elif digit == "A" or digit == "a":
        decimal = 10
    elif digit == "B" or digit == "b":
        decimal = 11
    elif digit == "C" or digit == "c":
        decimal = 12
    elif digit == "D" or digit == "d":
        decimal = 13
    elif digit == "E" or digit == "e":
        decimal = 14
    elif digit == "F" or digit == "f":
        decimal = 15
    return decimal


# Decodes an entire hexadecimal string and returns its value
def hex_string_decode(hex):
    # Disregard first two "digits" if they begin with 0x
    if hex[0] == '0' and hex[1] == 'x':
        hex = hex[2:]
    decimal_number = 0
    # Work through each bit from right to left
    # Raise digit * 16 to "i-th" power with i increasing as we move left to right
    for i in range(len(hex)):
        position = len(hex) - 1 - i
        digit = hex[position]
        if digit == "A" or digit == "B" or digit == "C" or digit == "D" or digit == "E" or digit == "F" or digit == "a" or digit == "b" or digit == "c" or digit == "d" or digit == "e" or digit == "f":
            decimal_number += hex_char_decode(digit) * 16 ** i
        else:
            decimal_number += int(digit) * 16 ** i
    return decimal_number


# Decodes a binary string and returns its value
def binary_string_decode(binary):
    # Disregard if string starts with 0b
    if binary[0] == '0' and binary[1] == 'b':
        binary = binary[2:]
    decimal_number = 0
    # Same process as hex decoding except with base 2
    for i in range(len(binary)):
        position = len(binary) - 1 - i
        digit = binary[position]
        decimal_number += int(digit) * 2 ** i
    return decimal_number


# Decodes a binary string, re-encodes as hexadecimal, and returns its hexadecimal string
def binary_to_hex(binary):
    # Initialize an empty string that we will append to later on
    hex = ""
    # Disregard first two digits if we start with 0b
    if binary[0] == '0' and binary[1] == 'b':
        binary = binary[2:]
    # If length(binary) is not even, add a leading zero
    if len(binary) % 2 != 0:
        binary = "0" + binary
    # Determine the # of groups of 4
    groups = int(len(binary) / 4)
    # Make sure to iterate over # of groups
    for i in range(groups):
        # Convert first 4 hex digits to binary
        result_1 = int(binary[0]) * 2 ** 3
        result_2 = int(binary[1]) * 2 ** 2
        result_3 = int(binary[2]) * 2 ** 1
        result_4 = int(binary[3]) * 2 ** 0
        # Store sum
        result = result_1 + result_2 + result_3 + result_4
        # Encode to letters if need be
        if result in range(0, 10):
            result = str(result)
        elif result == 10:
            result = "A"
        elif result == 11:
            result = "B"
        elif result == 12:
            result = "C"
        elif result == 13:
            result = "D"
        elif result == 14:
            result = "E"
        elif result == 15:
            result = "F"
        # Append the result to the hex string
        hex += result
        # Delete the leading four digits once we're done with calculations
        binary = binary[4:]
    return hex


def main():
    input_continues = True
    while input_continues:
        # Display menu and ask for input
        menu()
        option = input("Please enter an option: ")
        # Convert string from hex to decimal. Print result
        if option == "1":
            string = input("Please enter the numeric string to convert: ")
            result = hex_string_decode(string)
            print(f"Result: {result}")
            print()
        # Convert binary string to decimal. Print result
        elif option == "2":
            string = input("Please enter the numeric string to convert: ")
            result = binary_string_decode(string)
            print(f"Result: {result}")
            print()
        # Convert binary to hex. Print result.
        elif option == "3":
            string = input("Please enter the numeric string to convert: ")
            result = binary_to_hex(string)
            print(f"Result: {result}")
            print()
        # Break out of while loop
        elif option == "4":
            print("Goodbye!")
            input_continues = False

# Calling the main() function to execute program
if __name__ == '__main__':
    main()





