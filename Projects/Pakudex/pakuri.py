# Create a Pakuri class with initial values of species, attack, defense and speed
class Pakuri:
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

# Getter for species type
    def get_species(self):
        return self.species
# Getter for attack value
    def get_attack(self):
        return self.attack
# Getter for defense value
    def get_defense(self):
        return self.defense
# Getter for speed value
    def get_speed(self):
        return self.speed
# Setter for new attack value
    def set_attack(self, new_attack):
        self.attack = new_attack

# Evolve species by increasing attack, defense and speed
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

# Define method to be done for sorting
    def __lt__(self, other):
        return self.species < other.species
