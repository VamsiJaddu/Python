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

# The variable arguments is length of the positional argumnets and prints in TUPLES
  
def add(*args):
    return sum(args)

result = add(10,5,20,40)
print(result)

def add(*args):
    print(f"sum of nubers:{sum(args)}") 

add(10,5,20,40)

#keywaord variable is length of keywords and prints in DICITIONARY.

def add(**kwargs):
    return sum(kwargs.values())

result = add(a=10,b=5,c=20,d=40)
print(result)


######## precendence (a,b,*args,**kwargs) ###########





