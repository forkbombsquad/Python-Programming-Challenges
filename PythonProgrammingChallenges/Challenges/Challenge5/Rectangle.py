from .Shape import Shape


class Rectangle(Shape):

    def __init__(self, side1: float, side2: float):
        self.side1 = side1
        self.side2 = side2

    def shapeName(self) -> str:
        return "Rectangle"

    def area(self) -> float:
        return self.side1 * self.side2

# TODO CHALLENGE 5
