from utils import pipeline
import json

file_path = 'Degree Audit.txt'

with open(file_path, 'r') as file:
    text = file.readlines()

optimalCourseList = json.loads(pipeline(text))

