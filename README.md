# Byte Me README 
---
###### Made By Calvin Schmeichel for "Byte Me" (Team 5) | SCSU Hackathon Fall 2023

### Table of Contents
---
- [1. Overview](https://github.com/Computer-Science-Club-SCSU-University/byteme/tree/main#1-overview--tldr)
- [2. Introduction](https://github.com/Computer-Science-Club-SCSU-University/byteme/tree/main#2-introduction)
- [3. Demo](https://github.com/Computer-Science-Club-SCSU-University/byteme/tree/main#3-demo)
- [4. Technologies](https://github.com/Computer-Science-Club-SCSU-University/byteme/tree/main#4-technologies)
- [5. Looking Forward](https://github.com/Computer-Science-Club-SCSU-University/byteme/tree/main#5-looking-forward)
- [6. Glossary](https://github.com/Computer-Science-Club-SCSU-University/byteme/tree/main#6-glossary)
- [7. Contributors](https://github.com/Computer-Science-Club-SCSU-University/byteme/tree/main#7-contributors)
### 1. Overview / TLDR
---
- For our Fall 2023 Hackathon Project topic we chose web scrapping.
- All SCSU students have to take General Liberal Education courses. For many finding the right courses to take that make financial sense and are fun and appealing to the student can be hard. So we set out to fix it.
- Our *Solution* is to leverage Web Scraping to gather a students Degree Audit and Unofficial Transcript to figure out what classes the student has completed. To then use **our revolutionary in-house algorithm. Leveraging cutting-edge AI and machine learning techniques, we've crafted a state-of-the-art solution to optimize course schedules.** We then use this algorithm to generate a custom report for the student to help better plan their future semesters.
### 2. Introduction
---
The main problem is the lack of guidance and information of courses available to student's. It's sometimes unclear what classes provide more value to the student or what classes have a less favorable professor.

<p align="center">
  <img src="Hackathon%20Fall%202023%20README%20Resources/SCSU_Liberal_Education_and_Graduation_Requirements.png" alt="Liberal_Education_and_Graduation_Requirements" width="500"/>
</p>
**(Figure 1)** SCSU requires students to take classes from 10 Separate goal areas plus Diversity and Cultural requirements. The university conveniently hosts all of this information on their website. This is the foundation for our web scrapper.

#### Unofficial Transcript Example
##### Student Information
| Name             | John Doe          |
|------------------|-------------------|
| Student ID       | 123456789         |
| Major            | Computer Science  |
| Academic Advisor | Dr. Jane Smith    |
##### Academic Record
| Term       | Course Code | Course Title       | Credits | Grade |
|------------|-------------|--------------------|---------|-------|
| Fall 2019  | CS 101      | Intro to Computing | 4       | A     |
| Fall 2019  | MATH 150    | Calculus I         | 4       | B+    |
| Spring 2020| CS 102      | Data Structures    | 4       | A-    |
| Spring 2020| ENG 101     | English Composition| 3       | B     |
| Fall 2020  | CS 201      | Algorithms         | 4       | B+    |
| Fall 2020  | STAT 200    | Statistics         | 3       | A     |
| Spring 2021| CS 301      | Operating Systems  | 4       | A-    |
| Spring 2021| PHIL 105    | Ethics in Tech     | 3       | B+    |
##### Cumulative Information
| Total Credits Earned | 29    |
|----------------------|-------|
| Cumulative GPA       | 3.55  |

**Note:** This is an unofficial transcript.

#### Product Data Pipeline

*Sketch/Draft*

<p align="center">
  <img src="Hackathon%20Fall%202023%20README%20Resources/HackathonStartStarIDLoginDemo.jpg" alt="Pipeline" width="700"/>
</p>


*Final*

```mermaid

graph TD;
    A["Browser & Username + Password"] --> B["API Request"];
    B --> C["Functions Kickoff"];
    C --> D["Degree Audit Parser"];
    C --> E["Transcript Parser"];
    E --> F["Text Formatter"];
    F --> G["Points Formula"];
    D --> G
    G --> H["API Response"]
    H --> A

```
### 3. Demo
---
#### 1 | Start StarID & Login 
*Sketch/Draft*
<p align="center">
  <img src="Hackathon%20Fall%202023%20README%20Resources/HackathonWebGUIDraft.jpg" alt="WebGUIDraft" width="700"/>
</p>

*Final*

<p align="center">
  <img src="Hackathon%20Fall%202023%20README%20Resources/GUIDEMO.png" alt="GUIDEMO" width="800"/>
</p>


```javascript
// Function to populate the accordion with data
// 
function populateAccordion(data) {
    const accordionContainer = document.getElementById('accordTemplate');

    Object.keys(data).forEach((mainCategory, mainIndex) => {
        let subAccordions = '';
        const mainAccordionId = `collapseMain${mainIndex}`;

        data[mainCategory].forEach((subCategoryObj) => {
            const subCategoryKey = Object.keys(subCategoryObj)[0];
            const subCategoryData = subCategoryObj[subCategoryKey];
            const subAccordionId = `collapseSub${mainIndex}${subCategoryKey.replace(
                /[^a-zA-Z0-9]/g,
                ''
            )}`;

            subAccordions += `
                <div class="accordion-item">
                    <h2 class="accordion-header" id="subHeading${subCategoryKey}${mainIndex}">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${subAccordionId}" aria-expanded="false" aria-controls="${subAccordionId}">
                           ${subCategoryKey}
                        </button>
                    </h2>
                    <div id="${subAccordionId}" class="accordion-collapse collapse" aria-labelledby="subHeading${subCategoryKey}${mainIndex}">
                        <div class="accordion-body">
                            Goal: ${subCategoryData.join(', ')}
                        </div>
                    </div>
                </div>
            `;
        });

        const accordionItem = `
            <div class="accordion-item">
                <h2 class="accordion-header" id="heading${mainIndex}">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${mainAccordionId}" aria-expanded="false" aria-controls="${mainAccordionId}">
                        Goal: ${mainCategory}
                    </button>
                </h2>
                <div id="${mainAccordionId}" class="accordion-collapse collapse" aria-labelledby="heading${mainIndex}">
                    <div class="accordion-body">
                        <div class="accordion" id="subAccordion${mainIndex}${mainCategory}">
                            ${subAccordions}
                        </div>
                    </div>
                </div>
            </div>
        `;

        accordionContainer.innerHTML += accordionItem;
    });
}
```

<p align="center">
  <img src="Hackathon%20Fall%202023%20README%20Resources/WebGUIReportDEMO.gif" alt="WebGUIReportDEMO" width="900"/>
</p>


#### 2 | Audit and Degree Map Scrape

#### grab_audit.py
```python
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
```

#### grab_schedule.py
```python
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
```

#### grab_transcript.py
```python
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
```

#### Demo GIF

<p align="center">
  <img src="Hackathon%20Fall%202023%20README%20Resources/demo.gif" alt="demovideo" width="800"/>
</p>


#### 3 | Data Parser
<p align="center">
  <img src="Hackathon%20Fall%202023%20README%20Resources/HackathonDataParserDraft.jpg" alt="DataParserDraft" width="600"/>
</p>

##### Degree Audit Parser

```python
def findOptimalCourse(courses: dict, goalLeft: list, userNotCompleted: dict):
    hashMap = {}
    res = []

    for course in courses:
        points = 0
        goalFulfill = courses[course]
        for goals in goalLeft:
            if goals in goalFulfill:
                points += 1
        hashMap[course] = points

    hashMap = dict(sorted(hashMap.items(), key=lambda x: x[1], reverse=True))

    for key, val in hashMap.items():
        if val > 0:
            res.append(key)
    for i, key in enumerate(res):
        if key in courses:
            res[i] = {key: courses[key]}
    courseGoal = {}

    for key in res:
        for val in key.values():
            for item in val:
                if item in courseGoal:
                    courseGoal[item].append(key)
                else:
                    courseGoal[item] = [key]

    newDict = {}

    for key in goalLeft:
        newDict[f"{str(key)} {userNotCompleted[key]}"] = courseGoal[key]
    return json.dumps(newDict)
```

-  This function creates a list of optimal courses according to the goal areas hasn't fulfilled in descending order
	- :param courses: The json of all courses from the scraper
	- :type courses: dict
	- :param goalLeft: Goal areas the user needs to fulfill
	- :type goalLeft: list
	- :return: A json of all the optimal courses the user can take
	- :rtype: dict
##### Transcript Parser

```python
def GetDegreeAudit(DegreeAuditFile):
    with open(DegreeAuditFile, 'r') as file:
        file_contents = file.read()   
    CoursesTaken = file_contents.split()
    return(CoursesTaken)
```

- The `GetDegreeAudit` function gets the degree audit file name and opens the file for the program to read and save it to a string. It then splits the data by blank/white space and make a list and returns the saved list to main for further processing.

```python
def GetTakenCourses(CoursesTaken):
	courses = [["CYB"],["CSCI"], ["..."]

    flattened_courses = [item for sublist in courses for item in sublist]
    flattened_courses_lower = set(course.lower() for course in flattened_courses)

    filtered_words_with_next = []

    for i in range(len(CoursesTaken) - 1):
        word = CoursesTaken[i]
        if word.isupper() and word.lower() in flattened_courses_lower:
            filtered_words_with_next.append(word)
            filtered_words_with_next.append(CoursesTaken[i + 1])
    return(filtered_words_with_next)
```

- The `GetTakenCourses` function takes the newly generated list and cleans out all the "Garbage" data from the data scrap we don't need.

```python
def PrintToScreen(filtered_words_with_next):
    
    FinalList = []

    for n in range (0,len(filtered_words_with_next)-1, 2):
        FinalList.append(str(filtered_words_with_next[n])+str(filtered_words_with_next[n+1]))
    return(FinalList)
```

- The `PrintToScreen` function takes the newly cleaned and list and formats the final list in a standardized way for our other pythons scripts to process.
#### 4 | Points System

```python
def findOptimalCourse(courses: dict, goalLeft: list):
    hashMap = {}
    res = []
    for course in courses:
        points = 0
        goalFulfill = courses[course]
        for goals in goalLeft:
            if goals in goalFulfill:
                points += 1
        hashMap[course] = points

    hashMap = dict(sorted(hashMap.items(), key=lambda x: x[1], reverse=True))

    for key, val in hashMap.items():
        if val > 0:
            res.append(key)

    return json.dumps({"optimalCourses": res})
```


The essence of the function can be represented by the equation:

$$O = \max(\sum G_c)$$

Where:

- $O$ Represents the Optimal set of courses.
- $Gc$​ denotes the Goals fulfilled by course $c$.
- The summation $∑Gc$​ sums the goals fulfilled by each course.
- The max⁡ function selects the combination of courses that maximizes the total number of fulfilled goals.
- Once the class scores are fully calculated. The data is exported as a JSON.

#### 5 | Display Data
### 4. Technologies
---
- [Python](https://www.python.org)
- [GitHub](https://github.com)
- [Obsidian](https://obsidian.md)
- Web-Scraping
	- [Undetected Chrome Driver](https://pypi.org/project/undetected-chromedriver/)
	- [Selenium](https://www.selenium.dev/documentation/webdriver/)
	- [Fast API](https://pypi.org/project/fastapi/)
- 
### 5. Looking Forward
---
**Business Aspect**

This product would add great value to students and SCSU as a whole. It would allow students to find more classes they will enjoy for a better value which in return would lead to better student retention at SCSU.

**Feasibility**

- This Product could be implemented directly into D2L or E-Services.
- Long-term we would want to grab this data directly from a database that SCSU host vs scraping the public web.
- In the long run this could be very profitable for the university.

**Future Works & Additions**

- Implement rate my professor to our Points System to add more data points to our generated report.
- Connect our product to e-services to gain access to class start times, dates and semester availability to provide a more detailed generated report.
- Expand our products scope to all Majors that are offered at SCSU. Not just General Liberal Education courses.
- Expand to all courses and implement a questionnaire/chatbot to help students gage what elective courses they might have interest in.
### 6. Glossary
---
- **Web Scrapping**: The process of using bots to extract content and data from a website.
- **API**: Application Programming Interface.
- **Text Parsing/Parser**: Task that separates the given series of text into smaller components based on some rules.
- **GUI**: Graphical User Interface
### 7. Contributors
---
- [Abdinasir Mumin](https://github.com/AbdinasirM)
- [Brendan Chermack](https://github.com/BrendanChermack)
- [Calvin Schemeichel](https://github.com/Calvin-Schmeichel)
- [William Munnich](https://github.com/williammunnich)
- [Joshua Olaoye](https://github.com/joolaoye)
