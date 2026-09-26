############## Docstring in a function ###########

# def func():
#     '''
#     sum of two numbers
    
#     '''
#     return none

# print(help(func))   


def divide(num1,num2):
    """
     num1 : numerator
     num2 : denomator
     :return : float
    """
    if num2 == 0:
        return "Denomator is zero cannot divide a number"
    else:
        result = num1/num2
        return result

help(divide)
print(divide(10,2))