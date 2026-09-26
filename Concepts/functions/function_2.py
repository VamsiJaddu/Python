# Recursion is a process in which a function calls itself till a certain condition met 
# Factorial n!= n*(n-1)*(n-2)*(n-3)....2*1

# There are 2 parts of recursive function.
# 1. Base/Terminal condition
# 2. Recursive condition


num = int(input("Enter a number: "))    
def fact(num):
    if num == 1 :
        return 1
    else:
        factorial = num * fact(num-1)
        return factorial
    
print(f"factorial of {num}: {fact(num)}")    
    
 