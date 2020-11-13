#!/usr/bin/env pybricks-micropython

import urequests
import json
from pprint import pprint


API_key = 'key4SssZ2nJDuK1KG'
baseID = 'appneqFpKwgcok5kj'
table_name = 'TeacherSurvey'


def getAirtable(API_key, baseID, table_name):
    headers = {'Authorization': 'Bearer ' + API_key}
    url = 'https://api.airtable.com/v0/' + baseID + '/' + table_name + \
        '?sort%5B0%5D%5Bfield%5D=Name&sort%5B0%5D%5Bdirection%5D=asc'
    response = urequests.get(url, headers=headers)

    if (response.status_code != 200):
        print('ERROR: Status ' + str(response.status_code))

    return response.json()


def get_quizNames():
    response = getAirtable(API_key, baseID, table_name)
    arr = []

    # Append the first quiz to empty array
    arr.append(response['records'][0]['fields']['Name'])

    for i in range(1, len(response['records'])):
        if (arr[len(arr)-1] != response['records'][i]['fields']['Name']):
            arr.append(response['records'][i]['fields']['Name'])

    return arr

# At first the string will be splitted
# at the occurence of ';' to divide items
# for the dictionaryand then again splitting
# will be done at occurence of '=' which
# generates key:value pair for each item
# dictionary = dict(subString.split("=") for subString in str.split(";"))


def ac_to_dictionary(convert):
    # convert = "{" + convert + "}"
    # convert = 'black = test3\n''red = test4\n''blue = test5\n''green = test6\n''yellow = test7\n''white = test8\n''brown = test9'
    convert = convert.strip()
    convert = convert.replace(" ", "")

    dictionary = dict(subString.split(":")
                      for subString in convert.split("\n"))
    return dictionary


def get_quizDetails(quiz_name):
    response = getAirtable(API_key, baseID, table_name)

    Quiz_Setting = None  # single value
    Questions = []  # Holds all the quiz questions
    Response_Types = []  # Holds all the response types
    Difficulty_Level = []  # Holds all diffculty levels of leveled questions
    Progression_Type = None  # single value
    Average_Performance = None  # single value
    Percentile = None  # single value
    Teacher_Aproval = None  # single value
    Answer_choices = None
    Answers = []  # Holds all answers to all questions

    for i in range(0, len(response['records'])):
        if (quiz_name == response['records'][i]['fields']['Name']):
            Quiz_Setting = response['records'][i]['fields']['Quiz settings']
            Questions.append(response['records'][i]['fields']['Question'])

            if (response['records'][i]['fields']['Response Type'] == 'High five (yes/no)'):
                Response_Types.append('yes_or_no')
            elif (response['records'][i]['fields']['Response Type'] == 'Counting (number 0-10)'):
                Response_Types.append('counting')
            elif (response['records'][i]['fields']['Response Type'] == 'Colored blocks (multiple choice)'):
                Response_Types.append('multiple_choice')

            # Getting all answers
            if (response['records'][i]['fields']['Response Type'] == 'High five (yes/no)'):
                Answers.append(
                    (response['records'][i]['fields']['High Five answer']).lower())
            elif (response['records'][i]['fields']['Response Type'] == 'Counting (number 0-10)'):
                Answers.append(
                    int(response['records'][i]['fields']['Counting answer']))
            else:
                # First slot is answer, second slot are each colors' meaning (aka Color follow up)
                # The second slot contains '\n' which can be used to parse it
                Answers.append(
                    (response['records'][i]['fields']['Colored blocks answers']).lower())
                # pair = [
                # 			(response['records'][i]['fields']['Colored blocks answers']).lower(),
                # 			(response['records'][i]['fields']['Colored blocks follow up']).lower()
                # 		]
                Answer_choices = ac_to_dictionary(
                    (response['records'][i]['fields']['Colored blocks follow up']).lower())
                # Answers.append(pair)

            # If Quiz is in Leveled mode, obtain necessary values
            if (Quiz_Setting != 'Standard'):
                Difficulty_Level.append(
                    response['records'][i]['fields']['Difficulty Level'])
                Progression_Type = response['records'][i]['fields']['Progression Type']
                if (Progression_Type == 'Percentile'):
                    Percentile = response['records'][i]['fields']['Percentile']
                elif (Progression_Type != 'Percentile' and Progression_Type != 'Teacher Approval'):
                    Average_Performance = response['records'][i]['fields']['Average Performance']
                else:
                    Teacher_Aproval = True

    Quiz = {
        'Quiz_Setting': Quiz_Setting,
        'Questions': Questions,
        'Response_Types': Response_Types,
        'Difficulty_Level': Difficulty_Level,
        'Progression_Type': Progression_Type,
        'Average_Performance': Average_Performance,
        'Percentile': Percentile,
        'Teacher_Aproval': Teacher_Aproval,
        'Answer_choices': Answer_choices,
        'Answers': Answers
    }
    return Quiz


# pprint(getAirtable(API_key, baseID, table_name))
