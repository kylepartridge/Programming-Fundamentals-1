from cow import Cow

class Dragon(Cow):
    # Constructor; creates a new Dragon object with the given name and image.
    def __init__(self, name, image):
        super().__init__(name)
        self.set_image(image)



    # Exists in every Dragon class. For the default Dragon type, it should always return True
    def can_breathe_fire(self):
        return True


