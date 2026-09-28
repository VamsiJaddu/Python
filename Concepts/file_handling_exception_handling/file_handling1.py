# W- mode will overwrite the txt in the file
# if file is soesn't present it will create the new file .

file = open("practice1",'wt')
file.write("Have a nice day!")
file.close()


fh = open("practice1.txt",'wt')
fh.write("Have a nice day!")
fh.close()

