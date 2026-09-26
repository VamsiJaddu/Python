
####### for loop ######

for i in range(1,6):
    print("* " * i)




#### Infinite Loop ##################

secret = "python"

while True:
    password = input("Enter the password: ")
    if secret == password:
        print("Access granted!")
        break
    else: 
        print("Access denied! Try again.")
print("You have successfully logged in.")        