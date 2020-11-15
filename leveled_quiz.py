from quiz import Quiz
from multiple_choice import MultipleChoice
from yes_or_no import YesOrNo
from counting import Counting
from student_stats import updateStats
from student_stats import getAveragePerformance, getApprovalStatus, getPercentile


class LeveledQuiz(Quiz):
    def __init__(self, questions, ev3, sensors, student_name, threshold_type, threshold):
        super().__init__(questions=questions, ev3=ev3, sensors=sensors, student_name=student_name)
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

    def leveled_administer(self, ev3, quest):
        ev3.speaker.say("Let's begin a quiz.")
        checked = False
        i = 0
        for question in self.questions:
            print(quest[i]["difficulty"])
            # Average Performance 
            if (self.threshold_type == "Average_Performance"):
                if (quest[i]["difficulty"] == "Beginner"):
                    question.ask(self.ev3)
                    updateStats(self.student_name, question.isCorrect(self.sensors))
                elif (quest[i]["difficulty"] == "Intermediate"):
                    if (getAveragePerformance(self.student_name) < self.threshold and (checked == False)):
                        ev3.speaker.say("Score is not high enough to keep going")
                        checked == True
                        return "Finished"
                    else:
                        checked = True
                        question.ask(self.ev3)
                        updateStats(self.student_name, question.isCorrect(self.sensors))
                elif (quest[i]["difficulty"] == "Advanced"):
                    if (getAveragePerformance(self.student_name) < self.threshold and (checked == True)):
                        ev3.speaker.say("Score is not high enough to keep going")
                        checked == False
                        return "Finished"
                    else:
                        checked = False
                        question.ask(self.ev3)
                        updateStats(self.student_name, question.isCorrect(self.sensors))
            # Percentile 
            elif (self.threshold_type == "Percentile"):
                if (quest[i]["difficulty"] == "Beginner"):
                    question.ask(self.ev3)
                    updateStats(self.student_name, question.isCorrect(self.sensors))
                elif (quest[i]["difficulty"] == "Intermediate"):
                    if (getPercentile(self.student_name) < self.threshold and (checked == False)):
                        ev3.speaker.say("Score is not high enough to keep going")
                        checked == True
                        return "Finished"
                    else:
                        checked = True
                        question.ask(self.ev3)
                        updateStats(self.student_name, question.isCorrect(self.sensors))
                elif (quest[i]["difficulty"] == "Advanced"):
                    if (getPercentile(self.student_name) < self.threshold and (checked == True)):
                        ev3.speaker.say("Score is not high enough to keep going")
                        checked == False
                        return "Finished"
                    else:
                        checked = False
                        question.ask(self.ev3)
                        updateStats(self.student_name, question.isCorrect(self.sensors))
            # Teacher Approval
            elif (self.threshold_type == "Teacher_Approval"):
                if (quest[i]["difficulty"] == "Beginner"):
                    question.ask(self.ev3)
                    updateStats(self.student_name, question.isCorrect(self.sensors))
                elif (quest[i]["difficulty"] == "Intermediate"):
                    if (getPercentile(self.student_name) < self.threshold and (checked == False)):
                        ev3.speaker.say("Score is not high enough to keep going")
                        checked == True
                        return "Finished"
                    else:
                        checked = True
                        question.ask(self.ev3)
                        updateStats(self.student_name, question.isCorrect(self.sensors))
                elif (quest[i]["difficulty"] == "Advanced"):
                    if (getPercentile(self.student_name) < self.threshold and (checked == True)):
                        ev3.speaker.say("Score is not high enough to keep going")
                        checked == False
                        return "Finished"
                    else:
                        checked = False
                        question.ask(self.ev3)
                        updateStats(self.student_name, question.isCorrect(self.sensors))


            # print(quest[i]["text"])
            
  
            # elif (quest[i]["difficulty"] == "Advanced"):
            #     print(quest[i]["text"])
            # print(question.isCorrect(self.sensors))
            # print(self.threshold)
            # print(self.threshold_type)
            i += 1
            # for q in quest:
            #     if (q["difficulty"] == "Beginner"):
            #         question.ask(self.ev3)
            #         updateStats(self.student_name, question.isCorrect(self.sensors))
            #         print(q["difficulty"])
            #         break
            #     elif (q["difficulty"] == "Intermediate"):
            #         question.ask(self.ev3)
            #         updateStats(self.student_name, question.isCorrect(self.sensors))
            #         print(q["difficulty"])
            #         break
            #     elif (q["difficulty"] == "Advanced"): 
            #         question.ask(self.ev3)
            #         updateStats(self.student_name, question.isCorrect(self.sensors))
            #         print(q["difficulty"])
            #         break


        # for question in self.questions:
        #     for q in questions:
        #         if (q["difficulty"] == "Beginner"):
        #             question.ask(self.ev3)
        #         elif (q["difficulty"] == "Intermediate"):
        #             question.ask(self.ev3)
        #         elif (q["difficulty"] == "Advanced"): 
        #             question.ask(self.ev3)
        #     print(q["difficulty"])

        # for question in self.questions:
        #     question.ask(self.ev3)
                # print(question["difficulty"])
        #     updateStats(self.student_name, question.isCorrect(self.sensors))


