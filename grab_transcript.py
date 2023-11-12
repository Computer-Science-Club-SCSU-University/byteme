#used to bypass cloudflare bot check, it's a modded version of chromedriver with a little bit different usage
import base64
import undetected_chromedriver as uc

#used for making whole function pause for a perios of time. Should be replaced by await eventually.
import time

#God bless webscrapers 🙏
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

#for error handling
from selenium.common.exceptions import NoSuchElementException, TimeoutException

#For opening THE .env file
import os
from dotenv import load_dotenv
# Load the .env file
load_dotenv()
#set variables from .env file
password = os.getenv("PASSWORD")
username = os.getenv("USERNAME")

import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = uc.ChromeOptions()

#undetected_chromedriver as uc application, starts blank browser controlled from this python file
driver = uc.Chrome(options=chrome_options)


# Create a WebDriverWait instance with a timeout (e.g., 30 seconds)
wait = WebDriverWait(driver, 30)

#from the already started blank Chrome browser navigates to chat GPT website
button_on_page = driver.get("https://eservices.minnstate.edu/esession/authentication.do?campusId=073&postAuthUrl=http%3A%2F%2Feservices.minnstate.edu%2Fstudent-portal%2Fsecure%2Fdashboard.do%3Fcampusid%3D073")

time.sleep(4)

"""button_on_page = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/form/table/tbody/tr[1]/td/input')
button_on_page.click()
time.sleep(4)
button_on_page = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/form/table/tbody/tr[3]/td/select/option[33]')
button_on_page.click()
time.sleep(4)"""
move_on = input("Move on 0 -->")
try:
    input_field_username = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/form/table/tbody/tr[1]/td/input')
    input_field_password = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/form/table/tbody/tr[2]/td/input')
    input_field_username.send_keys(username)
    input_field_password.send_keys(password)
    button_on_page = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/form/table/tbody/tr[5]/td[2]/input')
    button_on_page.click()
except NoSuchElementException as e:
    print(f"Error: {e}")
    # Handle the exception or pass
    pass
except TimeoutException as e:
    print(f"Page load timed out: {e}")
    pass
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    pass
move_on = input("Move on 1 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[5]/a')
button_on_page.click()
move_on = input("Move on 2 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/ul/li[2]/a')
button_on_page.click()
move_on = input("Move on 3 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div[1]/div/div/form/input[2]')
button_on_page.click()
move_on = input("Move on 4 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div[2]/a/img')
button_on_page.click()

move_on = input("Move on 6 -->")
import os
import glob

folder_path = "C:/Users/kg7481ty/Downloads/"  # Replace with the actual path to your folder

# Get a list of all files in the folder
files = glob.glob(os.path.join(folder_path, "*"))

# Sort the files by modification time (most recent first)
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)


# Check if there are any files in the folder
if files:
    most_recent_file = files[0]
    filepath = most_recent_file.replace("/",f'\\')
    print(filepath)
else:
    print("The folder is empty.")


move_on = input("Move on 7 -->")

# importing required modules 
from PyPDF2 import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader(filepath) 
  
# printing number of pages in pdf file 
pages = int(str(len(reader.pages)))
  
floating_pages = ""
for i in range(pages):
    page = reader.pages[i]
    text = page.extract_text() 
    floating_pages += floating_pages + text

# Define the pattern to search for
pattern = r'xxx-xx-(\d{4})'
# Replace the pattern with 12 asterisks, sanitze SSN
import re
floating_pages = re.sub(pattern, '************', floating_pages)

filename = "transcript.txt"

# Open the file in write mode ('w') and write the string to it
with open(filename, 'w', encoding='utf-8') as file:
    file.write(floating_pages)


move_on = input("Move on 8 -->")