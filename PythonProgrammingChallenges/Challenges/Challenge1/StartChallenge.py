from Challenges.Challenge import Challenge
from Challenges.AnswerKeys import Answer1

challenge = Challenge(
    name="Challenge 1 - FizzBuzz",
    instr="This challenge will loop through the numbers 1-100. As each number passes you will add a line to the answerString."
          "\nFor normal numbers, you simply need to add the number to the answerString but there are exceptions:"
          "\n\nException 1: For numbers divisible by 3, you should add FIZZ to the answerString instead of the number. "
          "\nException 2: For numbers divisible by 5, you should add BUZZ to the answerString instead of the number. "
          "\nException 3: For numbers divisible by both 3 and 5, you should add FIZZBUZZ to the answerString instead of the number."
          "\n\nFor bonus points, see if you can finish this challenge in 6 lines of code or less!",
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
    print(challenge.compareAnswer(answerString, ""))
