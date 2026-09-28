## read()---- reads the txt file shows in string.
## If you want char 5 or 10 you can give the number in read function. 

fh = open("practice1.txt",'rt')
content = fh.read()
fh.close()
print(content)
 print(type(content))


## read(char) --- can read the char from file. 
lh = open("practice1.txt",'rt')
content = lh.read(10)

lh.close()
print(content)
print(type(content))


## reads the first line of the file and with \n
## When the o/p give empty string --it is end of the file

fh = open("practice1.txt",'rt')
line1 = fh.readline()
line2 = fh.readline()
line3 = fh.readline()
fh.close()

print(line1)
print(line2)
print(line3)
## give an empty string only at end of the file.

## It reads thr lines of the file but it gives in the form list.

fh = open("practice1.txt",'rt')
lines = fh.readlines()
fh.close()
print(lines)
print(type(lines)) # list

for line in lines:
    print(line)
    
## To remove the spaces in betwn the lines we need to use strip.    
## strip can be used on strings.
## rstrip('\n') is used to remove the \nfrom the right.    

for line in lines:
    print(line.rstrip('\n'))