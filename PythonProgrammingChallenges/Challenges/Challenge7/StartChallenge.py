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

def getNumberLetter(letter: str) -> int:
    match letter:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 2
        case "D":
            return 3
        case "E":
            return 4
        case "F":
            return 5
        case "G":
            return 6
        case "H":
            return 7
        case "I":
            return 8
        case "J":
            return 9
        case "K":
            return 10
        case "L":
            return 11
        case "M":
            return 12
        case "N":
            return 13
        case "O":
            return 14
        case "P":
            return 15
        case "Q":
            return 16
        case "R":
            return 17
        case "S":
            return 18
        case "T":
            return 19
        case "U":
            return 20
        case "V":
            return 21
        case "W":
            return 22
        case "X":
            return 23
        case "Y":
            return 24
        case "Z":
            return 25

def messageTrim(message: str) -> str:
    returnString = ""
    for x in message:
        if x != " ":
            returnString += x
        else:
            returnString += ""

    return returnString


def runChallengeCode() -> str:
    # The message and keyword are stored on these objects in variables of the same name.
    codeToEncrypt = Input7.TO_ENCRYPT
    codeToDecrypt = Input7.TO_DECRYPT

    table = Input7.VINGENERE_TABLE

    answerArray = []

    # Your Code Starts Here
    #
    # Let's break this down:

    # ENCRYPT
    # 1) Encrypt is taking letters of a phrase/word string
    # 2) sending it through a translator to turn it into encoded letters
    # 3) printing out the 'gibberish' characters

    # 1) Loop through the array of letters/string, sending each letter through a function to get the number associated w/ the letter
    # 2a) taking the number and, based on the row/placement in the string, adding the difference to get the proper position
    # 2b) take the letter at the position and add it to an array
    # 3) Print/return the answer array.

    passPhraseToEncrypt = messageTrim(str(codeToEncrypt.keyword))
    messageToEncrypt = messageTrim(str(codeToEncrypt.message))

    if len(messageToEncrypt) > len(passPhraseToEncrypt):
        encryptDiff = len(messageToEncrypt) - len(passPhraseToEncrypt)
        x = 0
        while x < encryptDiff:
            passPhraseToEncrypt += passPhraseToEncrypt[x]
            x += 1

    encryptMessage = ""

    a = 0
    while a < len(messageToEncrypt):
        encryptXPos = getNumberLetter(messageToEncrypt[a]) + a
        encryptYPos = getNumberLetter(passPhraseToEncrypt[a])
        if encryptXPos > 25:
            encryptXPos = encryptXPos - 25

        encryptMessage += str(table[encryptXPos][encryptYPos])
        a += 1

    answerArray.append(encryptMessage)


    # DECRYPT
    # 1) Decrypt is taking random letters
    # 2) translating to readable
    # 3) printing out the readable translation

    passPhraseToDecrypt = messageTrim(str(codeToDecrypt.keyword))
    messageToDecrypt = messageTrim(str(codeToDecrypt.message))

    if len(messageToDecrypt) > len(passPhraseToDecrypt):
        lengthDiff = len(messageToDecrypt) - len(passPhraseToDecrypt)
        i = 0
        while i < lengthDiff:
            passPhraseToDecrypt += passPhraseToDecrypt[i]
            i += 1

    answerString = ""

    x = len(messageToDecrypt)

    # TODO This while loop is causing an array out of bounds issue
    # while x > 0:
    #     xPos = getNumberLetter(passPhraseToDecrypt[x]) + x
    #     yPos = getNumberLetter(messageToDecrypt[x])
    #     if xPos > 25:
    #         xPos = xPos - 25
    #
    #     answerString += str(table[xPos][yPos])
    #     x -= 1

    answerArray.append(answerString)

    #
    # Your Code Ends Here
    #
    print(answerArray)
    return str(answerArray)

def start():
    challenge.printInstructions()
    answerString = runChallengeCode()
    print(challenge.compareAnswer(answerString))