from Challenges.Challenge import Challenge
from Challenges.AnswerKeys import Answer7
from Challenges.Inputs import Input7

challenge = Challenge(
    name="Challenge 7 - Vigenere Cipher",
    instr="This challenge has you encrypting and decrypting phrases using a Vigenere Cipher.\n"
          "A Vigenere Cipher is similar to a Ceaser Cipher but with multiple substitution tables.\n"
          "To start, you are given a table (2 dimensional array) called a Vigenere Table.\n"
          "This table is 26x26 with the entire alphabet contained in each row, but shifted by one each time.\n"
          "(i.e. row 0 goes a, b, c... while row 1 starts b, c, d... row 24 starts with y, z, a...)\n"
          "Each phrase that needs to be encrypted or decrypted will also come with a keyword.\n"
          "This keyword is what you will use to determine which row of the table you will use for your substitution.\n"
          "For an explanation of how these cyphers work, check out https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html\n\n"
          "You are given two Code objects, one with a message to be encrypted and one to be decrypted, along with the keys for both.\n"
          "Do the required operations and then append the result to the answer array.\n"
          "You don't need to split your answer into groups of 5 but you do need to remove all spaces.\n"
          "Good Luck!",
    answer=Answer7.ANSWER
)

def getLetterNumber(num: int) -> str:
    match num:
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
        case 10:
            return "K"
        case 11:
            return "L"
        case 12:
            return "M"
        case 13:
            return "N"
        case 14:
            return "O"
        case 15:
            return "P"
        case 16:
            return "Q"
        case 17:
            return "R"
        case 18:
            return "S"
        case 19:
            return "T"
        case 20:
            return "U"
        case 21:
            return "V"
        case 22:
            return "W"
        case 23:
            return "X"
        case 24:
            return "Y"
        case 25:
            return "Z"
    return ""

def runChallengeCode() -> str:
    # The message and keyword are stored on these objects in variables of the same name.
    codeToEncrypt = Input7.TO_ENCRYPT
    codeToDecrypt = Input7.TO_DERCYPT

    table = Input7.VINGENERE_TABLE

    answerArray = []

    #
    # Your Code Starts Here
    #

    # TODO Challenge 7

    #
    # Your Code Ends Here
    #

    return str(answerArray)

def start():
    challenge.printInstructions()
    answerString = runChallengeCode()
    print(challenge.compareAnswer(answerString))
