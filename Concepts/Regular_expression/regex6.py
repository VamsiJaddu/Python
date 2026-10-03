## re.match(regex pattern,string) -- checks at the begining else it give None.

import re
message = "Python is programming language."
email = "john@gmai.com and alternate mail is john@edu.in"
phone = "Jhon-9876543212, Alex-9876543211, George-9876543213 , mark-7654321, Alice - 123456789987654321" 

pat = r'[a-z]{3}'
print(re.match(pat,message))

pat = r'[a-z]{3}'
print(re.match(pat,email))
print(re.match(pat,email).group())

pat = r"[0-9]{10}"
print(re.match(pat,phone))

## findall(regex pattern,string) --- returns all matches -- list

pat = r"[0-9]{10}"
print(re.findall(pat,phone))

pat = r"[0-9]{10}\b"
print(re.findall(pat,phone))

pat = r"\b[0-9]{10}\b"
print(re.findall(pat,phone))

# fetch all the phone numbers exactly 7 and should not exceed 15 digits

pat = r"[0-9]+"
print(re.findall(pat,phone))


pat = r"\d+"
print(re.findall(pat,phone))


pat = r"\b[0-9]{7,15}\b"
print(re.findall(pat,phone))

pat = r"[0-9]{7,}"   ### infinte
print(re.findall(pat,phone))

## finditer(regex pattern,string) ---- returns match object for all matches

pat = r"\b[0-9]{7,15}\b"
print(re.finditer(pat,phone))

pat = r"\b[0-9]{7,15}\b"
result = re.finditer(pat,phone)
for match in result:
    print(match)




