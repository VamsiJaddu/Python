## ^ - caret --- starting of the line
## $ - dollar --- end of te line
## [] - charter set
## () - group
##  | - or

import re
message = "Python is programming language"

## ^ - caret --- starting of the line
pat = r"[a-z]{8}"
print(re.search(pat,message))

pat = r"^[a-z]{8}"
print(re.search(pat,message))

## $ - dollar --- end of te line

pat = r"[a-z]{8}"
print(re.search(pat,message))

pat = r"[a-z]{8}$"
print(re.search(pat,message))


## [] - charter set


animal = "cat"
pat = r"[abc]"

print(re.search(pat,animal))

## | - or
email = "jhon123@gmail.com  is an email.alternate email is jhon123@edu.in"

pat = r'in|com'
print(re.search(pat,email))

## grouping - ()


message = "Python is programming language."

pat = r"[a-z]{8}(?=\.)"

result = re.search(pat, message)

print(result.group())



contact = "My phone number is 9876543210"

pat = r"(\d{3})(\d{3})(\d{4})"

result = re.search(pat, contact)

print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))