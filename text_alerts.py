#!/usr/bin/env pybricks-micropython

import urequests

API_key = 'key4SssZ2nJDuK1KG'
baseID = 'appneqFpKwgcok5kj'
table_name = 'TwilioAlerts'


def sendAlert(student_name, to_number, body):
    url = 'https://api.airtable.com/v0/' + baseID + '/' + table_name + '/' + \
        '?sort%5B0%5D%5Bfield%5D=Name&sort%5B0%5D%5Bdirection%5D=asc' + '/'
    headers = {
        "Authorization": "Bearer {}".format(API_key),
        'Content-Type': 'application/json'
    }
    data = {
        "fields": {"Name": student_name, "To Phone Number": to_number, "Body": body},
        "typecast": False
    }

    response = urequests.post(url, headers=headers, json=data)
    if (response.status_code != 200):
        print('ERROR: Status ' + str(response.status_code))


def alertSeekingApproval(student_name, to_number):
    body = student_name + " is seeking approval to progress to the next level! Please update their approval status within the AirTable."
    sendAlert(student_name, to_number, body)


def alertThresholdNotMet(student_name, to_number):
    body = student_name + " did not meet the threshold to progress to the next level. To override and allow them to progress, update their approval status within the AirTable."
    sendAlert(student_name, to_number, body)


# alertSeekingApproval("Student2", "19085688885")
# alertThresholdNotMet("Student2", "19085688885")
