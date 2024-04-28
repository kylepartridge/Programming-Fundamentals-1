from console_gfx import ConsoleGfx
# print menu
def menu():
    print("RLE Menu\n--------")
    print("0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String")
    print("4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image")
    print("7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data")
    print()

#convert data array to hex string
def to_hex_string(data):
    hex_string = ""
    dict_hex = {10: "a", 11: "b", 12: "c",
                13: "d", 14: "e", 15: "f",}
    for value in data:
        value = int(value)
        # Add integer value
        if value in range(0,10):
            hex_string += (str(value))
        # Else, look in dictionary
        elif value in range(10,16):
            hex_string += dict_hex[value]
        else:
            result_not_zero = True
            hex_appending = ""
            result = value
            # Probably not needed? In case there's an integer greater than 16...
            while result_not_zero:
                hex_appending += str(result % 16)
                result = result // 16
                if result == 0:
                    result_not_zero = False
            hex_appending = hex_appending[::-1]
            hex_string += hex_appending
    return hex_string

# Convert hex string to data array
def string_to_data(data_string):
    list = []
    # Dict to easily access alpabet data
    dict_hex = {"a": 10, "b": 11, "c": 12,
                "d": 13, "e": 14, "f": 15}
    # If there's a letter in the string, look in the dictionary. Else just append the integer value.
    for character in data_string:
        if character in dict_hex.keys():
            list.append(dict_hex[character])
        else:
            list.append(int(character))
    return list

# Convert flat data to RLE encoding
def encode_rle(flat_data):
    result = []
    current = flat_data[0]
    count = 1
    for item in flat_data[1:]:
        # Reset the count once we reach 15 but still add to the result list
        if current == item:
            if count == 15:
                result.extend([count, current])
                count = 1
            else:
                count += 1
        # Add the final pairing and reset the count
        else:
            result.extend([count, current])
            current = item
            count = 1
        # encode RLE: append count and current into result
    result.extend([count, current])
    return result

# Take the sum of every even integer because even indices indicate how many times the next element appears
def get_decoded_length(rle_data):
    sum_even = 0
    for index, item in enumerate(rle_data):
        if index % 2 == 0:
            sum_even += item
    return sum_even


# Count how many times data runs occur. If there are more than 15 repeats, reset the run but hold on to the count value
def count_runs(flat_data):
    if not flat_data:
        return 0
    count = 1
    repeat = 1
    for i in range(len(flat_data) - 1):
        if flat_data[i] != flat_data[i + 1]:
            count += 1
            repeat = 1  # Reset repeat for a new run
        else:
            repeat += 1
            if repeat > 15:
                count += 1
                repeat = 1  # Reset repeat after exceeding 15 repeats

    return count

# Opposite to encode_rle. Still step through every even element, repeat the next element the number of times of the integer preceeding.
def decode_rle(rle_data):
    result = []
    for i in range(0, len(rle_data), 2):  # Step through the list two elements at a time
        count = rle_data[i]
        value = rle_data[i+1]
        result.extend([value] * count)  # Append the value 'count' number of times

    return result

def to_rle_string(rle_data):
    rle_string = ''
    dict_hex = {10: "a", 11: "b", 12: "c",
                13: "d", 14: "e", 15: "f",}

    for index, number in enumerate(rle_data):
        if index % 2 == 0:
            if index != 0:  # Add a colon if it's not the first element
                rle_string += ":"
            rle_string += str(number)
        elif index % 2 != 0:
            if number >= 10:
                rle_string += dict_hex[number] # Look in dictionary to convert decimal # to hex letter
            else:
                rle_string += str(number)
    return rle_string


def string_to_rle(rle_string):
    dict_hex = {"a": 10, "b": 11, "c": 12,
                "d": 13, "e": 14, "f": 15}
    rle_data = []
    rle_temp = rle_string.split(":") # Split apart string into list by each colon
    for value in rle_temp:
        if len(value) == 3: # If we have a 3 element value, we need to look at the first two indices, then the third one
            number = int(value[0:2])
            hex_digit = value[-1]
            if hex_digit in dict_hex:
                hex_digit = dict_hex[hex_digit]
            rle_data.extend([number, hex_digit])
        elif len(value) == 2: # Otherwise, just look at the first and second element
            if value[0] in dict_hex:
                rle_data.append(dict_hex[value[0]])
            else:
                rle_data.append(int(value[0]))

            if value[1] in dict_hex: # If we have a letter in the second spot, look in dict_hex to convert
                rle_data.append(dict_hex[value[1]])
            else:
                rle_data.append(int(value[1]))
    return rle_data



# Project 2a
def main():
    image_data = None
    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print()
    while True:
        menu()
        option = input("Select a Menu Option: ")
        # Load a file from user input
        if option == "1":
            filename = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(filename)
        # Load test image
        if option == "2":
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.")
        # Read a RLE string from user input
        if option == "3":
            rle_data = input("Enter an RLE string to be decoded: ")
            rle_data = string_to_rle(rle_data) # Convert to RLE
            image_data = decode_rle(rle_data)  # Convert to flat data (image data)
        # Read a RLE Hex string from user input
        if option == "4":
            rle_data = input("Enter the hex string holding RLE data: ")
            rle_data = string_to_data(rle_data) # Convert to RLE
            image_data = decode_rle(rle_data)   # Convert to flat data
        # Read flat data from user input
        if option == "5":
            hex_string = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(hex_string) # Convert to flat data
        # Display the image either from user input or the test image
        if option == "6":
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)
        # Display the image data as RLE string
        if option == "7":
            image_data = encode_rle(image_data) # Convert to RLE byte data
            rle_string = to_rle_string(image_data) # Convert to RLE string
            print(f"RLE representation: {rle_string}")
        # Display image data as Hex RLE data
        if option == "8":
            image_data = encode_rle(image_data) # Convert to RLE byte data
            hex_string = to_hex_string(image_data) # Convert to RLE Hex string
            print(f"RLE hex values: {hex_string}")
        # Display image data as Hex flat data
        if option == "9":
            hexa_string = to_hex_string(image_data) # Convert to flat string
            print(f"Flat hex values: {hexa_string}")
        # Exit while loop
        if option == "0":
            break



if __name__ == "__main__":
    main()