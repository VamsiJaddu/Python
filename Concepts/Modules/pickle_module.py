############## Serialization ##############
'''
    In python we know we work with high level data types (list ,tuples,dict) and
    we want to store this data in memory or files need to be converted into sequence of bytes 
    for understanding of computer- Serialization
'''

############### Deserialization #############
"""
   when we want to access data structures from the stored file,
   the sequence of bytes should covert back into original datatype this process is called Deserialization.
"""

### Pickle module is used store the datatypes in file and access back while it required.

import pickle

students = {
    'student1' : {'name' : 'Jhon','age' : 24,'sport': True,'percent': 90.5},
    'student2' : {'name' : 'Jhon','age' : 23,'sport': True,'percent': 80.5},
    'student3' : {'name' : 'Jhon','age' : 25,'sport': False,'percent': 91.5}
}

print(students)
print(type(students))


## Serialization ###
# Here we dumping the values of the each student one by one using loop:
with open("students.bin",'xb') as fh:
    for student in students: 
        pickle.dump(students[student],fh)
    

### Deserialization ###
# here we have to load the values one by one because of upper step:
with open("students.bin",'rb') as fh:
    print(pickle.load(fh))
    print(pickle.load(fh))
    print(pickle.load(fh))
    
### Serialization ###
# Here we dumping the value of the students:
with open("students.bin",'xb') as fh:
        pickle.dump(students,fh)
    

### Deserialization ###
# here we have to load once:
with open("students.bin",'rb') as fh:
    data = pickle.load(fh)
    
    print(data)
      