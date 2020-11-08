from quiz import Quiz


class LeveledQuiz(Quiz):
    def __init___(self, questions, threshold_type, threshold):
        super().__init__(questions)
        self.threshold_type = threshold_type
        self.threshold = threshold
