class Challenge:
    def __init__(self, name: str, instr: str, answer: str):
        self.name = name
        self.instr = instr
        self.answer = answer

    def printInstructions(self):
        print(f'\n\n----- {self.name} -----\n')
        print(f'📘 START INSTRUCTIONS 📘\n\n{self.instr}\n\n📘 END INSTRUCTIONS 📘')

    def compareAnswer(self, answerString: str) -> str:
        if answerString.strip() == "":
            return "\n\n🟡 Answer String was only whitespace, skipping printout and answer section 🟡"
        else:
            print("\n+++++++++++++ START OF YOUR CODE PRINTOUT +++++++++++++")
            print(answerString)
            print("+++++++++++++ END OF YOUR CODE PRINTOUT +++++++++++++\n")
            if answerString == self.answer:
                return "✅ Your Answer is Correct ✅"
            else:
                return f"❌ Your Answer is Incorrect ❌\nHere's what your answer should look like:\n__________START CORRECT ANSWER__________\n{self.answer}\n__________END CORRECT ANSWER__________\n❌ Your Answer is Incorrect ❌\nScroll up to see the correct answer and further up to see what your code printed out."