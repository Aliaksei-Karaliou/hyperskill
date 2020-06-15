class Sphere:
    pi = 3.1415

    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.volume = 4 / 3 * self.pi * radius ** 3
