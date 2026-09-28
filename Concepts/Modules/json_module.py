############# Json Module ##############
# In json strings in " ".
# In json boolean in lowercase.
# In python json is handled by json library.
# usually json is used in Api's and data storage.

import json

students = {
    'student1' : {
        'name' : 'Jhon',
        'age' : 24,
        'sport': True,
        'percent': 90.5
    },
    'student2' : {
            'name' : 'Jhon',
            'age' : 23,
            'sport': True,
            'percent': 80.5
    },
    'student3' : {
             'name' : 'Jhon',
             'age' : 25,
             'sport': False,
             'percent': 91.5
    }
}

print(students)
print(type(students))

### dump() in json ### - used to convert the dictionary into json --- Serialization
with open("students.json",'xt') as fh:
    json.dump(students ,fh,indent=4)
    
    
### load() in json ### - used to convert the json into dictionary --- Deserialization

with open('students.json','rt') as fh:
    data = json.load(fh)
    print(data)
    print(type(data))
    

### update() in json ### - used to update the json file.

new_student = {
    'student4': {
         'name' : 'Alex',
         'age' : 25,
         'sport': False,
        'percent': 91.5
    }
}

with open("students.json",'rt') as fh:
    students = json.load(fh)    
    
students.update(new_student) 
print(students)

with open("students.json",'wt') as fh:
    json.dump(students,fh,indent=4)   