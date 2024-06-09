from Challenges.Challenge import Challenge
from Challenges.AnswerKeys import Answer4
from Challenges.Inputs import Input4

challenge = Challenge(
    name="Challenge 4 - Grid Hits",
    instr="This challenge inputs two things: A two dimensional array (grid) full of O's and a string of hit locations.\n"
          "It's your job to take the hit locations and put X's in the grid at those locations. The outer dimension of\n"
          "the grid should represent your Y axis and the inner dimension should be your X axis.\n"
          "The hit locations will be denoted as LetterNumber (i.e. A1, C4, etc). Letters represent the Y axis\n"
          "and Numbers represent the X axis. The top left grid square is A0 (denoted grid[0][0]) the bottom right is J9 (denoted grid[9][9]).\n"
          "The Location C8 would be denoted as grid[3][8].\n"
          "Good luck!"
          "\n\nFor bonus points, do this without ever looping through the grid itself",
    answer=Answer4.ANSWER
)

def replaceLetters(location) -> str:
    match location:
        case "A":
            return "0"
        case "B":
            return "1"
        case "C":
            return "2"
        case "D":
            return "3"
        case "E":
            return "4"
        case "F":
            return "5"
        case "G":
            return "6"
        case "H":
            return "7"
        case "I":
            return "8"
        case "J":
            return "9"

def getNumberLetter(letter: str) -> int:
    match letter:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 2
        case "D":
            return 3
        case "E":
            return 4
        case "F":
            return 5
        case "G":
            return 6
        case "H":
            return 7
        case "I":
            return 8
        case "J":
            return 9
        case "K":
            return 10
        case "L":
            return 11
        case "M":
            return 12
        case "N":
            return 13
        case "O":
            return 14
        case "P":
            return 15
        case "Q":
            return 16
        case "R":
            return 17
        case "S":
            return 18
        case "T":
            return 19
        case "U":
            return 20
        case "V":
            return 21
        case "W":
            return 22
        case "X":
            return 23
        case "Y":
            return 24
        case "Z":
            return 25

def messageTrim(message: str) -> str:
    returnString = ""
    for x in message:
        if x != " ":
            returnString += x
        else:
            returnString += ""

    return returnString


def runChallengeCode() -> str:
    hitLocations = Input4.HIT_LOCATIONS
    grid = Input4.GRID
    #
    # Your Code Starts Here
    #

    #array for storing converted letter coordinates to be read in the grid
    xLocations = []
    #array for storing y coordinates
    yLocations = []

    #cycle through hitlocations
    for i in hitLocations:
        #add each new coordinates into updated locations array after running through replaceLetters
        xLocations.append(replaceLetters(i[0]))
        yLocations.append(i[1])

    a = 0
    y = 0
    x = 0
    while a < len(xLocations):
        x = int(xLocations[a])
        y = int(yLocations[a])
        grid[x][y] = "X"
        a += 1

    # Your Code Ends Here
    #
    return Answer4.formatAnswerGrid(grid)

def start():
    challenge.printInstructions()
    answerString = runChallengeCode()
    print(challenge.compareAnswer(answerString))
