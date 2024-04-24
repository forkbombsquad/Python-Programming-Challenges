from .Shape import Shape

class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def shapeName(self) -> str:
        return "Circle"

    def area(self) -> float:
        return self.radius * self.radius * 3.14

# TODO CHALLENGE 5