from . import Constants

PRINTOUT_DIVIDING_LINE = "======================"

def printProgramStart(challengeNumber: Constants.ChallengeNumber):
    print(f'\n\n{PRINTOUT_DIVIDING_LINE}\n\n')
    print(f'Starting {challengeNumber} Program...')

def printProgramEnd():
    print(f'\n\n{PRINTOUT_DIVIDING_LINE}')