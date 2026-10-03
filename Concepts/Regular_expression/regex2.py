## if there special char or symbols in regex pattern is called as metacharacters.


import re

message = "The current python version is 3.14 . Other previous versions are 3.13 ,3.12 ."

# metachar - [0-9] 

## Here char matching gives only first occurance
print(re.search("[0-9][0-9]",message))
print(re.search("[0-9][0-9]","Address : 215/A"))
print(re.search("[0-9][0-9][0-9]","Address : 215/A"))

# metachar - .
## (.) ---- dot matches any character except new line character (\n). 
print(re.search("[0-9].[0-9]",message))
print(re.search("[0-9].[0-9][0-9]",message))
print(re.search("[0-9].[0-9]","Address : 215/A"))

content = "This is 2026 year."
print(re.search("[0-9].[0-9][0-9]",content))
print(re.search("[0-9][.][0-9][0-9]",content))
print(re.search("[0-9][.][0-9][0-9]",message))






