########### function as a Argumnet ###########

def add(number):
    return number + 1


def square(number):
    return number ** 2

num = int(input("Enter the number: "))

print(f"Square of {num}: {square(add(num))}")