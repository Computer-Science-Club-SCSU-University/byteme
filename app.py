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

#undetected_chromedriver as uc application, starts blank browser controlled from this python file
driver = uc.Chrome()

#from the already started blank Chrome browser navigates to chat GPT website
button_on_page = driver.get("https://en.wikipedia.org/wiki/Linus_Torvalds")

time.sleep(4)

button_on_page = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]/a[6]')
button_on_page.click()
time.sleep(4)
# Find all paragraph elements on the page
paragraphs = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[3]')
print("test: ",paragraphs.text)

time.sleep(20)
