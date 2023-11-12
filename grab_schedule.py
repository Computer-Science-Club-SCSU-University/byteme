#used to bypass cloudflare bot check, it's a modded version of chromedriver with a little bit different usage
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

#for parsing html
from bs4 import BeautifulSoup

#For opening THE .env file
import os
from dotenv import load_dotenv
# Load the .env file
load_dotenv()
#set variables from .env file
password = os.getenv("PASSWORD")
username = os.getenv("USERNAME")

#undetected_chromedriver as uc application, starts blank browser controlled from this python file
driver = uc.Chrome()

# Create a WebDriverWait instance with a timeout (e.g., 30 seconds)
wait = WebDriverWait(driver, 30)

#from the already started blank Chrome browser navigates to chat GPT website
button_on_page = driver.get("https://eservices.minnstate.edu/esession/authentication.do?campusId=073&postAuthUrl=http%3A%2F%2Feservices.minnstate.edu%2Fstudent-portal%2Fsecure%2Fdashboard.do%3Fcampusid%3D073")

time.sleep(4)

"""button_on_page = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/form/table/tbody/tr[3]/td/select')
button_on_page.click()
time.sleep(4)
button_on_page = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]/form/table/tbody/tr[3]/td/select/option[33]')
button_on_page.click()
time.sleep(4)"""
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
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[4]/a')
button_on_page.click()
move_on = input("Move on 2 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/ul/li[3]/a')
button_on_page.click()
move_on = input("Move on 3 -->")
# Execute a script that will change all elements with 'display: none' to 'display: block'
driver.execute_script("""
var elements = document.querySelectorAll('[style*="display: none"]');
for (var i = 0; i < elements.length; i++) {
  elements[i].style.display = 'block';
}
""")

schedules_text = (driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div')).text
print(schedules_text)
move_on = input("Move on 4 -->")

# Specify the filename
filename = "output.txt"

# Open the file in write mode ('w') and write the string to it
with open(filename, 'w', encoding='utf-8') as file:
    file.write(schedules_text)

# The 'with' block ensures the file is properly closed after writing
print(f"Text has been saved to {filename}")

move_on = input("Move on 5 -->")

