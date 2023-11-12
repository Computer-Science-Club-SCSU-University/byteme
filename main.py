from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn
from bytemeUtil.utils import pipeline
import json
from grab_audit_copy import degree_audit_return

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with the specific origins allowed to access the API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import datetime
@app.get("/utils")
async def main():  
    
    #await degree_audit_return()
    audit = 'C:/Users/kg7481ty/Documents/GitHub/byteme/bytemeUtil/Degree_audit.txt'
    transcript = 'C:/Users/kg7481ty/Documents/GitHub/byteme/bytemeUtil/Unofficial_transcript.txt'

    with open(audit, 'r') as file:
        auditData = file.readlines()
        #now = datetime.datetime.now()
        #auditData = auditData + str(now)

    with open(transcript, 'r') as file:
        transcriptData = file.readlines()

    optimalCourseList= json.loads(pipeline(auditData, transcript))
    return optimalCourseList

    """file_path = "C:/Users/kg7481ty/Documents/GitHub/byteme/bytemeUtil/Degree_audit.txt"

    with open(file_path, 'r') as file:
        text = file.readlines()

    data = json.loads(pipeline(text))
    return data
    """


if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", port=80, log_level="debug", reload="True")