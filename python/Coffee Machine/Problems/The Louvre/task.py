class Painting:
    museum = "the Louvre"

    def __init__(self, title, painter, year: int):
        super().__init__()
        self.title = title
        self.painter = painter
        self.year = year
        self.string = f"\"{title}\" by {painter} ({year}) hangs in {self.museum}."


painting = Painting(input(), input(), input())
print(painting.string)
