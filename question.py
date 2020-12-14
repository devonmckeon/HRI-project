class Question:
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer
        self.f_correct_answer = self.formatCorrectAnswer(correct_answer)

    def formatCorrectAnswer(self, correct_answer):
        pass

    def ask(self, ev3):
        pass

    def isCorrect(self, sensors):
        pass

    def giveFeedback(self, ev3, robot, is_correct):
        if is_correct:
            ev3.speaker.say("Great job!")
            robot.turn(300)

        else:
            ev3.speaker.say("So close! The right answer was " +
                            str(self.correct_answer))
