from regex9 import pattern_compiled

with open("Student_details", "rt") as file:
    
    phone_numbers = pattern_compiled.findall(file.read())    
    print(phone_numbers)