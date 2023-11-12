from utils import pipeline
import json

audit = 'C:/Users/kg7481ty/Documents/GitHub/byteme/bytemeUtil/Degree_audit.txt'
transcript = 'C:/Users/kg7481ty/Documents/GitHub/byteme/bytemeUtil/Unofficial_transcript.txt'

with open(audit, 'r') as file:
    auditData = file.readlines()

with open(transcript, 'r') as file:
    transcriptData = file.readlines()

optimalCourseList= json.loads(pipeline(auditData, transcript))
