from .TTTEnums import TTTBoxState

class Checker:

    def __init__(self):
        self.ties = 0
        self.wins = 0
        self.losses = 0

    def checkGame(self, board: [[TTTBoxState]]) -> bool:
        xCount = 0
        oCount = 0
        row = 0
        box = 0

        # Check Rows
        while row < 3:
            xCount = 0
            oCount = 0
            box = 0
            while box < 3:
                match board[row][box]:
                    case TTTBoxState.X:
                        xCount += 1
                    case TTTBoxState.O:
                        oCount += 1
                box += 1
            if xCount == 3:
                self.wins += 1
                return True
            if oCount == 3:
                self.losses += 1
                return True
            row += 1

        row = 0
        box = 0
        # Check Cols
        while box < 3:
            xCount = 0
            oCount = 0
            row = 0
            while row < 3:
                match board[row][box]:
                    case TTTBoxState.X:
                        xCount += 1
                    case TTTBoxState.O:
                        oCount += 1
                row += 1
            if xCount == 3:
                self.wins += 1
                return True
            if oCount == 3:
                self.losses += 1
                return True
            box += 1

        count = 0
        row = 0
        box = 0
        xCount = 0
        oCount = 0
        # Check Diagonals
        while count < 3:
            row = count
            box = count
            match board[row][box]:
                case TTTBoxState.X:
                    xCount += 1
                case TTTBoxState.O:
                    oCount += 1
            count += 1
        if xCount == 3:
            self.wins += 1
            return True
        if oCount == 3:
            self.losses += 1
            return True

        count = 0
        row = 0
        box = 0
        xCount = 0
        oCount = 0
        # Check Diagonals
        while count < 3:
            row = count
            box = 2-count
            match board[row][box]:
                case TTTBoxState.X:
                    xCount += 1
                case TTTBoxState.O:
                    oCount += 1
            count += 1

        if xCount == 3:
            self.wins += 1
            return True
        if oCount == 3:
            self.losses += 1
            return True

        # Check for full board
        for r in board:
            for b in r:
                if b == TTTBoxState.EMPTY:
                    # Still have a place to play
                    return False

        # All boxes full
        self.ties += 1
        return True

