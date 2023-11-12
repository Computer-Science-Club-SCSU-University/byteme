# importing required modules 
from PyPDF2 import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader('page.pdf') 
  
# printing number of pages in pdf file 
pages = int(str(len(reader.pages)))
  
floating_pages = ""
for i in range(pages):
    page = reader.pages[i]
    text = page.extract_text() 
    floating_pages += floating_pages + text

 
print(text) 
filename = "audit.txt"

# Open the file in write mode ('w') and write the string to it
with open(filename, 'w', encoding='utf-8') as file:
    file.write(floating_pages)
