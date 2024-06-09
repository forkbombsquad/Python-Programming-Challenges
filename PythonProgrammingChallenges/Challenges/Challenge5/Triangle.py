from .Shape import Shape


class Triangle(Shape):

    def __init__(self, height: float, base: float):
        self.height = height
        self.base = base

    def shapeName(self) -> str:
        return "Triangle"

    # TODO CHALLENGE 5
    def area(self) -> float:
        return self.height * self.base / 2
