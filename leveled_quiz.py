from quiz import Quiz
import time
from multiple_choice import MultipleChoice
from yes_or_no import YesOrNo
from counting import Counting
from student_stats import getAveragePerformance, getApprovalStatus, getPercentile, updateStats, updateApprovalStatus
from text_alerts import alertThresholdNotMet, alertSeekingApproval


class LeveledQuiz(Quiz):
    def __init__(self, questions, ev3, sensors, student_name, threshold_type, threshold):
        super().__init__(questions=questions, ev3=ev3,
                         sensors=sensors, student_name=student_name)
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

    def leveled_administer(self, ev3, quest, phone_number):
        ev3.speaker.say("Let's begin a quiz.")
        checked = False
        i = 0
        for question in self.questions:
            print(quest[i]["difficulty"])
            # Average Performance and Percentile
            if (self.threshold_type == "Average_Performance" or self.threshold_type == "Percentile"):
                if (quest[i]["difficulty"] == "Intermediate"):
                    if ((getAveragePerformance(self.student_name) < self.threshold and (checked == False)) 
                            or (getPercentile(self.student_name) < self.threshold and (checked == False))):
                        alertThresholdNotMet(self.student_name, phone_number)
                        updateApprovalStatus(self.student_name, "Seeking Approval")
                        ev3.speaker.say("Score is not high enough to keep going")
                        while (getApprovalStatus(self.student_name) == "Seeking Approval"):
                            ev3.speaker.say("Waiting for teacher")
                            time.sleep(5)
                    checked = True
                    if (getApprovalStatus(self.student_name) == "Denied"):
                        ev3.speaker.say("Quiz is finished")
                        return "Finished"
                elif (quest[i]["difficulty"] == "Advanced"):
                    if ((getAveragePerformance(self.student_name) < self.threshold and (checked == True))
                            or (getPercentile(self.student_name) < self.threshold and (checked == True))):
                        alertThresholdNotMet(self.student_name, phone_number)
                        updateApprovalStatus(self.student_name, "Seeking Approval")
                        ev3.speaker.say("Score is not high enough to keep going")
                        while (getApprovalStatus(self.student_name) == "Seeking Approval"):
                            ev3.speaker.say("Waiting for teacher")
                            time.sleep(5)
                    checked = False
                    if (getApprovalStatus(self.student_name) == "Denied"):
                        ev3.speaker.say("Quiz is finished")
                        return "Finished"
            # Teacher Approval
            elif (self.threshold_type == "Teacher_Approval"):
                if (quest[i]["difficulty"] == "Intermediate"):
                    alertSeekingApproval(self.student_name, phone_number)
                    updateApprovalStatus(self.student_name, "Seeking Approval")
                    while (getApprovalStatus(self.student_name) == "Seeking Approval" and checked == False):
                        ev3.speaker.say("Waiting for teacher")
                        time.sleep(5)
                    checked = True
                    if (getApprovalStatus(self.student_name) == "Denied"):
                        ev3.speaker.say("Quiz is finished")
                        return "Finished"
                elif (quest[i]["difficulty"] == "Advanced"):
                    alertSeekingApproval(self.student_name, phone_number)
                    updateApprovalStatus(self.student_name, "Seeking Approval")
                    while (getApprovalStatus(self.student_name) == "Seeking Approval" and checked == True):
                        ev3.speaker.say("Waiting for teacher")
                        time.sleep(5)
                    checked = False
                    if (getApprovalStatus(self.student_name) == "Denied"):
                        ev3.speaker.say("Quiz is finished")
                        return "Finished"
            question.ask(self.ev3)
            updateStats(self.student_name, question.isCorrect(self.sensors))
            i += 1