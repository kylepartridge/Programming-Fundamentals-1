from pakudex import Pakudex

def menu():
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri")
    print("4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit")
    print()

def main():
    # Print a welcome message
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    # Ask for capacity and make sure the user enters an integer
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity < 0:
                print("Please enter a valid size.")
                continue
            else:
                break
        except:
            print("Please enter a valid size.")

    # Create a Pakudex instantiation "pakudex" with capacity
    pakudex = Pakudex(capacity)
    # Call the get_capacity() method from Pakudex
    print(f"The Pakudex can hold {pakudex.get_capacity()} species of Pakuri.")
    print()
    while True:
        # Print menu options and ask for an input
        menu()
        option = input("What would you like to do? ")
        # List all species in the Pakudex in the order entered
        if option == "1":
            # Make sure the pakudex is not empty
            if pakudex.get_species_array() is None:
                print("No Pakuri in Pakudex yet!")
                print()
            else:
                print("Pakuri In Pakudex:")
                for index, species in enumerate(pakudex.get_species_array()):
                    print(f"{index+1}. {species}")
        # Prompt user to enter a species and display information
        elif option == "2":
            species = input("Enter the name of the species to display: ")
            # Make sure the species exist in get_species_array()
            if pakudex.get_species_array() is None or species not in pakudex.get_species_array():
                print("Error: No such Pakuri!")
                print()
            else:
                print(f"Species: {species}")
                print(f"Attack: {pakudex.get_stats(species)[0]}")
                print(f"Defense: {pakudex.get_stats(species)[1]}")
                print(f"Speed: {pakudex.get_stats(species)[2]}")
                print()
        # Add a Pakuri species with user inputted name
        elif option == "3":
            # Make sure Pakudex is not full
            if pakudex.get_size() == pakudex.get_capacity():
                print("Error: Pakudex is full!")
                print()
                continue
            species = input("Enter the name of the species to add: ")
            # If get_species_array() returns None, still add the species to it
            if pakudex.get_species_array() is None or species not in pakudex.get_species_array():
                pakudex.add_pakuri(species)
                print(f"Pakuri species {species} successfully added!")
                print()
            # Make sure species doesn't exist in Pakudex
            elif species in pakudex.get_species_array():
                print("Error: Pakudex already contains this species!")

        # Evolve the Pakuri species inputted by user
        elif option == "4":
            species = input("Enter the name of the species to evolve: ")
            if pakudex.get_species_array() is None or species not in pakudex.get_species_array():
                print("Error: No such Pakuri!")
                print()
            else:
                pakudex.evolve_species(species)
                print(f"{species} has evolved!")
                print()
        # Sort Pakuri species
        elif option == "5":
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")
            print()
        # Break out of while loop
        elif option == "6":
            print("Thanks for using Pakudex! Bye!")
            break
        # User error for input other than 1, 2, 3, 4, 5, 6
        else:
            print("Unrecognized menu selection!")
            print()


if __name__ == "__main__":
    main()