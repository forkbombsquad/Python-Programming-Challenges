import random
from .TTTEnums import TTTBoxState
from .Checker import Checker

class Opponent:

    def __init__(self):
        self.personalChecker = Checker()

    def takeTurn(self, board: [[TTTBoxState]]) -> [[TTTBoxState]]:
        # Don't do anything if X already won
        if self.personalChecker.checkGame(board):
            return board

        potentialMove = self.xGoingToWin(board)
        if self.isFirstMove(board) or potentialMove[0] == -1:
            # Nowhere to block x yet so just move randomly
            row = random.randint(0, 2)
            box = random.randint(0, 2)
            while board[row][box] != TTTBoxState.EMPTY:
                row = random.randint(0, 2)
                box = random.randint(0, 2)
            board[row][box] = TTTBoxState.O
            return board
        else:
            # X is going to win so block them.
            board[potentialMove[0]][potentialMove[1]] = TTTBoxState.O
            return board


    def isFirstMove(self, board: [[TTTBoxState]]) -> bool:
        count = 0
        for row in board:
            for box in row:
                if box != TTTBoxState.EMPTY:
                    count += 1
                    if count > 1:
                        return False
        return True

    def xGoingToWin(self, board: [[TTTBoxState]]) -> (int, int):
        # Rows
        rowInd = 0

        selRow = 0
        selBox = 0
        for row in board:
            boxInd = 0
            xCount = 0
            oCount = 0

            for box in row:
                if box == TTTBoxState.X:
                    xCount += 1
                elif box == TTTBoxState.EMPTY:
                    selRow = rowInd
                    selBox = boxInd
                elif box == TTTBoxState.O:
                    oCount
                boxInd += 1
            if xCount == 2 and oCount == 0:
                return selRow, selBox
            rowInd += 1

        # Columns
        boxInd = 0
        selRow = 0
        selBox = 0
        while boxInd < 3:
            rowInd = 0
            xCount = 0
            oCount = 0
            while rowInd < 3:
                box = board[rowInd][boxInd]
                if box == TTTBoxState.X:
                    xCount += 1
                elif box == TTTBoxState.EMPTY:
                    selRow = rowInd
                    selBox = boxInd
                elif box == TTTBoxState.O:
                    oCount
                rowInd += 1
            if xCount == 2 and oCount == 0:
                return selRow, selBox
            boxInd += 1

        # Diagonals
        boxInd = 0
        rowInd = 0
        selRow = 0
        selBox = 0
        xCount = 0
        oCount = 0

        count = 0
        while count < 3:
            rowInd = count
            boxInd = count
            box = board[rowInd][boxInd]
            match box:
                case TTTBoxState.EMPTY:
                    selRow = rowInd
                    selBox = boxInd
                case TTTBoxState.X:
                    xCount += 1
                case TTTBoxState.O:
                    oCount += 1
            count += 1

        if xCount == 2 and oCount == 0:
            return selRow, selBox

        boxInd = 0
        rowInd = 0
        selRow = 0
        selBox = 0
        xCount = 0
        oCount = 0
        count = 0
        while count < 3:
            rowInd = count
            boxInd = 2-count
            box = board[rowInd][boxInd]
            match box:
                case TTTBoxState.EMPTY:
                    selRow = rowInd
                    selBox = boxInd
                case TTTBoxState.X:
                    xCount += 1
                case TTTBoxState.O:
                    oCount += 1
            count += 1

        if xCount == 2 and oCount == 0:
            return selRow, selBox
        else:
            return -1, -1