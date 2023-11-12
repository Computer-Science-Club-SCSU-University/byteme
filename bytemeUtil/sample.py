from utils import pipeline
import json

audit = 'Degree Audit.txt'
transcript = 'Unofficial transcript.txt'

with open(audit, 'r') as file:
    auditData = file.readlines()

with open(transcript, 'r') as file:
    transcriptData = file.readlines()

return json.loads(pipeline(auditData, transcriptData))
