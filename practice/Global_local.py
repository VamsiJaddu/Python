 ########## Global_Local variable ###############
 
# global variable
 
# n = 1 

# def func():
#     #local variable to function
#     n = 3
#     print("local", n)
    
# func()    
# print("global",n)


 
n = 1 

def func():
    global n
    n = 3
    print("local", n)
    
func()    
print("global",n)
n = 30
print("global",n)
func()
print("global",n)

