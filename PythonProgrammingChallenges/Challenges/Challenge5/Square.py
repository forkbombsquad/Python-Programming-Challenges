from .Shape import Shape

class Square(Shape):

    def __init__(self, sideLength: float):
        self.sideLength = sideLength

    def shapeName(self) -> str:
        return "Square"

    def area(self) -> float:
        return self.sideLength * self.sideLength