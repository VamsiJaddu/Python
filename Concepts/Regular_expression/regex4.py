############## Quantiifiers ##############

## {n} -- n times
## + -- matches one or more
## * -- matches zero or more
## ? -- matches zero or one

import re
message ="The current python version is Python3.14 . Other previous versions are 3.13 ,3.12."

## {n} -- n times

pat = r'[a-z]{4}'
print(re.search(pat,message))

pat = r'[A-Z][a-z]{5}'
print(re.search(pat,message))

pat = r'[A-Z][a-z]{2,5}'
print(re.search(pat,message))

## + -- matches one or more

pat = r'[a-z]+'
print(re.search(pat,message))

pat = r'[A-Z][a-z]+'
print(re.search(pat,message))

## ? -- matches zero or one


pat = r'[a-z]?'
print(re.search(pat,message))

pat = r'[A-Z][a-z]?'
print(re.search(pat,message))

## * -- matches zero or more

pat = r'[a-z]*'
print(re.search(pat,message))

pat = r'[A-Z][a-z]*'
print(re.search(pat,message))



