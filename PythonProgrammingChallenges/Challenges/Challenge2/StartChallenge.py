from Challenges.Challenge import Challenge
from Challenges.AnswerKeys import Answer2
from Challenges.Inputs import Input2

challenge = Challenge(
    name="Challenge 2 - Unconventional Sorting",
    instr="This challenge inputs a list of all the letters of the alphabet in alphabetical order."
          "\nIt's your job to take that list and make a new list that alternates between the first and last letters of the alphabet, like so:"
          "\nA, Z, B, Y, C, X ... etc"
          "\n\nFor bonus points, see if you can finish this challenge in 5 lines of code or less!",
    answer=Answer2.ANSWER
)

def runChallengeCode() -> str:
    inputList = Input2.INPUT
    answerList = []
    #
    # Your Code Starts Here
    #

    # TODO Challenge 2

    #
    # Your Code Ends Here
    #
    return answerList.__str__().replace("[","").replace("]", "")

def start():
    challenge.printInstructions()
    answerString = runChallengeCode()
    print(challenge.compareAnswer(answerString))
