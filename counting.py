from question import Question
import time


class Counting(Question):
    def __init__(self, text, correct_answer):
        super().__init__(text=text, correct_answer=correct_answer)

    def formatCorrectAnswer(self, correct_answer):
        return correct_answer

    def ask(self, ev3):
        ev3.speaker.say(self.text)
        ev3.speaker.say(
            "Give me that many high fives")

    def isCorrect(self, sensors):
        touch_sensor = sensors["touch"]
        presses = 0
        is_pressed = False
        start = time.time()
        while time.time() - start < 10:
            if touch_sensor.pressed():
                if is_pressed == False:
                    presses += 1
                    is_pressed = True
            else:
                is_pressed = False

        if presses == self.correct_answer:
            return True
        else:
            return False
