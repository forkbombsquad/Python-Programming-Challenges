from collections.abc import MutableSequence
from Challenges.Challenge import Challenge
from Challenges.AnswerKeys import Answer5
from Challenges.Inputs import Input5
from .Shape import Shape

from .Triangle import Triangle
from .Square import Square
from .Circle import Circle
from .Rectangle import Rectangle
from .Oval import Oval

challenge = Challenge(
    name="Challenge 5 - Shapes and Inheritance",
    instr="This challenge inputs a list of shape types and sizes. It's your job to take them and turn them into shape objects.\n"
          "There are several class files in this folder that represent the different shapes all extending the base Shape class.\n"
          "You will need to go into each file and fill out the missing information so that the classes function properly.\n"
          "Rectangle has been finished for you so that you can see the way its supposed to be structured.\n"
          "In the end, the area function of each shape will be called and compared with the true answer.\n"
          "Note - You should use 3.14 for pi"
          "Good luck!"
          "\n\nThe shapes in the input array are formatted as such:\n"
          "'T[1,2]' = Triangle[base,height]\n"
          "'R[1,2]' = Rectangle[side1,side2]\n"
          "'S[1]' = Square[side]\n"
          "'C[1]' = Circle[radius]\n"
          "'O[1,2]' = Oval[radius1,radius2]\n",
    answer=Answer5.ANSWER
)

def runChallengeCode() -> str:
    shapesInput = Input5.SHAPES
    shapeArray: MutableSequence[Shape] = []
    #
    # Your Code Starts Here
    #
    for i in shapesInput:
        match i[0]:
            case "C":
                radius = str(i).strip("C").strip("[").strip("]")
                shapeArray.append(Circle(float(radius)))
            case "O":
                radii = str(i).strip("O").strip("[").strip("]")
                radii = radii.split(",")
                radius1 = radii[0]
                radius2 = radii[1]
                shapeArray.append(Oval(float(radius1), float(radius2)))
            case "R":
                sides = str(i).strip("R").strip("[").strip("]")
                sides = sides.split(",")
                side1 = sides[0]
                side2 = sides[1]
                shapeArray.append(Rectangle(float(side1), float(side2)))
            case "S":
                sides = str(i).strip("S").strip("[").strip("]")
                shapeArray.append(Square(float(sides)))
            case "T":
                baseHeight = str(i).strip("T").strip("[").strip("]")
                baseHeight = baseHeight.split(",")
                base = baseHeight[0]
                height = baseHeight[1]
                shapeArray.append(Triangle(float(base), float(height)))






    # TODO Challenge 5

    #
    # Your Code Ends Here
    #
    return Answer5.getAnswerString(shapeArray)

def start():
    challenge.printInstructions()
    answerString = runChallengeCode()
    print(challenge.compareAnswer(answerString))
