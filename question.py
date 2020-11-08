class Question:
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = self.formatCorrectAnswer(correct_answer)

    def formatCorrectAnswer(self, correct_answer):
        pass

    def ask(self, ev3):
        pass

    def isCorrect(self, sensors):
        pass
