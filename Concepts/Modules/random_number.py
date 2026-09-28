import random
# Generate a random float number between 0.0 to 1.0(1.0 excluded)
print(f"Random Float between 0.0 and 1.0 : {random.random()}")


# Generate a random integer between 1 and 10 (both inclusive)
print(f"Random Integer between 1 and 10 : {random.randint(1,10)}")

# Generate a random number from a list of numbers
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Random numberfrom list :{random.choice(num)}")

#
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
random.shuffle(fruits)
print(f"Random fruits list : {fruits}")