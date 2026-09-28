############# file exists ##############

import os 

file_name =  "practice2.txt"
if os.path.exists(file_name):
    print("file exist!")
else:
    print("file doesn't exits.we create a file.")
    with open(file_name,'xt') as fh:
        fh.write("Welcome to python!")
        fh.write("let's start python.")
        
import pathlib

# pathlib.Path.exits()

file_name = pathlib.Path("practice3.txt")
if file_name.exists():
    print("file exist!")
else:
    print("file doesn't exits.we create a file.")
    fh = open(file_name,'xt')
    fh.write("Welcome to python!")
    fh.write("let's start python.")
    fh.close()

        