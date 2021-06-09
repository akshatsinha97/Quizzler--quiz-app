import requests
import json
from quiz import Quiz
from UI import UI

# url for quiz data
questions_url= "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean"

# get requests to API
response = requests.get(url=questions_url).json()['results']

# instantiating class with the response of above request
obj1 = Quiz(response)
obj2 = UI(obj1)


