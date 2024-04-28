from cow import Cow

class FileCow(Cow):
    def __init__(self, name, filename):
        super().__init__(name)
        try:
            # Open the .cow file and read it
            with open(filename, 'r') as f:
                self.image = f.read()
        except FileNotFoundError:
            # If the file is not found, raise an error
            raise RuntimeError("MOOOOO!!!!!!")

    def set_image(self, image):
        raise RuntimeError("Cannot reset FileCow image")

