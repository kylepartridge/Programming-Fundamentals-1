from dragon import Dragon

class IceDragon(Dragon):
    # Constructor; creates a new IceDragon object with the given name and image.
    def __init__(self, name, image):
        super().__init__(name, image)


    def can_breathe_fire(self):
        # For the IceDragon type, this method should always return False.
        return False