############ User defined function #############

def function_name(a,b ....N):
    statement1
    statement2

function_name(a,b ...N)

# multiple arguments ---- *arg
def function_name(*arg):
function_name(a,b,c)

#####################################################

def even_odd(num):
    if num % 2 ==0:
        print("Even number")
    else:
        print("Odd number")
        
even_odd(5)
even_odd(56)

# this function will not return any value so if we try to store the result in a variable it will return none
result = even_odd(5)
print(result)    


########### return instead of print ##############

def even_odd(num):
    if num % 2 ==0:
        return "Even number"
    else:
        return "Odd number"

result = even_odd(5)
print(result)  

####### addition of two numbers ##########

def add(a,b):
    result = a + b
    return result

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = add(a,b)
print(f"adddition of {a} and {b} is {result}")

########### add,sub,mul ###################

def arthimatic(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    return add , sub, mul

a = int(input("Enter the value: "))
b = int(input("Enter the value: "))


res_1,res_2,res_3 = arthimatic(a,b) 
print(f"addition of {a} and {b} is {res_1}")
print(f"substraction of {a} and {b} is {res_2}")
print(f"multiplication of {a} and {b} is {res_3}")
