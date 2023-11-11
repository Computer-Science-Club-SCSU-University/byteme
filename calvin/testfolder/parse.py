def filter_three_char_items(input_list):
    # Using list comprehension to filter items
    filtered_list = [item for item in input_list if len(item) == 3]
    return filtered_list


filename = "calvintran.txt"  # Replace 'yourfile.txt' with your actual file name

with open(filename, 'r') as file:
    file_contents = file.read()

# Now file_contents holds the entire text from the file

#print(file_contents)

words = file_contents.split()
#print(words)
"""for item in words:
    print(item)"""

#print(words)

#words = filter_three_char_items(words)
"""for item in words:
    print(item)"""


# Correcting the syntax error and completing the list of course names with abbreviations

courses = [
    ["Accounting", "ACCT"],
    ["Anthropology", "ANTH"],
    ["Applied Behavior Analysis", "ABA"],
    ["Applied Clinical Research", "ACR"],
    ["Art", "ART"],
    ["Astronomy", "ASTR"],
    ["Atmospheric & Hydrologic Sciences", "AHS"],
    ["Biochemistry & Molecular Biology", "BMB"],
    ["Biological Sciences", "BIOL"],
    ["British Studies", "BRIT"],
    ["Business Law", "BLAW"],
    ["Chemistry", "CHEM"],
    ["Child and Family Studies", "CFS"],
    ["Chinese", "CHIN"],
    ["College Counseling and Student Development", "CCSD"],
    ["College Experience", "COLL"],
    ["Communication Sciences and Disorders", "CSD"],
    ["Communication Studies", "CMST"],
    ["Community Psychology", "CPSY"],
    ["Community Studies", "CMTY"],
    ["Computer Science", "CSCI"],
    ["Construction Management", "CM"],
    ["Counseling Family Therapy", "COUN"],
    ["Criminal Justice Studies", "CJS"],
    ["Cybersecurity", "CYB"],
    ["Deaf Leadership and Advocacy", "DLA"],
    ["East Asian Studies", "EAST"],
    ["Economics", "ECON"],
    ["Education", "ED"],
    ["Educational Administration", "EDAD"],
    ["Electrical and Computer Engineering", "ECE"],
    ["Engineering Management", "EM"],
    ["English", "ENGL"],
    ["English for Academic Purposes", "EAP"],
    ["Entrepreneurship", "ENTR"],
    ["Environmental Engineering", "ENVE"],
    ["Environmental and Technological Studies", "ETS"],
    ["Ethnic Studies", "ETHS"],
    ["Exercise Science", "EXSC"],
    ["Film Studies", "FS"],
    ["Finance, Insurance and Real Estate", "FIRE"],
    ["French", "FREN"],
    ["Gender and Women's Studies", "GWS"],
    ["General Engineering", "GENG"],
    ["Geography", "GEOG"],
    ["German", "GER"],
    ["Gerontology", "GERO"],
    ["Global Studies", "GLST"],
    ["Health", "HLTH"],
    ["Health Education and Physical Education", "HPE"],
    ["Herberger Business School", "HBS"],
    ["Higher Education Administration", "HIED"],
    ["History", "HIST"],
    ["Honors", "HONS"],
    ["Hospitality and Tourism Planning", "HTSM"],
    ["Human Relations and Multicultural Education", "HURL"],
    ["Information Assurance", "IA"],
    ["Information Media", "IM"],
    ["Information Systems", "IS"],
    ["International Studies", "INTL"],
    ["Japanese", "JPN"],
    ["Jewish Studies", "JWST"],
    ["Languages and Cultures", "LC"],
    ["Learning Resources and Services", "LIB"],
    ["MASTER OF BUSINESS ADMIN.", "MBA"],
    ["Management", "MGMT"],
    ["Manufacturing Engineering Technology", "MFET"],
    ["Marketing and Business Law", "MKTG"],
    ["Marriage and Family Therapy", "MFT"],
    ["Mass Communications", "MCOM"],
    ["Masters in Public Administration", "MPA"],
    ["Mathematics", "MATH"],
    ["Mechanical and Manufacturing Engineering", "MME"],
    ["Medical Laboratory Sciences", "MLS"],
    ["Medical Technology Quality", "MTQ"],
    ["Military Science", "MILS"],
    ["Music Education", "MUSE"],
    ["Music Musicianship", "MUSM"],
    ["Music Performance", "MUSP"],
    ["Nuclear Medicine Technology", "NMDT"],
    ["Nursing", "NURS"],
    ["Philosophy", "PHIL"],
    ["Physical Education Sports Science", "PESS"],
    ["Physics", "PHYS"],
    ["Political Science", "POL"],
    ["Professional Communication", "PCOM"],
    ["Psychology", "PSY"],
    ["Radiologic Technology", "RADT"],
    ["Recreation", "REC"],
    ["Regulatory Affairs and Services", "RAS"],
    ["Rehabilitation Counseling", "RHAB"],
    ["Religious Studies", "REL"],
    ["School Counseling", "SCHL"],
    ["School of the Arts", "SOTA"],
    ["Science", "SCI"],
    ["Science, Technology, Engineering & Math Education", "STEM"],
    ["Social Studies Education", "SSE"],
    ["Social Work", "SW"],
    ["Sociology", "SOC"],
    ["Software Engineering", "SE"],
    ["Spanish", "SPAN"],
    ["Special Education","SPED"],
    ["Statistics", "STAT"], 
    ["Theatre", "TH"],
    ["Traffic Safety Education", "TSE"]]

courses = [
    ["ACCT"],
    ["ANTH"],
    ["ABA"],
    ["ACR"],
    ["ART"],
    ["ASTR"],
    ["AHS"],
    ["BMB"],
    ["BIOL"],
    ["BRIT"],
    ["BLAW"],
    ["CHEM"],
    ["CFS"],
    ["CHIN"],
    ["CCSD"],
    ["COLL"],
    ["CSD"],
    ["CMST"],
    ["CPSY"],
    ["CMTY"],
    ["CSCI"],
    ["CM"],
    ["COUN"],
    ["CJS"],
    ["CYB"],
    ["DLA"],
    ["EAST"],
    ["ECON"],
    ["ED"],
    ["EDAD"],
    ["ECE"],
    ["EM"],
    ["ENGL"],
    ["EAP"],
    ["ENTR"],
    ["ENVE"],
    ["ETS"],
    ["ETHS"],
    ["EXSC"],
    ["FS"],
    ["FIRE"],
    ["FREN"],
    ["GWS"],
    ["GENG"],
    ["GEOG"],
    ["GER"],
    ["GERO"],
    ["GLST"],
    ["HLTH"],
    ["HPE"],
    ["HBS"],
    ["HIED"],
    ["HIST"],
    ["HONS"],
    ["HTSM"],
    ["HURL"],
    ["IA"],
    ["IM"],
    ["IS"],
    ["INTL"],
    ["JPN"],
    ["JWST"],
    ["LC"],
    ["LIB"],
    ["MBA"],
    ["MGMT"],
    ["MFET"],
    ["MKTG"],
    ["MFT"],
    ["MCOM"],
    ["MPA"],
    ["MATH"],
    ["MME"],
    ["MLS"],
    ["MTQ"],
    ["MILS"],
    ["MUSE"],
    ["MUSM"],
    ["MUSP"],
    ["NMDT"],
    ["NURS"],
    ["PHIL"],
    ["PESS"],
    ["PHYS"],
    ["POL"],
    ["PCOM"],
    ["PSY"],
    ["RADT"],
    ["REC"],
    ["RAS"],
    ["RHAB"],
    ["REL"],
    ["SCHL"],
    ["SOTA"],
    ["SCI"],
    ["STEM"],
    ["SSE"],
    ["SW"],
    ["SOC"],
    ["SE"],
    ["SPAN"],
    ["SPED"],
    ["STAT"], 
    ["TH"],
    ["TSE"]]




# Flatten the courses list to include both names and abbreviations
flattened_courses = [item for sublist in courses for item in sublist]

# Optional: Convert to lower case for case-insensitive comparison
flattened_courses_lower = set(course.lower() for course in flattened_courses)

# Filter words list and keep the next item after a match
# Also, ensure that the matching items are all uppercase
filtered_words_with_next = []
for i in range(len(words) - 1):  # Subtract 1 to avoid index out of range on the last item
    word = words[i]
    if word.isupper() and word.lower() in flattened_courses_lower:
        filtered_words_with_next.append(word)  # Add the current item
        filtered_words_with_next.append(words[i + 1])  # Add the next item


print(filtered_words_with_next)

print(len(filtered_words_with_next))

for n in range (0, len(filtered_words_with_next)-1, 2):
    print(filtered_words_with_next[n], filtered_words_with_next[n+1])