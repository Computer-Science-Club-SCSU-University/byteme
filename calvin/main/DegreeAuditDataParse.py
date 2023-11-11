def GetDegreeAudit(DegreeAutiFile):
    
    with open(DegreeAutiFile, 'r') as file:
        file_contents = file.read()
        
    CoursesTaken = file_contents.split()

    return(CoursesTaken)


def GetTakenCourses(CoursesTaken):
    courses = [["ACCT"],["ANTH"],["ABA"],["ACR"],["ART"],["ASTR"],["AHS"],["BMB"],["BIOL"],["BRIT"],["BLAW"],["CHEM"],["CFS"],["CHIN"],["CCSD"],["COLL"],["CSD"],["CMST"],["CPSY"],["CMTY"],["CSCI"],["CM"],["COUN"],["CJS"],["CYB"],["DLA"],["EAST"],["ECON"],["ED"],["EDAD"],["ECE"],["EM"],["ENGL"],["EAP"],["ENTR"],["ENVE"],["ETS"],["ETHS"],["EXSC"],["FS"],["FIRE"],["FREN"],["GWS"],["GENG"],["GEOG"],["GER"],["GERO"],["GLST"],["HLTH"],["HPE"],["HBS"],["HIED"],["HIST"],["HONS"],["HTSM"],["HURL"],["IA"],["IM"],["IS"],["INTL"],["JPN"],["JWST"],["LC"],["LIB"],["MBA"],["MGMT"],["MFET"],["MKTG"],["MFT"],["MCOM"],["MPA"],["MATH"],["MME"],["MLS"],["MTQ"],["MILS"],["MUSE"],["MUSM"],["MUSP"],["NMDT"],["NURS"],["PHIL"],["PESS"],["PHYS"],["POL"],["PCOM"],["PSY"],["RADT"],["REC"],["RAS"],["RHAB"],["REL"],["SCHL"],["SOTA"],["SCI"],["STEM"],["SSE"],["SW"],["SOC"],["SE"],["SPAN"],["SPED"],["STAT"], ["TH"],["TSE"]]

    flattened_courses = [item for sublist in courses for item in sublist]

    flattened_courses_lower = set(course.lower() for course in flattened_courses)

    filtered_words_with_next = []
    for i in range(len(CoursesTaken) - 1):
        word = CoursesTaken[i]
        if word.isupper() and word.lower() in flattened_courses_lower:
            filtered_words_with_next.append(word)  # Add the current item
            filtered_words_with_next.append(CoursesTaken[i + 1])  # Add the next item
    
    return(filtered_words_with_next)
    

def PrintToScreen(filtered_words_with_next):
    FinalList = []

    for n in range (0, len(filtered_words_with_next)-1, 2):
        FinalList.append(str(filtered_words_with_next[n])+str(filtered_words_with_next[n+1]))

    return(FinalList)

def GetListToTransfer(DegreeAutiFile):
    return(PrintToScreen(GetTakenCourses(GetDegreeAudit(DegreeAutiFile))))


def main():
    print(GetListToTransfer("calvintrancopy.txt"))


#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()




