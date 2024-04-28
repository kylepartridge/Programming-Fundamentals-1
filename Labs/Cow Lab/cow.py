class Cow:
    # Initialize a cow object with name and image set to be None
    def __init__(self, name):
        self.name = name
        self.image = None

# Return the name of the cow
    def get_name(self):
        return self.name

# Return the image used to display the cow
    def get_image(self):
        return self.image

# Sets the image used to display the cow
    def set_image(self, image):
        self.image = image




