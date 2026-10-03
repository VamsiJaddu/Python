#### Regular Expression - re module ####

message = "The current python version is 3.14.7"

## membership operator True/False

print("python" in message)
print("3.14.7" in message)
print("15" in message)

## using Find for index 
print(message.find("3.14.7"))
print(message.find("python"))
 
 ## re.search(regex pattern,string)
 ## returns match object when match found else returns None
 
import re  
 
message = "The current python version is 3.14.7"

output = re.search('is',message)
print(output)
 
result = re.search('13',message)
print(result)

if re.search('14',message):
    print("found")
else:
    print("Not found")    


print(message[27:29])


 