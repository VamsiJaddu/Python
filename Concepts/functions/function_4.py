## Enormous function / LAMBDA FUNCTION - means which doesn not have a function name

# lambda argumnet : expression

func = lambda a : a + 1
print(func(1))


func = lambda a , b : a + b
print(func(11,2))

########## filter function #############

#filter(function,seq) --- filters frrom existing list

seq = [1,2,3,4]

filter_output = filter(lambda x : True if x % 2 != 0 else False,seq)
print(filter_output)
print(f"Odd numbers: {list(filter_output)}")

########### Map function  #################

# map(function,seq) ---- transform every item
seq = [1,2,3,4]

mapped_output = map(lambda x : x ** 2,seq)
print(mapped_output)
print(f"Odd numbers: {list(mapped_output)}")
