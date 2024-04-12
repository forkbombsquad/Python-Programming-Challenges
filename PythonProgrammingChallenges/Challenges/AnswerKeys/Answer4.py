ANSWER = "A| O O O O O O O O O O\n" \
         "B| O O O O O O O O O O\n" \
         "C| O O X X O O X X O O\n" \
         "D| O O X X O O X X O O\n" \
         "E| O O O O O O O O O O\n" \
         "F| O X X O O O O X X O\n" \
         "G| O O X X O O X X O O\n" \
         "H| O O O X X X X O O O\n" \
         "I| O O O O X X O O O O\n" \
         "J| O O O O O O O O O O\n" \
         "-| - - - - - - - - - -\n" \
         "-| O 1 2 3 4 5 6 7 8 9"

def getLetterForNumber(number: int) -> str:
    match number:
        case 0:
            return "A"
        case 1:
            return "B"
        case 2:
            return "C"
        case 3:
            return "D"
        case 4:
            return "E"
        case 5:
            return "F"
        case 6:
            return "G"
        case 7:
            return "H"
        case 8:
            return "I"
        case 9:
            return "J"
    return ""

def formatAnswerGrid(grid: [[]]) -> str:
    yIndex = 0
    formattedAnswer = ""
    for y in grid:
        formattedAnswer += f'{getLetterForNumber(yIndex)}| {str(y).replace("[", "").replace("]", "").replace(",", "")}\n'
        yIndex += 1
    formattedAnswer += "-| - - - - - - - - - -\n-| O 1 2 3 4 5 6 7 8 9"
    return formattedAnswer.replace("'", "")