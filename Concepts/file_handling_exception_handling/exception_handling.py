############ Exception handling ################
## try-except else --- after excution of try block no error, code enters into else block when there is no exception.

try:
    with open("practice1.txt",'rt') as fh:
        data = fh.read()
except FileNotFoundError as file_err:
    print("File is not found") 
    print(file_err)
else:       
    print(data)
    
    
######## try-except else finally #########  
import io  
    
try:
    fh = open("practice1.txt",'wt')
    data = fh.read()
except FileNotFoundError as file_err:
    print("File is not found") 
    print(file_err)
except io.UnsupportedOperation as io_err:
    print("while in writing mode , we can't read.")
    print(io_err)    
else:       
    print(data)  
finally:
    print("Finally,Code execution is done. ") 
    fh.close()       
    
######## try-except finally #########  
import io  
    
try:
    fh = open("file.txt",'wt')
    fh.write("hello")
except FileNotFoundError as file_err:
    print("File is not found") 
    print(file_err)
except io.UnsupportedOperation as io_err:
    print("while in writing mode , we can't read.")
    print(io_err)     
finally:
    print("Finally,Code execution is done. ") 
    fh.close()      
    