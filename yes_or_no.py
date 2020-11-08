from question import Question
import time


class YesOrNo(Question):
    def __init__(self, text, correct_answer):
        super().__init__(text=text, correct_answer=correct_answer)

    def formatCorrectAnswer(self, correct_answer):
        if correct_answer == "yes":
            return 1
        else:
            return 2

    def ask(self, ev3):
        ev3.speaker.say(self.text)
        ev3.speaker.say(
            "Give me one high five for Yes")
        ev3.speaker.say("Give me two high fives for No")

    def isCorrect(self, sensors):
        touch_sensor = sensors["touch"]
        presses = 0
        is_pressed = False
        start = time.time()
        while time.time() - start < 5:
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
