############## with Statment ##############
## with statment ensures automatic closure of file after reading the file  
with open("practice1.txt", 'rt') as fh:
    print(fh.read())
   
########## Normal Read ###########

fh = open ("practice1.txt", 'rt')
content = fh.read()
fh.close()
print(content)

fh = open ("practice1.txt", 'rt')
print(fh.read())
fh.close()


 
