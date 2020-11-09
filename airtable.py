import requests,json,pygments
from pprint import pprint
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter


API_key = 'key4SssZ2nJDuK1KG'
baseID = 'appneqFpKwgcok5kj'
table_name = 'Teacher Survey'


def getAirtable(API_key, baseID, table_name):
	headers = {"Authorization": "Bearer " + API_key}
	url = 'https://api.airtable.com/v0/' + baseID + "/" + table_name + "?sort%5B0%5D%5Bfield%5D=Name&sort%5B0%5D%5Bdirection%5D=asc"
	response = requests.get(url, headers=headers)

	if (response.status_code != 200):
		print("ERROR: Status " + str(response.status_code))

	return response.json()


def airtable_field(fieldname):
	response = getAirtable(API_key, baseID, table_name)

pprint(getAirtable(API_key, baseID, table_name))



# {'records': [{'createdTime': '2020-11-09T06:11:19.000Z',
#               'fields': {'Confirm': 'I have read and understood the above '
#                                     'statement',
#                          'High Five Follow Up': 'No/False',
#                          'Name': 'Emun',
#                          'Question': 'Is the sky Black? ',
#                          'Quiz settings': 'Standard ',
#                          'What type of response should the robot expect from the student?': 'High '
#                                                                                             'five '
#                                                                                             '(true/false, '
#                                                                                             'yes/no)'},
#               'id': 'recCnHDOBLkBlu4SG'},
#              {'createdTime': '2020-11-09T06:12:41.000Z',
#               'fields': {'Confirm': 'I have read and understood the above '
#                                     'statement',
#                          'Counting follow up': '4',
#                          'Name': 'Emun',
#                          'Question': 'Whats 2 + 2? ',
#                          'Quiz settings': 'Standard ',
#                          'What type of response should the robot expect from the student?': 'Counting '
#                                                                                             '(number '
#                                                                                             '0-10)'},
#               'id': 'recQhka3OfnTDo895'},
#              {'createdTime': '2020-11-09T06:13:57.000Z',
#               'fields': {'Confirm': 'I have read and understood the above '
#                                     'statement',
#                          'Difficulty Level': 'Beginner',
#                          'High Five Follow Up': 'Yes/True',
#                          'Name': 'Sophie ',
#                          'Percentile': 0.25,
#                          'Progression Type': 'Percentile',
#                          'Question': 'Is the sky color blue? ',
#                          'Quiz settings': 'Leveled (students move on to more '
#                                           'difficult questions if they meet a '
#                                           'threshold)',
#                          'What type of response should the robot expect from the student?': 'High '
#                                                                                             'five '
#                                                                                             '(true/false, '
#                                                                                             'yes/no)'},
#               'id': 'recXFWGtuKGxKL6md'},
#              {'createdTime': '2020-11-09T06:10:55.000Z',
#               'fields': {'Colored blocks answers': ['Blue'],
#                          'Colored blocks follow up': 'Black: "Enter text"\n'
#                                                      'Red: "Enter text"\n'
#                                                      'Blue: "Blue"\n'
#                                                      'Green: "Enter text"\n'
#                                                      'Yellow: "Enter text"\n'
#                                                      'White: "Enter text"\n'
#                                                      'Brown: "Enter text"\n',
#                          'Confirm': 'I have read and understood the above '
#                                     'statement',
#                          'Name': 'Emun',
#                          'Question': 'What color is the sky? ',
#                          'Quiz settings': 'Standard ',
#                          'What type of response should the robot expect from the student?': 'Colored '
#                                                                                             'blocks '
#                                                                                             '(multiple '
#                                                                                             'choice)'},
#               'id': 'recaRzsQJxO3ZGi5O'}]}
