import random

class Host:

    def __init__(self):
        self.doors = []

    def startNewGame(self):
        # The doors are stored as an array of booleans. Doors with goats are false, the door with the car is true.
        self.doors = [False, False, False]
        # Randomly determine which door has the car
        self.doors[random.randint(0, 2)] = True

    def revealGoat(self, contestantChoice: int) -> int:
        # TODO Challenge 8 - return the index of one of the two goat doors, but make sure it's not the contestant's chosen door!
        return 0

    def checkForWinner(self, contestantChoice: int) -> bool:
        # TODO Challenge 8 - return whether or not the contestant won the game based on their choice. Reminder, the contestant should've switched their door after the goat reveal!
        return False