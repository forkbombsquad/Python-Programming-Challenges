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


def getYearCode(year: int) -> int:
    # yearCode = ((Last Two Digits of Year) + (Last two Digits of Year / 4)) mod 7
    if len(str(year)) > 2:
        last2 = abs(year) % 100
        # TODO this is a problem. You're currently returning: last2 + ((last2 / 4) % 7), because of your order of operations. Also you need to floor it so that there are no decimals, try casting to int before you cast to float.
        return int(float((last2 + (last2 / 4)) % 7))
    else:
        # TODO this is a problem. You're currently returning: year + ((year / 4) % 7), because of your order of operations. Also you need to floor it so that there are no decimals, try casting to int before you cast to float.
        return int((year + (year / 4)) % 7)


def getMonthName(month: str) -> str:
    match month:
        case "01":
            return "jan"
        case "02":
            return "feb"
        case "03":
            return "mar"
        case "04":
            return "apr"
        case "05":
            return "may"
        case "06":
            return "jun"
        case "07":
            return "jul"
        case "08":
            return "aug"
        case "09":
            return "sep"
        case "10":
            return "oct"
        case "11":
            return "nov"
        case "12":
            return "dec"


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


def centuryCode(year: int) -> int:
    # centuryCode = take the first two digits of the year. The century code is a repeating pattern of 4, 2, 0, 6 assigned
    # to each century ascending. I.e. 01 = 4, 02 = 2, 03 = 0, 04 = 6 ... 19 = 0, 20 = 6, etc.
    centuryPattern = [4, 2, 0, 6]
    first2 = str(year)[:2]
    first2 = float(first2)
    # check if the first2 are 4, 2, 0 or 6 by running them through an equation
    index = int(first2 % 4)
    index = index - 1
    return centuryPattern[index]


    # doing a match-case instead, to make sure my further equation is working
    """    match first2:
        case "01":
            return 4
        case "02":
            return 2
        case "03":
            return 0
        case "04":
            return 6
        case "05":
            return 4
        case "06":
            return 2
        case "07":
            return 0
        case "08":
            return 6
        case "09":
            return 4
        case "10":
            return 2
        case "11":
            return 0
        case "12":
            return 6
        case "13":
            return 4
        case "14":
            return 2
        case "15":
            return 0
        case "16":
            return 6
        case "17":
            return 4
        case "18":
            return 2
        case "19":
            return 0
        case "20":
            return 6
        case "21":
            return 4
        case "22":
            return 2
        case "23":
            return 0
        case "24":
            return 6"""


def leapYearCode(year: int, month: str) -> int:
    # leapYearCode = if the year is a leap year, you need to subtract 1 from your equation, otherwise leave it unchanged
    # A year is a leap year if: it is divisible by 4, but NOT if it's also divisible by 100 unless it's ALSO divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if month == "jan" or month == "feb":
            return 1
        else:
            return 0
    else:
        return 0


def getDayName(dayCode: int) -> str:
    match dayCode:
        case 0:
            return "Sunday"
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"


def runChallengeCode() -> str:
    dates = Input6.DATES
    daysOfWeek = []
    #
    # Your Code Starts Here
    #
    # (yearCode + monthCode + centuryCode + dayNumber - leapYearCode) % 7 = dayOfTheWeek
    i = 0
    while i < len(dates):
        brokenDate = str(dates[i]).split("-")
        year = int(brokenDate[0])
        month = getMonthName(brokenDate[1])
        day = int(brokenDate[2])
        dayOfTheWeek = ((getYearCode(year) + getMonthCode(month) + centuryCode(year) + day - leapYearCode(year, month)) % 7)
        daysOfWeek.append(getDayName(int(dayOfTheWeek)))
        i += 1

    # TODO Challenge 6

    #
    # Your Code Ends Here
    #
    return str(daysOfWeek)


def start():
    challenge.printInstructions()
    answerString = runChallengeCode()
    print(challenge.compareAnswer(answerString))
