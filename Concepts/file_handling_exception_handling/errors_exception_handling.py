## error handling
## 1.Compile error --- syntax / Indentation error
## 2.Exceptions error --- errors during execution 
## how to handle exception errors - try-except 


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))  
    result=(num1/num2)
    print(result)
except ZeroDivisionError:
    print(f"Denominator is {num2} it can't divide Numerator.")  
except ValueError:
    print("Only Integers are taken as a value")      
    
#### added file_err in except    
    
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))  
    result=(num1/num2)
    print(result)
except ZeroDivisionError as file_err:
    print(f"Denominator is {num2} it can't divide Numerator.")  
    print(file_err)
except ValueError as file_err:
    print("Only Integers are taken as a value") 
    print(file_err)        
  