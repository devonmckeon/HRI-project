from question import Question
from pybricks.parameters import Color


class MultipleChoice(Question):
    def __init__(self, text, correct_answer, answer_choices):
        super().__init__(text=text, correct_answer=correct_answer)
        self.answer_choices = answer_choices

    def formatCorrectAnswer(self, correct_answer):
        if correct_answer == "black":
            return Color.BLACK
        elif correct_answer == "red":
            return Color.RED
        elif correct_answer == "blue":
            return Color.BLUE
        elif correct_answer == "green":
            return Color.GREEN
        elif correct_answer == "yellow":
            return Color.YELLOW
        elif correct_answer == "white":
            return Color.WHITE
        elif correct_answer == "brown":
            return Color.BROWN

    def ask(self, ev3):
        ev3.speaker.say(self.text)
        if self.answer_choices["black"]:
            ev3.speaker.say(
                "Show me a black block for " + self.answer_choices["black"])
        if self.answer_choices["red"]:
            ev3.speaker.say(
                "Show me a red block for " + self.answer_choices["red"])
        if self.answer_choices["blue"]:
            ev3.speaker.say(
                "Show me a blue block for " + self.answer_choices["blue"])
        if self.answer_choices["green"]:
            ev3.speaker.say(
                "Show me a green block for " + self.answer_choices["green"])
        if self.answer_choices["yellow"]:
            ev3.speaker.say(
                "Show me a yellow block for " + self.answer_choices["yellow"])
        if self.answer_choices["white"]:
            ev3.speaker.say(
                "Show me a white block for " + self.answer_choices["white"])
        if self.answer_choices["brown"]:
            ev3.speaker.say(
                "Show me a brown block for " + self.answer_choices["brown"])

    def isCorrect(self, sensors):
        color_sensor = sensors["color"]
        while color_sensor.color() == None:
            continue
        print(color_sensor.color())
        if color_sensor.color() == self.f_correct_answer:
            return True
        else:
            return False
