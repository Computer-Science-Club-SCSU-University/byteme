import json
import re


def findOptimalCourse(courses: dict, goalLeft: list, userNotCompleted: dict):
    """
    This function creates a list of optimal courses according
    to the goal areas hasn't fulfilled in descending order

    :param courses: The json of all courses from the scraper
    :type courses: dict
    :param goalLeft: Goal areas the user needs to fulfill
    :type goalLeft: list
    :return: A json of all the optimal courses the user can take
    :rtype: dict
    """
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


def splitAlpha(string: str):
    """
    This function seperates course abbreviations and codes into seperate lists

    :param string: The string to be seperated
    :type string: str
    :return: The the list of course abbreviations and
    :rtype: dict
    """
    courses = []
    codes = []
    alpha = ""
    integer = ""

    for item in string:
        if item.isalpha():
            alpha += item
        else:
            if alpha:
                courses.append(alpha)
                alpha = ""

            if not (len(integer) >= 3):
                integer += item

            else:
                codes.append(integer)
                integer = item

    if integer and integer not in codes:
        codes.append(integer)

    return {"course": courses, "code": codes}


def extractCourseCode(text: str):
    """
    This function creates a list of optimal courses according
    to the goal areas hasn't fulfilled in descending order

    :param courses: The json of all courses from the scraper
    :type courses: dict
    :param goalLeft: Goal areas the user needs to fulfill
    :type goalLeft: list
    :return: A json of all the optimal courses the user can take
    :rtype: dict
    """
    pattern = re.compile(r"\b[A-Za-z]{2,4}\d{3}\b")
    matches = pattern.findall(text)

    comma_pattern = re.compile(
        r"\b([A-Za-z]{2,4}(?:\s|\d{3}(?:,|\s))\d{3}(?:,\d{3})*)\b"
    )
    matches += comma_pattern.findall(text)

    space_pattern = re.compile(r"\b([A-Za-z]{2,4}\d{3}(?:\s[A-Za-z]{3,4}\d{3})*)\b")
    matches += space_pattern.findall(text)

    parsed = {}

    for item in matches:
        item = item.split()
        item = ",".join(item).split(",")
        item = "".join(item)

        vals = splitAlpha(item)

        courses = vals["course"]
        codes = vals["code"]

        cur = courses[0]

        while courses or codes:
            if courses:
                cur = courses.pop(0)

            if cur in parsed:
                parsed[cur].append(codes.pop(0))
            else:
                parsed[cur] = [codes.pop(0)]

    courselist = set()

    for course, codes in parsed.items():
        for code in codes:
            courselist.add(course + code)

    courselist = list(sorted(courselist))

    return courselist


def extractGoalAreas(text: list):
    """
    This function creates a list of optimal courses according
    to the goal areas hasn't fulfilled in descending order

    :param courses: The json of all courses from the scraper
    :type courses: dict
    :param goalLeft: Goal areas the user needs to fulfill
    :type goalLeft: list
    :return: A json of all the optimal courses the user can take
    :rtype: dict
    """
    pattern_1 = r"GOAL\s*(?P<goal_number>\d+):"
    pattern_2 = r"\(\d+ courses? or experience[s]?\)"
    current = -1

    sortGoalAreas = {"NO": [], "YES": [], "IP": []}
    goalCourses = {}

    for line in text:
        if re.search(pattern_1, line):
            content = line.split()
            current = int(content[2][:-1])
            description = " ".join(content[3:])

            goalCourses[current] = ""

        elif re.search(pattern_2, line):
            description += f" {line.strip()}"

            if content[0] in sortGoalAreas:
                sortGoalAreas[content[0]].append({current: description})
            else:
                sortGoalAreas[content[0]] = [{current: description}]

        elif "UNIVERSITY REQUIREMENTS-DIVERSITY" in line:
            break

        else:
            if current in goalCourses:
                goalCourses[current] += line

    for goals in goalCourses:
        goalCourses[goals] = extractCourseCode(goalCourses[goals])

    return {"Goal-Courses": goalCourses, "Progress-Goal": sortGoalAreas}


def extractCourseGoals(goalCourses: dict, coursesTaken: list):
    """
    This function creates a list of optimal courses according
    to the goal areas hasn't fulfilled in descending order

    :param courses: The json of all courses from the scraper
    :type courses: dict
    :param goalLeft: Goal areas the user needs to fulfill
    :type goalLeft: list
    :return: A json of all the optimal courses the user can take
    :rtype: dict
    """
    courseGoals = {}

    for goal in goalCourses:
        for course in goalCourses[goal]:
            if course in coursesTaken:
                pass
            elif course in courseGoals:
                courseGoals[course].append(goal)
                courseGoals[course] = courseGoals[course]
            else:
                courseGoals[course] = [goal]

    return courseGoals


def pipeline(audit, transcript):
    """
    This function creates a list of optimal courses according
    to the goal areas hasn't fulfilled in descending order

    :param courses: The json of all courses from the scraper
    :type courses: dict
    :param goalLeft: Goal areas the user needs to fulfill
    :type goalLeft: list
    :return: A json of all the optimal courses the user can take
    :rtype: dict
    """
    auditData = extractGoalAreas(audit)
    transcriptData = extractCourseCode(str(transcript))

    courseContents = auditData["Goal-Courses"]

    userNotCompleted = auditData["Progress-Goal"]["NO"]

    goalsLeft = []

    for data in userNotCompleted:
        for key in data:
            goalsLeft.append(key)

    newDict = {}

    for data in userNotCompleted:
        for key, val in data.items():
            newDict[key] = val

    courseGoals = extractCourseGoals(courseContents, transcriptData)

    return findOptimalCourse(courseGoals, goalsLeft, newDict)
