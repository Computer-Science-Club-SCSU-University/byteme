"""
This file contain a function that creates a list of optimal courses user can take

:Author: Joshua O. Olaoye
"""

from json import dumps

def findOptimalCourse(courses : dict, goalLeft : list):
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
        goalFulfill = courses[course]["goal"]

        for goals in goalLeft:
            if goals in goalFulfill:
                points += 1

        hashMap[course] = points

    hashMap = dict(sorted(hashMap.items(), key= lambda x: x[1], reverse=True))

    for key, val in hashMap.items():
        if val > 0:
            res.append(key)

    return dumps({"optimalCourses": res})