from .Shape import Shape

class Oval(Shape):

    def __init__(self, radius1: float, radius2: float):
        self.radius1 = radius1
        self.radius2 = radius2

    def shapeName(self) -> str:
        return "Oval"

    def area(self) -> float:
        return self.radius1 * self.radius2 * 3.14

# TODO CHALLENGE 5