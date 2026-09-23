############## position Arguments #######

def add(a,b):
    return a + b

a = int(input("enter the value: "))
b = int(input("enter the value: "))
result = add(a,b)
print(result)



############ default arguments ################


def add(a,b=10):
    return a + b

result = add(10,5)
sum = add(10)
print(result)
print(sum)

# the non defualt arguments should not follow the default arguments.

############# Keyword Arguments #############
def add(a,b=10,c=20):
    return a + b + c

result = add(10,c=5)
print(result)
