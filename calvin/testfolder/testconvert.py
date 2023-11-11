import re

def splitAlpha(string):
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


def extractCourseCode(text):
    pattern = re.compile(r"\b[A-Za-z]{3,4}\d{3}\b")
    matches = pattern.findall(text)

    comma_pattern = re.compile(
        r"\b([A-Za-z]{3,4}(?:\s|\d{3}(?:,|\s))\d{3}(?:,\d{3})*)\b"
    )
    matches += comma_pattern.findall(text)

    space_pattern = re.compile(r"\b([A-Za-z]{3,4}\d{3}(?:\s[A-Za-z]{3,4}\d{3})*)\b")
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

    
with open("calvintran.txt", 'r') as file:
    file_contents = file.read()
        
    #CoursesTaken = file_contents.split()

print(extractCourseCode(file_contents))
print(len(extractCourseCode(file_contents)))
print(len(set(extractCourseCode(file_contents))))