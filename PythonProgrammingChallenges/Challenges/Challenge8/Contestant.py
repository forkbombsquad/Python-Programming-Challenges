import random

class Contestant:

    def __init__(self):
        self.selectedDoor = -1

    def selectDoorAtRandom(self):
        # Contestant selects one of the three doors at random
        self.selectedDoor = random.randint(0, 2)

    def changeDoorSelection(self, revealedGoatDoor: int):
        # TODO Challenge 8 - set the contestant's selected door to be the remaining door (i.e. not the current selection and not the revealedGoatDoor)
        self.selectedDoor = -1
