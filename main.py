#!/usr/bin/env pybricks-micropython

from pprint import pprint
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from quiz import Quiz
from leveled_quiz import LeveledQuiz

from teacher_survey import get_quizNames
from teacher_survey import get_quizDetails
from student_stats import createNewStudent

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

student_name = "Student1"
sensors = {"touch": TouchSensor(Port.S4), "color": ColorSensor(Port.S1)}

# Getting list of all quizzes
list_of_quizzes = get_quizNames()
# Setting form equal to only second 3rd quiz (You can use quiz name directly)
# For example: get_quizDetails(list_of_quizzes["Quiz 1"])
form = get_quizDetails(list_of_quizzes[1])

# print(list_of_quizzes)
# pprint(form)

# Dictionary to hold all Q's
all_questions = {}
# Array to hold finalized questions
questions = []
for i in range(len(form['Questions'])):
    # Creating all Q variables
    all_questions["Q{0}".format(i)] = None
    # Setting each Q equal to proper format
    if (form["Response_Types"][i] == 'multiple_choice'):
        if (form["Quiz_Setting"] != "Standard"):
            all_questions["Q" + str(i)] = {
                "text": form["Questions"][i],
                "question_type": form["Response_Types"][i],
                "correct_answer": form["Answers"][i],
                "answer_choices": form["Answer_choices"],
                "difficulty": form["Difficulty_Level"][i]
            }
<< << << < Updated upstream
        else:
== == == =
        else:
>>>>>> > Stashed changes
            all_questions["Q" + str(i)] = {
                "text": form["Questions"][i],
                "question_type": form["Response_Types"][i],
                "correct_answer": form["Answers"][i],
                "answer_choices": form["Answer_choices"]
            }
    elif (form["Response_Types"][i] == 'yes_or_no'):
        if (form["Quiz_Setting"] != "Standard"):
            all_questions["Q" + str(i)] = {
                "text": form["Questions"][i],
                "question_type": form["Response_Types"][i],
                "correct_answer": form["Answers"][i],
                "difficulty": form["Difficulty_Level"][i]
            }
        else:
            all_questions["Q" + str(i)] = {
                "text": form["Questions"][i],
                "question_type": form["Response_Types"][i],
                "correct_answer": form["Answers"][i]
            }
    elif (form["Response_Types"][i] == 'counting'):
        if (form["Quiz_Setting"] != "Standard"):
            all_questions["Q" + str(i)] = {
                "text": form["Questions"][i],
                "question_type": form["Response_Types"][i],
                "correct_answer": form["Answers"][i],
                "difficulty": form["Difficulty_Level"][i]
            }
        else:
            all_questions["Q" + str(i)] = {
                "text": form["Questions"][i],
                "question_type": form["Response_Types"][i],
                "correct_answer": form["Answers"][i]
            }
    # Adding each final Q to questions array
    questions.append(all_questions["Q" + str(i)])

# pprint(all_questions)
# print(questions)

createNewStudent(student_name)

# Create and administer quiz
# print(type(form["Quiz_Setting"]))
if (form["Quiz_Setting"] == "Standard"):
    quiz = Quiz(questions, ev3, sensors, student_name) 
    quiz.administer(ev3)
else: 
    if (form["Progression_Type"] == "Average Performance (correct / total questions) in current level"):
        threshold_type = "Average_Performance"
        threshold = form["Average_Performance"]
    elif (form["Progression_Type"] == "Teacher Approval"):
        threshold_type = "Teacher_Approval"
        threshold = "Teacher_Approval"
    else:
        threshold_type = "Percentile"
        threshold = form["Percentile"]
        threshold = (float(threshold.strip('%')))/100
    # print(threshold_type)
    # print(threshold)
    quiz = LeveledQuiz(questions, ev3, sensors,
                       student_name, threshold_type, threshold)
    quiz.leveled_administer(ev3, questions)
