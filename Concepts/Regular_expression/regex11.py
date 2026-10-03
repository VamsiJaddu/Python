import re

with open('Student_details', 'rt') as file:
    pattern = r'\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]{2,3}\b'
    
    print(re.findall(pattern, file.read()))