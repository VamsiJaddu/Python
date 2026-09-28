############# Raising Exception Error ############

salary = int(input("Enter your Salary: "))

if salary < 0:
    raise ValueError("Salary won't be in Negative!")
else:
    print(f"Your salary is: {salary}")


#### if-else Raise Exception ####   
age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age shouldn't be in Negative")
else:
    if age > 18:
        print("You can vote")
    else:
        print("You can't vote")   
                
#### try-except else finally Raise Exception ####
try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise Exception("Age won't be negative!")

except ValueError:
    print("You have to enter only integers.")

except Exception as val_err:
    print(val_err)

else:
    if age >= 18:
        print("You can vote")
    else:
        print("You can't vote")

finally:
    print("The program is done")