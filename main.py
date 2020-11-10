#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from quiz import Quiz

from airtable import get_quizNames
from airtable import get_quizDetails
from pprint import pprint

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

sensors = {"touch": TouchSensor(Port.S4), "color": ColorSensor(Port.S1)}

# Getting list of all quizzes 
list_of_quizzes = get_quizNames()
# Setting form equal to only second 3rd quiz (You can use quiz name directly)
# For example: get_quizDetails(list_of_quizzes["Quiz 1"])
form = get_quizDetails(list_of_quizzes[2])

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
		all_questions["Q" + str(i)] = {
										"text": form["Questions"][i], 
										"question_type": form["Response_Types"][i], 
										"correct_answer": form["Answers"][i],
										"answer_choices": form["Answer_choices"]
										}
	elif (form["Response_Types"][i] == 'yes_or_no'):
		all_questions["Q" + str(i)] = {
										"text": form["Questions"][i], 
										"question_type": form["Response_Types"][i], 
										"correct_answer": form["Answers"][i]
										}
	elif (form["Response_Types"][i] == 'counting'):
		all_questions["Q" + str(i)] = {
										"text": form["Questions"][i],
										"question_type": form["Response_Types"][i],
										"correct_answer": form["Answers"][i]
										}
	# Adding each final Q to questions array
	questions.append(all_questions["Q" + str(i)])

# pprint(all_questions)
# print(questions)

# Create and administer quiz
quiz = Quiz(questions, ev3, sensors)
quiz.administer(ev3)


# answer_choices = {"black": "black", "red": "red", "blue": "blue",
#                   "green": "green", "yellow": "yellow", "white": "white", "brown": "brown"}

# multiple_choice_q = {"text": "What is the best color?", "question_type": "multiple_choice",
#                      "correct_answer": "green", "answer_choices": answer_choices}

# yes_or_no_q = {"text": "Is red the best color?",
#                "question_type": "yes_or_no", "correct_answer": "yes"}

# counting_q = {"text": "What is 2 plus 4?",
#               "question_type": "counting", "correct_answer": 6}

# This array should be filled with questions retrieved from Teacher Survey
# questions = [counting_q, yes_or_no_q, multiple_choice_q]







