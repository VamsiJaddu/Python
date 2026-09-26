########### cotinue statement is used to skip the current iteration of a loop and move on to the next iteration. It is often used in conjunction with an if statement to skip certain iterations based on a condition
for i in range(10):
    if i % 3 == 0:
        continue

    print(f"{i} is not divisible by 3") 


########## break statement is used to exit a loop prematurely, before the loop has completed all of its iterations. It is often used in conjunction with an if statement to exit the loop when a certain condition is met.
for i in range(1,10):
    if i % 3 == 0:
        break

    print(f"{i}")     