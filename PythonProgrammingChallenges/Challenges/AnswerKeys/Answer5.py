from collections.abc import MutableSequence
from Challenges.Challenge5.Shape import Shape

ANSWER = "Square 25.0\n" \
         "Triangle 6.0\n" \
         "Circle 803.84\n" \
         "Rectangle 32.0\n" \
         "Oval 37.68\n" \
         "Square 144.0\n" \
         "Triangle 0.5\n" \
         "Circle 254.34\n" \
         "Rectangle 3.0\n" \
         "Oval 21.98\n"

def getAnswerString(shapeArray: MutableSequence[Shape]) -> str:
    answerStr = ""
    for shape in shapeArray:
        answerStr += shape.shapeName() + " " + str(shape.area())
        answerStr += "\n"
    return answerStr