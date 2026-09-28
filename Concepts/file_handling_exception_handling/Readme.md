## vedio,audio,images files stored in binary --bytes
## 1byte - 8bits

FILE HANDLING:
## opening a file in python
## modes (r=read , x=create , w=write , a=append , t=txt , b=binary) By default = rt
## open("open_file",'mode to open')
## close(), write() , read()
## W- mode will overwrite the txt in the file
## if file is soesn't present it will create the new file .
## read()---- reads the txt file shows in string.
## read(char) --- can read the char from file. 
## readline()---reads the first line of the file and with \n
## readline()---give an empty string only at end of the file.
## readlines()---It reads thr lines of the file but it gives in the form list.
## with statment ensures automatic closure of file after reading the file  
## with open("filename",'mode') as variable: no need of close
## if file exists using os , pathlib module   


EXCEPTION HANDLING:
## error handling
## 1.Compile error --- syntax / Indentation error
## 2.Exceptions error --- errors during execution 
## how to handle exception errors - try-except block
## try-except else finally --- after excution of try block no error, code enters into else block when there is no exception.Final stage executes on every go.
## you can raise the exception in try stage when ccondition is not acceptable.