from Challenges.Challenge import Challenge
from Challenges.AnswerKeys import Answer1

challenge = Challenge(
    name="Challenge 1 - FizzBuzz",
    instr="This challenge will loop through the numbers 1-100. As each number passes you will add a line to the answerString. For normal numbers, you simply need to add the number to the output string but there are exceptions:"
          "\nException 1: For numbers divisible by 3, you should add FIZZ to the answerString instead of the number. "
          "\nException 2: For numbers divisible by 5, you should add Buzz to the answerString instead of the number. "
          "\nException 3: For numbers divisible by both 3 and 5, you should add FIZZBUZZ to the answerString instead of the number."
          "\nTry to keep your answer under 10 lines of code.",
    answer=Answer1.ANSWER
)

def runChallengeCode() -> str:
    answerString = ""
    currentNumber = 1
    while currentNumber <= 100:
        #
        # Your Code Starts Here
        #

        # TODO Challenge 1

        #
        # Your Code Ends Here
        #
        currentNumber += 1
        if currentNumber < 101:
            answerString += "\n"
    return answerString

def start():
    challenge.printInstructions()
    answerString = runChallengeCode()
    print(challenge.compareAnswer(answerString))
