## Problem Statement: Write a Python program that:
## Takes user input and writes it to a file named output.txt.
## Appends additional data to the same file.
## Reads and displays the final content of the file.


str = input("Enter text to write the file : ")
with open("output.txt",'wt') as fh:
    fh.write(str + "\n")
    print("Data sucessfully written to output.txt")
 
txt = input("Enter additional text to append: ")    
with open("output.txt",'at') as fh:
    fh.write(txt)
    print("Data sucessfully appended to output.txt")
    
with open("output.txt",'rt') as fh:
    print(f"Final content of the output.txt: {'\n'+ fh.read()}")   