from Challenges.Challenge import Challenge
from .Opponent import Opponent
from .Checker import Checker
from .TTTEnums import TTTBoxState
import random

challenge = Challenge(
    name="Challenge 8 - Tic-Tac-Toe",
    instr="This challenge has you building an unbeatable tic-tac-toe computer.\n"
          "You will play X's and always move first, your opponent will play O's.\n"
          "10,000 games will be simulated. It's your job to ensure that your computer player is\n"
          "good enough that you only either tie or win, never lose.\n"
          "Your Tic-Tac-Toe board is a 3x3 grid (2 dimensional array) filled with TTTBoxState.EMPTY enums.\n"
          "Each turn you will place an X somewhere on the board and then pass the board to the Opponent who will place an O.\n"
          "Then pass the board to the checker who will check the board to see if there's a win state for either side.\n"
          "\n\n"
          "You can use this link to know how to always win/draw at TTT:\n"
          "https://www.wikihow.com/Win-at-Tic-Tac-Toe#:~:text=If%20you%27re%20the%20first%2Cto%20establish%20an%20end%2Dgame.\n"
          "Good Luck!",
    answer="0"
)

def getNewBoard() -> [[TTTBoxState]]:
    return [
        [TTTBoxState.EMPTY, TTTBoxState.EMPTY, TTTBoxState.EMPTY],
        [TTTBoxState.EMPTY, TTTBoxState.EMPTY, TTTBoxState.EMPTY],
        [TTTBoxState.EMPTY, TTTBoxState.EMPTY, TTTBoxState.EMPTY]
    ]

def prettyPrintBoard(board: [[TTTBoxState]]):
    printstr = ""
    for row in board:
        for box in row:
            printstr += " [" + str(box) + "]"
        print(printstr)
        printstr = ""

def runChallengeCode() -> str:
    opponent = Opponent()
    checker = Checker()
    board = getNewBoard()

    # TODO set this to true if you want to see a printout of the results of each game
    showPrintout = False

    gameCount = 0
    while gameCount < 10000:
    #
    # Your Code Starts Here
    #


    # TODO Challenge 9

    # TODO the following code between the <delete-this> tags should be deleted. It's only there so that the code can be run without infinite looping.
    # TODO <delete-this>
    # Literally just put an x randomly on the board
        row = random.randint(0, 2)
        box = random.randint(0, 2)
        while board[row][box] != TTTBoxState.EMPTY:
            row = random.randint(0, 2)
            box = random.randint(0, 2)

        board[row][box] = TTTBoxState.X
    # TODO </delete-this>

    #
    # Your Code Ends Here
    #
        board = opponent.takeTurn(board)
        if checker.checkGame(board):
            if showPrintout:
                print("\nW: " + str(checker.wins) + " L: " + str(checker.losses) + " T: " + str(checker.ties))
                prettyPrintBoard(board)
            gameCount += 1
            board = getNewBoard()

    return str(checker.losses)

def start():
    challenge.printInstructions()
    answer = runChallengeCode()
    print(challenge.compareAnswer(answer))
