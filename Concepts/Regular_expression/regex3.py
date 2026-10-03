
## [A-Z] ,[a-z]

import re

s1 = "Python is programming langauage."

## \n is consider as new line
pat = "old\new" 
print(pat) 

## r -- raw string
content = r"old\new"
print(content)

output = r"[a-z][a-z]" 
print(re.search(output,s1))

result = r"[A-Z][a-z][a-z]"
print(re.search(result,s1))

## \d and \D 
## metachar \d -- consider 1 digit character like [0-9].

message = "The current python version is python3.14 . Other previous versions are 3.13 ,3.12 ."

pat = r'[a-z][a-z][a-z]\d'
print(re.search(pat,message))

## metachar \D --- matches to any non-digit character.
cat = r'[a-z][a-z][a-z]\D'
print(re.search(cat,message))

## \s and \S
## metavhar \s -- matches to any spaces and it matches \t and \n(new line).

pat = r'[a-z][a-z][a-z]\s'
print(re.search(pat,message))

s2 = """Hi Hello
Hi there, how are you."""

pat = r'[a-z][a-z][a-z]\s'
print(re.search(pat,s2))
## metavhar \S -- matches to any character and except spaces, \t and \n(new line).

pat = r'[a-z][a-z][a-z]\S'
print(re.search(pat,message))

pat = r'[a-z][a-z][a-z]\S'
print(re.search(pat,s2))

## \w and \W
## metavhar \w -- matches [a-z],[A-Z],[0-9].

pat = r'[a-z][a-z]\w'
print(re.search(pat,message))

pat = r'[a-z][a-z][a-z]\w'
print(re.search(pat,s2))

## metachar \W -- matches spaces,\n,-,$ etc.. except [a-z][A-Z][0-9]

pat = r'[a-z][a-z]\W'
print(re.search(pat,message))

pat = r'[a-z][a-z][a-z]\W'
print(re.search(pat,s2))

