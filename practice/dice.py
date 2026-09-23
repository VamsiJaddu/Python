###### dice (1 to 6) randomly ######
import random

print("Welcome to the dice game!")

while True:
    choice = input("press 'Enter' to roll the dice or 'q' to quit: ")
    choice = choice.strip()
    if choice == 'q':
        print("Thanks for playing!")
        break
        
    elif choice == '':
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll}!")
    
    else:
        print("Invalid input. Please try again.")    
print("Game over.")   
