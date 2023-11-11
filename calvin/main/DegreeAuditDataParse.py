"""
Made By Calvin Schmeichel for "Byte Me" (Team 5) | SCSU Hackathon Fall 2023
                                                                                                                        
                                                           ./*                                                          
                                                       @@@&////@@@#                                                     
                                                     %@@/%*    %%/@@                                                    
                                                     @@/%%      %%/@@                                                   
                                                     @@/%%%%%%%%%%&@&                                                   
                                                     @@/%%%%%%%%%%@@                                                    
                                                     /@&#%%%%%%%%&@@                                                    
                                                      @@/%%%%%%%%%@@                                                    
                                                      @@/%%%%%%%%&@(                                                    
                                                      @@(%%%%%%%&@@                                                     
                                                      .@@(%%%%%%%@@                                                     
                                                       @@/%%%%%%%@@                                                     
                                                       @@/%%%%%%@@.                                                     
                                                       @@@@@@@@@@@                                                      
                                                       @@/%%%%%#@@/                                                     
                                                      @@%#%%%%%%/@@/                                                    
                                                    @@@/%%%%%%%%%%/@@@                                                  
                                   @@@@@@@@@@@@@@@@&/#%%%%     %%%%%//@@@@@@@@@@@@@@@@@                                 
                                &@@ %%%%%%%%%%%%%%%%%%%%%%%   %%%%%%%%%%%%%%%%%%%%%%%, @@                               
                                @@/&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&/@@                              
                               &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                              
                               @@#########%%%%%%#%%#%%%%####%%%%#%%%%%%%#%%#############@@/                             
                               @@                                                        @@                             
                              @@# ****************************************************** @@                             
                              @@ ******************************************************* &@&                            
                              @@ ******************************************************** @@                            
                             @@*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@                            
                              @@@@@@@@@@@&@@@@&@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@                            
                         (#((((((((#((#(((##(((((((((((((((((((((((((((((((((((((((((((((((((((#                        

"""

#This function gets the degree audit file name and opens the file for the program to read and save it to a string
def GetDegreeAudit(DegreeAuditFile):
    #We first open the file
    with open(DegreeAuditFile, 'r') as file:
        #We then save the file contents
        file_contents = file.read()
    #We then split the data by blank/white space and make a list   
    CoursesTaken = file_contents.split()
    #Finally we return the saved list to main for further processing
    return(CoursesTaken)

#This function takes the newly generated "CoursesTaken" list and cleans out all the "Garbage" data we do not need
def GetTakenCourses(CoursesTaken):
    #This "courses" list contains all of SCSU's course acronyms to search by | Example: "CYB" = "Cyber Security"
    courses = [["ACCT"],["ANTH"],["ABA"],["ACR"],["ART"],["ASTR"],["AHS"],["BMB"],["BIOL"],["BRIT"],["BLAW"],["CHEM"],["CFS"],["CHIN"],["CCSD"],["COLL"],["CSD"],["CMST"],["CPSY"],["CMTY"],["CSCI"],["CM"],["COUN"],["CJS"],["CYB"],["DLA"],["EAST"],["ECON"],["ED"],["EDAD"],["ECE"],["EM"],["ENGL"],["EAP"],["ENTR"],["ENVE"],["ETS"],["ETHS"],["EXSC"],["FS"],["FIRE"],["FREN"],["GWS"],["GENG"],["GEOG"],["GER"],["GERO"],["GLST"],["HLTH"],["HPE"],["HBS"],["HIED"],["HIST"],["HONS"],["HTSM"],["HURL"],["IA"],["IM"],["IS"],["INTL"],["JPN"],["JWST"],["LC"],["LIB"],["MBA"],["MGMT"],["MFET"],["MKTG"],["MFT"],["MCOM"],["MPA"],["MATH"],["MME"],["MLS"],["MTQ"],["MILS"],["MUSE"],["MUSM"],["MUSP"],["NMDT"],["NURS"],["PHIL"],["PESS"],["PHYS"],["POL"],["PCOM"],["PSY"],["RADT"],["REC"],["RAS"],["RHAB"],["REL"],["SCHL"],["SOTA"],["SCI"],["STEM"],["SSE"],["SW"],["SOC"],["SE"],["SPAN"],["SPED"],["STAT"], ["TH"],["TSE"]]

    #We first normalize the text data within the lists so we don't run into search conflicts
    flattened_courses = [item for sublist in courses for item in sublist]
    flattened_courses_lower = set(course.lower() for course in flattened_courses)

    #We then create a new list to save the Course list
    filtered_words_with_next = []

    #This for loop compares the two lists and if it finds a match it adds it to the list with its class number.
    for i in range(len(CoursesTaken) - 1):
        word = CoursesTaken[i]
        if word.isupper() and word.lower() in flattened_courses_lower:
            #Add the current item (Class acronym)
            filtered_words_with_next.append(word)
            #Add the next item (Class number)
            filtered_words_with_next.append(CoursesTaken[i + 1])
    #We then return the new CourseList
    return(filtered_words_with_next)
    
#This function is mainly for debugging/testing but also a good way to view the content of the lists from the terminal
#We are also using this to format the final list in a standarized way for our other pythons scripts.
def PrintToScreen(filtered_words_with_next):
    #We create the final list
    FinalList = []
    #This for loop loops through our CourseList and formats the final list in a standarized way for our other pythons scripts.
    for n in range (0, len(filtered_words_with_next)-1, 2):
        FinalList.append(str(filtered_words_with_next[n])+str(filtered_words_with_next[n+1]))
    #Finally we send the FinalList with stnadard format for further processing in other pythons scripts.
    return(FinalList)

#This function calls the other functions to generate the FinalList and makes it easy for importing to other pythons scripts later.
def GetListToTransfer(DegreeAutiFile):
    return(PrintToScreen(GetTakenCourses(GetDegreeAudit(DegreeAutiFile))))

#This is our main function for testing.
def main():
    print(GetListToTransfer("calvintrancopy.txt"))


#This is so we can import the functions in this program in other code without having to run the main function
if __name__ == "__main__":
    main()