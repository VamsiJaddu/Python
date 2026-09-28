## vedio,audio,images files stored in binary --bytes
## 1byte - 8bits
## opening a file in python
#(open_file,mode to open)
# modes (r=read , x=create , w=write , a=append , t=txt , b=binary) By default = rt


# Creation of file and writing

file = open("practice1.txt", 'xt')
file.write("Hi Good to see you")

file.close()

# Opening and reading the file

file_handler = open("practice1.txt",'rt')
print(file_handler)

file_handler.close()
print(file_handler)

