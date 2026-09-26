##### user defined modules #####

def add(*args):
    return sum(args)

def square_root(a):
    return a ** 0.5

# Here __name__ variable stops the running code when it is imported .
if __name__ =="__main__":
    a = 10
    b = 20
    result = add(a,b)
    print(result)
# Im importing this function into arthematic.py