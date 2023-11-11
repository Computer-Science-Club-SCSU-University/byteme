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
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[5]/a')
button_on_page.click()
move_on = input("Move on 2 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/ul/li[1]/a')
button_on_page.click()
move_on = input("Move on 3 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/p[3]/strong[1]/a')
button_on_page.click()
move_on = input("Move on 4 -->")
# First, get the current window handle so you can switch back later if needed
original_window = driver.current_window_handle

# Perform the action that opens the new tab
# ...

# Wait for the new tab to open
wait.until(EC.number_of_windows_to_be(2))

# Store all window handles in a list
window_handles = driver.window_handles

# Switch to the new window/tab
for handle in window_handles:
    if handle != original_window:  # If the handle is not the original tab, switch to the new tab
        driver.switch_to.window(handle)
        break
#breaking here
try:
    input_field_username2 = driver.find_element(By.XPATH, '//*[@name="j_username"]') #/html/body/main/div/div/div/form/div[1]/input
    move_on = input("Move on 5 -->")
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
try:
    input_field_password2 = driver.find_element(By.XPATH, '//*[@name="j_password"]') #/html/body/main/div/div/div/form/div[2]/input
    move_on = input("Move on 6 -->")
    input_field_username2.send_keys(username)
    move_on = input("Move on 7 -->")
    input_field_password2.send_keys(password)
    move_on = input("Move on 8 -->")
    button_on_page = driver.find_element(By.XPATH, '/html/body/main/div/div/div/form/div[3]/button')
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
move_on = input("Move on 9 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/select')
button_on_page.click()
move_on = input("Move on 10 -->")
button_on_page = driver.find_element(By.XPATH, '//*[@value="73:Instidq#002377  :Instid#   :Instcd"]')
button_on_page.click()
move_on = input("Move on 11 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/button')
button_on_page.click()
move_on = input("Move on 13 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div[4]/div/p/button')
button_on_page.click()
move_on = input("Move on 14 -->")
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/form[2]/div[2]/table/tbody/tr[3]/td[11]/a')
button_on_page.click()
move_on = input("Move on 15 -->")
#This part will need to be made dynamic to make more robust
button_on_page = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/p[2]/a')
button_on_page.click()
move_on = input("Move on 16 -->")
page_body = (driver.find_element(By.XPATH, '/html/body')).text
print(page_body)
move_on = input("Move on 17 -->")
# Specify the filename
filename = "output.txt"

# Open the file in write mode ('w') and write the string to it
with open(filename, 'w', encoding='utf-8') as file:
    file.write(page_body)

# The 'with' block ensures the file is properly closed after writing
print(f"Text has been saved to {filename}")
move_on = input("Move on 18 -->")
time.sleep(20)
