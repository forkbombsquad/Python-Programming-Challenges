from Utils.Constants import ChallengeNumber
from Utils import Printer
from Challenges import AllChallenges
import Challenges

# This is the program entry point. You can set up other schemes to run different files on start, but this is the default.

# For each challenge, change the enum below to be the appropriate level:
challengeToRun = ChallengeNumber.CHALLENGE_1

Printer.printProgramStart(challengeToRun)

match challengeToRun:
    case ChallengeNumber.CHALLENGE_1:
        # Start Challenge1
        AllChallenges.Challenge1.start()
    case ChallengeNumber.CHALLENGE_2:
        # Start Challenge 2
        print("Todo")

Printer.printProgramEnd()