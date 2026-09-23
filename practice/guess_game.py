
############ Guessing Game ###########

import random
        

secret = random.randint(1, 50)
print("Secret number is between 1 to 50.")
print("You have 10 chances to guess it right!")
 
for i in range(10, 0, -1):
    user = int(input("Guess the number: "))
    if user == secret:
        print("Congrats! You guessed it right!")
        break
    elif user < secret:
        print("You guessed it low! Try high.")
        print(f"You have {i-1} chances left.")
    else:
        print("You guessed it high! Try low.")
        print(f"You have {i-1} chances left.")
print(f"The secret number was: {secret}")
print(" Game Over!")