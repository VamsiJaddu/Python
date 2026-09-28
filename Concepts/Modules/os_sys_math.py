# .py file is a module
# Built-in modules
# math, random, datetime .....

# how to import module
# import module_name 
# Syntax for importing only few functions/variables: from module_name import f1 ,f2 ,f3
# syntax to create alias for the module that is imported: import module_name as alias_name

# datetime Module

import datetime as dt
time = dt.time(8,43,7)

print(time)

import datetime

date = datetime.datetime.now()
print(date)

# Math module
import math

# calculate the square root of the number
num = 100
output = math.sqrt(num) # module.function(arg1,arg2,...)
print(f"Square root of the {num}: {output}")


# calculate the area of the circle

radius = 5
area = math.pi * radius ** 2
print(f"Area of the circle:{area}")

# Random Module
from random import randint
value = randint(1,6) 
print(f"Random value from 1 to 6 : {value}")

# Os module --- interact with operating system - files,folders,paths,environment variables

import os 

## to get current working directory
folder = os.getcwd() 
print(f"Current working directory: {folder}")

## list of directories in current working directory
folder = os.listdir()
print(f"Current working directory: {folder}")

## find out the file is existing or not in current working directory 

if os.path.exists("practice/range.py"):
    print("File exists")
else:
    print("File does not exist")

## It creates a folder in working directory.    
# os.mkdir("myfolder")


# sys module -- interacts with python itselt

import sys

## It shows the version of python
print(sys.version)

## It gives the o/p in list
print(sys.argv)


## here exits the python code when coondition is not satisfed.
age = 15

if age < 18:
    print("You are not eligible")
    sys.exit()

print("You can continue")