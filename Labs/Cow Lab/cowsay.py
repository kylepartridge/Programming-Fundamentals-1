# Import module for command line arguments and heifergenerator to access objects
import sys
from cow import Cow
from heifer_generator import HeiferGenerator
from dragon import Dragon
from ice_dragon import IceDragon
# list available cows in from Cow objects
def list_cows(cows):
    print("Cows available: ", end="")
    for i, cow in enumerate(cows):
        if i > 0:
            print(" ", end="")
        print(cow.name, end="")
    print()
    print("File cows available: ", end="")
    file_cows = HeiferGenerator.get_file_cows()
    for i, cow in enumerate(file_cows):
        if i > 0:
            print(" ", end="")
        print(cow.get_name(), end="")
    print()


# Check if inputted cow name exists in Cow object, return the name if so
def find_cow(name, cows):
    for cow in cows:
        if cow.name == name:
            return cow
    return None

if __name__ == "__main__":
    # Grab all the cows and file_cows from heifergenerator
    cows = HeiferGenerator.get_cows()
    file_cows = HeiferGenerator.get_file_cows()
    # If user enters "-l" return the Cow objects in a sentence
    if sys.argv[1] == '-l':
        list_cows(cows)
    # If user enters "-f", print the user message, if possible, and print the specified cow if it exists
    elif sys.argv[1] == '-f':
        cow_name = sys.argv[2]
        file_cow = None
        for cow in file_cows:
            if cow.get_name() == cow_name:
                file_cow = cow
                break
        if file_cow is None:
            print(f"Could not find {cow_name} cow!")
        else:
            words = sys.argv[3:]
            print(" ".join(words))
            print(file_cow.get_image())  # Access the image attribute of the FileCow object



    # Return error message if inputted cow doesn't exist. Otherwise print the message and the cow.image found from find_cow
    elif sys.argv[1] == '-n':
        if find_cow(sys.argv[2], cows) is None:
            print(f"Could not find {sys.argv[2]} cow!")
        else:
            # Grab words user inputted and join them with spaces
            words = sys.argv[3:]
            print(" ".join(words))
            # Create variable for user selected cow using find_cow() method
            selected_cow = find_cow(sys.argv[2], cows)
            # Print user selected cow
            print(find_cow(sys.argv[2], cows).image)
            # isinstance() returns true if user enters a dragon or ice-dragon since they are parent-child classes
            if isinstance(selected_cow, Dragon):  # Check if it's a Dragon or its subclass
                # If user enters dragon
                if selected_cow.can_breathe_fire():
                    print("This dragon can breathe fire.")
                # if user enters ice-dragon
                else:
                    print("This dragon cannot breathe fire.")
    # Print whatever message the user inputted and print the default heifer cow.image that is found from find_cow
    else:
        words = sys.argv[1:]
        print(" ".join(words))
        print(find_cow("heifer", cows).image)

