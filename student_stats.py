#!/usr/bin/env pybricks-micropython

import urequests
import json
from pprint import pprint
import math

API_key = 'key4SssZ2nJDuK1KG'
baseID = 'appneqFpKwgcok5kj'
table_name = 'StudentInformation'


def getAll():
    headers = {"Accept": "application/json",
               "Authorization": "Bearer {}".format(API_key)}
    url = 'https://api.airtable.com/v0/' + baseID + '/' + table_name + \
        '?sort%5B0%5D%5Bfield%5D=Name&sort%5B0%5D%5Bdirection%5D=asc'
    response = urequests.get(url, headers=headers)

    if (response.status_code != 200):
        print('ERROR: Status ' + str(response.status_code))

    return response.json()


def insert(fields):
    url = 'https://api.airtable.com/v0/' + baseID + '/' + table_name + '/' + \
        '?sort%5B0%5D%5Bfield%5D=Name&sort%5B0%5D%5Bdirection%5D=asc' + '/'
    headers = {
        "Authorization": "Bearer {}".format(API_key),
        'Content-Type': 'application/json'
    }
    data = {
        "fields": fields,
        "typecast": False
    }

    response = urequests.post(url, headers=headers, json=data)
    if (response.status_code != 200):
        print('ERROR: Status ' + str(response.status_code))


def update(id, fields):
    url = 'https://api.airtable.com/v0/' + baseID + '/' + table_name + '/' + \
        id + '?sort%5B0%5D%5Bfield%5D=Name&sort%5B0%5D%5Bdirection%5D=asc' + '/'
    headers = {
        "Authorization": "Bearer {}".format(API_key),
        'Content-Type': 'application/json'
    }
    data = {
        "fields": fields,
        "typecast": True
    }

    response = urequests.patch(url, headers=headers, json=data)
    if (response.status_code != 200):
        print('ERROR: Status ' + str(response.status_code))


def getStudentStats():
    return getAll()["records"]


def getClassSize():
    student_stats = getStudentStats()
    return len(student_stats)


def createNewStudent(student_name):
    insert({'Name': student_name, 'Status': 'Seeking Approval',
            'Questions Completed': 0, 'Score': 0, 'Average Performance': 0.00, 'Percentile': 0})


def searchStudent(student_name):
    studentStats = getStudentStats()
    for student in studentStats:
        if student["fields"]["Name"] == student_name:
            return student
    print(student_name, "not found")


def getCompletedQuestions(student_name):
    student = searchStudent(student_name)['fields']
    return student['Questions Completed']


def incrementQuestionsCompleted(student_name):
    student = searchStudent(student_name)
    incremented_completed = student['fields']['Questions Completed'] + 1
    fields = {'Questions Completed': incremented_completed}
    update(student['id'], fields)
    return


def getScore(student_name):
    student = searchStudent(student_name)['fields']
    return student['Score']


def incrementScore(student_name):
    student = searchStudent(student_name)
    incremented_score = student['fields']['Score'] + 1
    fields = {'Score': incremented_score}
    update(student['id'], fields)
    return


def getPercentile(student_name):
    student = searchStudent(student_name)['fields']
    return student['Percentile']


def compareVal(s):
    return s['fields']['Average Performance']


def updatePercentile(student_name):
    student = searchStudent(student_name)

    student_stats = getStudentStats()
    class_size = getClassSize()
    first_quarter_idx = math.floor(class_size / 4)
    second_quarter_idx = 2 * first_quarter_idx
    third_quarter_idx = 3 * first_quarter_idx

    student_stats.sort(key=compareVal)
    for i in range(len(student_stats)):
        if student_stats[i]["fields"]["Name"] == student_name:
            if i > third_quarter_idx:
                percentile = .75
            elif i > second_quarter_idx:
                percentile = .50
            elif i > first_quarter_idx:
                percentile = .25
            else:
                percentile = 0
            fields = {'Percentile': percentile}
            update(student['id'], fields)
            break


def getAveragePerformance(student_name):
    student = searchStudent(student_name)['fields']
    return student['Average Performance']


def updateAveragePerformance(student_name):
    student = searchStudent(student_name)
    questions_completed = student['fields']['Questions Completed']
    score = student['fields']['Score']
    fields = {'Average Performance': score / questions_completed}
    update(student['id'], fields)
    return


def getApprovalStatus(student_name):
    student = searchStudent(student_name)['fields']
    return student['Status']


def updateStats(student_name, wasCorrect):
    incrementQuestionsCompleted(student_name)
    if wasCorrect:
        incrementScore(student_name)
    updateAveragePerformance(student_name)
    updatePercentile(student_name)


# pprint(incrementQuestionsCompleted("Student1"))
# pprint(getAll())
# pprint(createNewStudent("Student1"))
updatePercentile("Student3")
