from functools import partial


class ImageBase:
    """Abstract image"""

    @classmethod
    def create(cls, width, height):
        """create image"""
        return cls(width, height)

    def draw(self, x, y, color):
        """Draws a point in a given color"""
        raise NotImplementedError()

    def fill(self, color):
        """Color fill"""
        raise NotImplementedError()

    def save(self, filename):
        """Save image to file"""
        raise NotImplementedError()


class Image(ImageBase):
    def __init__(self, width, height):
        self._width = int(width)
        self._height = int(height)

    def draw(self, x, y, color):
        print(f"Draw point; Coordinates: ({x}, {y}); цвет: {color}")

    def fill(self, color):
        print(f"Fill image by {color} color")

    def save(self, filename):
        print(f"Save image to {filename}")


class ImageProxy(ImageBase):
    """
    Delays the execution of operations on the image until it is saved.
    """

    def __init__(self, *args, **kwargs):
        self._image = Image(*args, **kwargs)
        self.operations = []

    def draw(self, *args):
        func = partial(self._image.draw, *args)
        self.operations.append(func)

    def fill(self, *args):
        func = partial(self._image.fill, *args)
        self.operations.append(func)

    def save(self, filename):
        # we perform all operations on the image
        map(lambda f: f(), self.operations)
        # save image
        self._image.save(filename)


img = ImageProxy(200, 200)
img.fill("gray")
img.draw(0, 0, "green")
img.draw(0, 1, "green")
img.draw(1, 0, "green")
img.draw(1, 1, "green")
img.save("image.png")
