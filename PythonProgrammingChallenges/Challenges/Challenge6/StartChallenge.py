from Challenges.Challenge import Challenge
from Challenges.AnswerKeys import Answer6
from Challenges.Inputs import Input6

challenge = Challenge(
    name="Challenge 6 - Day of the week",
    instr="This challenge inputs a list of dates formatted as yyyy-MM-dd. Its your job to determine the day of the week\n"
          "that that date lands on. The formula to determine the day of the week from any date is as follows:\n\n"
          "(yearCode + monthCode + centuryCode + dayNumber - leapYearCode) % 7 = dayOfTheWeek\n\n"
          "yearCode = ((Last Two Digits of Year) + (Last two Digits of Year / 4)) mod 7\n"
          "monthCode = A set number for each month. There is a function below that returns the month code for\n"
          "    the name of the month. Feel free to use it or design your own. It was just the easiest way to portray the info.\n"
          "centuryCode = take the first two digits of the year. The century code is a repeating pattern of 4, 2, 0, 6 assigned\n"
          "    to each century ascending. I.e. 01 = 4, 02 = 2, 03 = 0, 04 = 6 ... 19 = 0, 20 = 6, etc.\n"
          "dateNumber = the day of the month. I.e for 2024-04-17, it would be 17.\n"
          "leapYearCode = if the year is a leap year and January or February, you need to subtract 1 from your equation, otherwise leave it unchanged.\n"
          "    A year is a leap year if: it is divisible by 4, but NOT if it's also divisible by 100 unless it's ALSO divisible by 400.\n"
          "    For example, the year 2000 is a leap year but 1900 is not.\n"
          "Then, when you have your answer, You can turn that into the day of the week just by knowing that 0=Sunday, 1=Monday ... 6=Saturday.",
    answer=Answer6.ANSWER
)



def getMonthCode(month: str) -> int:
    match month:
        case "jan":
            return 0
        case "feb":
            return 3
        case "mar":
            return 3
        case "apr":
            return 6
        case "may":
            return 1
        case "jun":
            return 4
        case "jul":
            return 6
        case "aug":
            return 2
        case "sep":
            return 5
        case "oct":
            return 0
        case "nov":
            return 3
        case "dec":
            return 5
    return 0

def runChallengeCode() -> str:
    dates = Input6.DATES
    daysOfWeek = []
    #
    # Your Code Starts Here
    #

    # TODO Challenge 6

    #
    # Your Code Ends Here
    #
    return str(daysOfWeek)

def start():
    challenge.printInstructions()
    answerString = runChallengeCode()
    print(challenge.compareAnswer(answerString))
