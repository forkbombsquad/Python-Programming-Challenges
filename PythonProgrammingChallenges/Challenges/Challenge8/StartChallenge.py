from Challenges.Challenge import Challenge
from Challenges.AnswerKeys import Answer8
from .Host import Host
from .Contestant import Contestant

challenge = Challenge.withRange(
    name="Challenge 8 - Monty Hall",
    instr="This challenge has you simulating a Monty Hall game show to show that, counterintuitively,\n"
          "switching your door give you increased odds of winning.\n"
          "The Monty Hall game is simple. A contestant chooses one of three doors to be their door.\n"
          "Behind two of the doors are goats, but behind the third door is a new car!\n"
          "After the contestant chooses their door, the host will open a DIFFERENT door - but always one that has a goat behind it.\n"
          "The host will then offer the contestant the opportunity to switch which door they picked to the other unopened door.\n"
          "Your simulation will show that contestants have a 66% chance of winning if they switch doors, while only a 33% chance of winning if they\n"
          "Keep their original picks.\n\n"
          "You are provided with a few class files in this folder to help you out structuring your game.\n"
          "You will need to fill in a few of the functions to make them work properly.\n"
          "You should run the simulation 100,000 times,\n"
          "Always having the contestant switch doors. Record the total number of wins and losses.\n"
          "Then take the total number of wins and divide it by the total number of games to be your answer.\n"
          "With 100,000 games you should always be within the margin of error if you simulated the game correctly.\n"
          "Make sure you convert your answers to floats so that you don't lose your decimal points!\n"
          "Good Luck!",
    answerBottom=Answer8.ANSWER_BOTTOM,
    answerTop=Answer8.ANSWER_TOP
)

def runChallengeCode() -> float:
    host = Host()
    answerPercentage = 0.0

    wins = 0
    losses = 0
    #
    # Your Code Starts Here
    #

    # TODO Challenge 8
    # Remember to use contestant.selectedDoor to get their current guess.

    #
    # Your Code Ends Here
    #

    return answerPercentage

def start():
    challenge.printInstructions()
    percentage = runChallengeCode()
    print(challenge.compareAnswerWithMarginOfError(percentage))
