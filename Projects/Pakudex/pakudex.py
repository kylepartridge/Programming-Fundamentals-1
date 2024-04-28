from pakuri import Pakuri
class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity    # Defaults to 20
        self.pakuris = []   # store a list of pakuri objects
        self.size = 0   # keep track of the # of concrete pakuri objects in self.pakuri
    # Getter for size
    def get_size(self):
        return self.size
# Getter for capacity
    def get_capacity(self):
        return self.capacity
# Return the species of the Pakuri objects in the Pakudex
    def get_species_array(self):
        res = []
        if self.size == 0:
            return None
        # loop through self.pakuris to look at each pakuri object
            # append pakuri.species to the res
        for pakuri_objects in self.pakuris:
            res.append(pakuri_objects.species)
        return res

# Same as get_species but return a list of attack, defense and speed values
    def get_stats(self, species):
        # loop through self.pakuris to look at each pakuri object
            # compare pakuri.species == species
            # if true, return
        for pakuri_objects in self.pakuris:
            if pakuri_objects.species == species:
                return [pakuri_objects.get_attack(), pakuri_objects.get_defense(), pakuri_objects.get_speed()]
        return None

# Sort method
    def sort_pakuri(self):
        self.pakuris.sort()

# Add a new species to Pakudex
    def add_pakuri(self, species):
        # 1. check duplicates first
        # loop through self.pakuris to look at each pakuri object
            # compare pakuri.species == species
        for pakuri_objects in self.pakuris:
            if pakuri_objects.species == species:
                return False
        # 2. when the list is full
        if self.size == self.capacity:
            return False
        # 3. add a new pakuri object into the list
        # 4. increment self.size
        else:
            self.pakuris.append(Pakuri(species))
            self.size += 1
            return True

# Evolve species in Pakuri object
    def evolve_species(self, species):
        for pakuri_objects in self.pakuris:
            if pakuri_objects.species == species:
                pakuri_objects.evolve()
                return True
        return False