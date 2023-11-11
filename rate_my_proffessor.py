import ratemyprofessor
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

def getFullListOfTeachers():
    #undetected_chromedriver as uc application, starts blank browser controlled from this python file
    driver = uc.Chrome()
    #from the already started blank Chrome browser navigates to chat GPT website
    button_on_page = driver.get("https://www.ratemyprofessors.com/search/professors/833?q=*")
    while True:
        move_on = input("Move on 4 -->")
        time.sleep(3)
        button_on_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[4]/button')
        button_on_page.click()
    

def getProfessorsTeachClass(the_class):
    return the_class

def getProffessorRatingByClass(the_professor):
    professor = ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("St. Cloud State University"), str(the_professor))
    if professor is not None:
        print("%sworks in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
        print("Overal Rating: %s / 5.0" % professor.rating)
        print("Overall Difficulty: %s / 5.0" % professor.difficulty)
        print("Total Ratings: %s" % professor.num_ratings)
        if professor.would_take_again is not None:
            print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
        else:
            print("Would Take Again: N/A")
        teacher_ratings = professor.get_ratings()
        for rate in teacher_ratings:
            print(" Class: " + str(rate.class_name) + " ---> Rating: " + str(rate.rating))
    else:
        print("Professor %s not found" % (str(the_professor)))

"""professor = ratemyprofessor.get_professor_by_schools_and_name(ratemyprofessor.get_school_by_name("St. Cloud State University"), "")
print(professor)
getProffessorRatingByClass("petzold")"""

getFullListOfTeachers()

