  ######## factorial of n! #############
  
  
num = int(input("Enter the number: "))
def fact(num):
    factorial = 1
    while num>=1:
        factorial *= num
        num -=1  
    return factorial

print(f"Factorial of {num}! is: {fact(num)}")      