from quiz import Quiz


class LeveledQuiz(Quiz):
    def __init___(self, questions, ev3, sensors, student_name, threshold_type, threshold):
        super().__init__(questions, ev3, sensors, student_name)
        self.threshold_type = threshold_type
        self.threshold = threshold
        self.questions = self.prepQuestions(questions)

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
            updateStats(self.student_name, question.isCorrect(self.sensors))



# formatted_q = {level: level, question: MultipleChoice(…)} 