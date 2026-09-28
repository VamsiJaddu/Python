## a -- append the lines to the existing file
## if file doesn't exist, it will create the new file and write 

fh = open("practice1.txt",'at' )
fh.write('Hello, how are you?\n')
fh.write('Hi,Im good\n')

fh.close()