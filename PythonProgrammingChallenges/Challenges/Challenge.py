class Challenge:
    def __init__(self, name: str, instr: str, answer: str):
        self.name = name
        self.instr = instr
        self.answer = answer

    @classmethod
    def withRange(cls, name: str, instr: str, answerBottom: float, answerTop: float):
        ch = cls(name, instr, "")
        ch.answerBottom = answerBottom
        ch.answerTop = answerTop
        return ch

    def printInstructions(self):
        print(f'\n\n----- {self.name} -----\n')
        print(f'📘 START INSTRUCTIONS 📘\n\n{self.instr}\n\n📘 END INSTRUCTIONS 📘')

    def compareAnswerWithMarginOfError(self, answerFloat: float) -> str:
        print("\n+++++++++++++ START OF YOUR CODE PRINTOUT +++++++++++++")
        print(answerFloat)
        print("+++++++++++++ END OF YOUR CODE PRINTOUT +++++++++++++\n")
        if self.answerBottom <= answerFloat <= self.answerTop:
            return "✅ Your Answer is Correct ✅"
        else:
            return f"❌ Your Answer is Incorrect ❌\nYour answer should be between the following numbers:\n__________START CORRECT ANSWER__________\nBetween {self.answerBottom} and {self.answerTop}\n__________END CORRECT ANSWER__________\n❌ Your Answer is Incorrect ❌\nScroll up to see the correct answer and further up to see what your code printed out."

    def compareAnswer(self, answerString: str) -> str:
        if answerString.strip() == "":
            return "\n\n🟡 Answer String was only whitespace, skipping printout and answer section 🟡"
        else:
            print("\n+++++++++++++ START OF YOUR CODE PRINTOUT +++++++++++++")
            print(answerString)
            print("+++++++++++++ END OF YOUR CODE PRINTOUT +++++++++++++\n")
            if answerString == self.answer.__str__():
                return "✅ Your Answer is Correct ✅"
            else:
                return f"❌ Your Answer is Incorrect ❌\nHere's what your answer should look like:\n__________START CORRECT ANSWER__________\n{self.answer}\n__________END CORRECT ANSWER__________\n❌ Your Answer is Incorrect ❌\nScroll up to see the correct answer and further up to see what your code printed out."