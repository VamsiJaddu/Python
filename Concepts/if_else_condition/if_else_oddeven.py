########## Find out given number is odd/even . using if-else ##############

num = int(input("Enter a Number: "))

if num % 2 == 0:
    print(f"{num} is a even number.")
else:
     print(f"{num} is a odd number.")   
     


########## Find out given number is odd/even .using user defined function with print ,if-else ##############      

def even_odd(num):
    if num % 2 == 0:
       print(f"{num} is a even number.")
    else:
       print(f"{num} is a odd number.")    
       
num = int(input("Enter a Number: "))
even_odd(num)       

########## Find out given number is odd/even .using user defined function with return ,if-else ##############  

def even_odd(num):
    if num % 2 == 0:
       return f"{num} is a even number."
    else:
       return f"{num} is a odd number."    
       
num = int(input("Enter a Number: "))
result = even_odd(num) 
print(result)   