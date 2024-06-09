from Challenges.Challenge import Challenge
from Challenges.AnswerKeys import Answer3
from Challenges.Inputs import Input3

challenge = Challenge(
    name="Challenge 3 - Morse Code",
    instr="This challenge inputs a message written in International Morse Code, found here:\n"
          "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/260px-International_Morse_Code.svg.png"
          "\nIt's your job to take message and translate it to english. '.' is used for dot and '-' is used for dash."
          "\nLetters are separated by ' ' and words are separated by ' / '."
          "\n\nFor bonus points, use a function that takes in a morse code letter and returns an english letter."
          "\nRemember, functions in Python need to be defined HIGHER UP in the file than they are used.\n"
          "A 'match' statement would be useful in this function",
    answer=Answer3.ANSWER
)

def morseTranslate(morse) -> str:

    match morse:
        case ".-":
            return "A"
        case "-...":
            return "B"
        case "-.-.":
            return "C"
        case "-..":
            return "D"
        case ".":
            return "E"
        case "..-.":
            return "F"
        case "--.":
            return "G"
        case "....":
            return "H"
        case "..":
            return "I"
        case ".---":
            return "J"
        case "-.-":
            return "K"
        case ".-..":
            return "L"
        case "--":
            return "M"
        case "-.":
            return "N"
        case "---":
            return "O"
        case ".--.":
            return "P"
        case "--.-":
            return "Q"
        case ".-.":
            return "R"
        case "...":
            return "S"
        case "-":
            return "T"
        case "..-":
            return "U"
        case "...-":
            return "V"
        case ".--":
            return "W"
        case "-..-":
            return "X"
        case "-.--":
            return "Y"
        case "--..":
            return "Z"
        case " ":
            return ""
        case "/":
            return " "


# I'm needing to send 26/36 arguments to the morseTranslate function, {just did the letters}
# then for each letter in inputString, translate and append the letters to answerString.

def runChallengeCode() -> str:
    inputString = Input3.INPUT
    answerString = ""
    #
    # Your Code Starts Here
    #
    for i in inputString.split(" "):
        answerString += morseTranslate(i)


    # TODO Challenge 3
    #
    # Your Code Ends Here
    #

    return answerString.strip()

def start():
    challenge.printInstructions()
    answerString = runChallengeCode()
    print(challenge.compareAnswer(answerString))
