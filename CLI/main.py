import requests
import json
from quiz import Quiz

# url for quiz data
questions_url= "https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean"

# get requests to API
response = requests.get(url=questions_url).json()['results']

# instantiating class with the response of above request
obj = Quiz(response)
obj.final_format()