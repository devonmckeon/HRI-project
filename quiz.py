from multiple_choice import MultipleChoice
from yes_or_no import YesOrNo
from counting import Counting


class Quiz:
    def __init__(self, questions, ev3, sensors):
        self.questions = self.prepQuestions(questions)
        self.student_score = 0
        self.ev3 = ev3
        self.sensors = sensors

    def prepQuestions(self, questions):
        formatted_questions = []
        for q in questions:
            if q["question_type"] == "multiple_choice":
                formatted_q = MultipleChoice(
                    text=q["text"], correct_answer=q["correct_answer"], answer_choices=q["answer_choices"])
            if q["question_type"] == "yes_or_no":
                formatted_q = YesOrNo(
                    text=q["text"], correct_answer=q["correct_answer"])
            if q["question_type"] == "counting":
                formatted_q = Counting(
                    text=q["text"], correct_answer=q["correct_answer"])
            formatted_questions.append(formatted_q)
        return formatted_questions

    def administer(self, ev3):
        ev3.speaker.say(
            "Let's begin a quiz.")
        for question in self.questions:
            question.ask(self.ev3)
            if question.isCorrect(self.sensors):
                print("correct")
                ev3.speaker.say("That was correct.")
                self.student_score += 1
            else:
                ev3.speaker.say("That was incorrect.")
                print("incorrect")
