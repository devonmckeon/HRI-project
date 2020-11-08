#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from quiz import Quiz


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

sensors = {"touch": TouchSensor(Port.S4), "color": ColorSensor(Port.S1)}

# Sample Inputs

answer_choices = {"black": "black", "red": "red", "blue": "blue",
                  "green": "green", "yellow": "yellow", "white": "white", "brown": "brown"}

multiple_choice_q = {"text": "What is the best color?", "question_type": "multiple_choice",
                     "correct_answer": "green", "answer_choices": answer_choices}

yes_or_no_q = {"text": "Is red the best color?",
               "question_type": "yes_or_no", "correct_answer": "yes"}

counting_q = {"text": "What is 2 plus 4?",
              "question_type": "counting", "correct_answer": 6}

# This array should be filled with questions retrieved from Teacher Survey
questions = [counting_q, yes_or_no_q, multiple_choice_q]

# Create and administer quiz
quiz = Quiz(questions, ev3, sensors)
quiz.administer(ev3)
