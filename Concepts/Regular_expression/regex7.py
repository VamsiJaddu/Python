## sub(pattern,replacement,string,count,flags=re.IGNORECASE) --- Replaces matched string

import re

s1 = " Sunday, Monday, Teusday, Monday, Sunday"
pat = "Sunday"
replacement = "Friday"
print(re.sub(pat,replacement,s1))
print(re.sub(pat,replacement,s1,count=1))


s2 = "The PYTHON program is running with python version 3.14"
pat =r'\bpython\b'
replacement = "hello"
print(re.sub(pat,replacement,s2, flags=re.IGNORECASE))

phone = "91-9898833444 , +91-9876543212"
pat = r'[+-]'
replacement = ""
        
print(re.sub(pat,replacement,phone))   


text = "cat dog cow"
pat = r"(dog|cat)"

print(re.findall(pat, text))
print(re.search(pat, text))
print(re.match(pat, text))
print(re.findall(pat, text))


