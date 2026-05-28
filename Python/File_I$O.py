# # FILE I/O:                                   ## File_I/O.py====> invalid file name due to the slash
#     # Chap#07_py4e(Book)
# In real life we work with files in the following way:
#     1) we take a file
#     2) open it    (for reading by default)
#     3) after opening, we read or write etc.
#     3) close it
# the same principal with some differences we use in virtual life too.
#
# # OPEN READ OR CLOSE FILE:
# #     WE HAVE TO OPEN A FILE BEFORE READING OR WRITING.
# #     FOR THIS WE HAVE BUILT-IN FUNC IN PYTHON
# # #    SUNTAX:
# #         file=open("file_name","mode")
# #             we assign the side effect of the open() func to file var for printing.
# #             the open() func take two perametors(in quotes):
# #                 1) file_name(with extention/suffex) OR  the path if the file isn't in the current working directory
# #                 2) mode--> mean that we wanna do with file(the mode is also a default perameter: read (by default-> if we didn't show mode explicitely))
# #                 # modes:
# #                 #     Character Meaning
# #                 #
# #                 #         'r' open for reading (default)
# #                 #         'w' open for writing, truncating the file first(over write---> the data which is already in the file will vanish first and then the new data will add. )
# #                 #         'x' create a new file and open it for writing
# #                 #         'a' open for writing, appending to the end of the file if it exists
# #                 #         'b' binary mode (for binary files)
# #                 #         't' text mode (default)
# #                 #         '+' open a disk file for updating (reading and writing) like, "r+"---> means read and write & w+--> write + read , a+---> append + read etc.
# #                 #             we can also write two modes combinely, like. "rt" ----> meaning reading text file but we don't write the t b/c its is t by default
# #                 #             but if we wanna read binany file then i will do it---> "rb" reading binary files
# file=open("demo.txt","r")   # opening the file   # in current working derectory(i.e in my same folder/directory (Apna_College among my lecture file))   # "/" --> inside & "\" -->
# # # i.e path: /Users/SALAMAN COMPUTERS/PycharmProjects/Apna_College/demo.txt
# # file=open("/Users/SALAMAN COMPUTERS/PycharmProjects/Apna_College/demo.txt","r")
# # after opening we can perform operation:
# data=file.read()  # to read the file
# print(data)
# file.close()  # should be close   # if we left it so a risk is created that anyone can acces, open anyone can read it, change in it (if in writing mode) etc.
# # but
# # if i move my file to other folder/out of the folder like, then i have to specify complete path where the file lies
# # file=open("demo.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'demo.txt'
# # file=open("/Users/SALAMAN COMPUTERS/PycharmProjects/Apna_College/File_I/demo.txt","r")  # inside users in salaman computers in pycharm projects in apna coolege in file_i is demo .txt
# # # print(file.read())
# f=open("/Users/SALAMAN COMPUTERS/PycharmProjects/Apna_College/demo.txt","r+")
# print(f.read())
# f=open("/Users/SALAMAN COMPUTERS/PycharmProjects/Apna_College/demo.txt","r")
# print(f.read()) #ValueError: Must have exactly one of create/read/write/append mode and at most one plus
#
#
# ## READING A FILE:
#      # we read the read() methd for reading ga file
#         # red=file.read()       # reads entire file
#         # we can slso pass perameter of no of chars that we wanna read to thye read() func, i.e.
#         # red=file.read(7)  # will show 1st 7 chars
#         # print(red)
#         # red_line=file.readline()         # reads one line at a time
#
#
# data=open("demo.txt","r")
# # red=data.read(7)
# # print(red)  # Hey! Gu
#
# red_lin1e=data.readline()
# print(red_line1)     # Hey! Guys how are you?
#
# ## ALSO EMPTY LINE AFTER THE LINE IT'S DUE TO THE NEWLINE CHAR AT THE END OF OUR 1ST LINE(that we don't see) WHICH SPECIFY END OF THE LINE BUT THERE IS ALSO ANOTHER \N CHAR(OF PRINT FUNC) THAT SPECIFY THE END OF THE EMPTY LINE . I.E,
# print("Jamal\n")
# print("Qadar")
# ## output:
# # Jamal
# #
# # Qadar
# # # this is b\c in our 1st statement(print("Jamal\n")) there  are two new line chars; one we passed and another is of the print function, by default--> documentation(
# # # def print(*values: object,
# # #           sep: str | None = " ",
# # #           end: str | None = "\n",) <<----this one
# #
# #
# # red_line2=data.readline()
# # print(red_line2)        # empty line b\c we have an mpty line in our file
# #
# # red_line4=data.readline()
# # print(red_line4)        # as there no line 4 so it will just print an empty line due to \n of print func and nothing else.
# #
# # data.close()        # im a responsible programmer
# #
# #
# # # BUT but but...
# # data=open("demo.txt","r")
# # print(data.read())
# #
# # red_line1=data.readline()
# # print(red_line1)
# #
# # red_line2=data.readline()
# # print(red_line2)
# #
# # red_line3=data.readline()
# # print(red_line3)
# # # OUTPUT:
# # # Hey! Guys how are you?
# # #
# # #     This is our demo file of type & suffex of .txt to perform basic operation on the file.
# # #
# # #
# # #
# # #
# # #
# # #
# #
# # ## if i first read the entire file and then(before/without closing and re-opening of the file) i wanna read a line that will not possible will print only an empty line.
# # # this is because of POINTER\CURSER:
# #     # IMAGINE A POINTER THAT READ EACH CAR ONE AFTER ONE IN A SEQUENCE OF GOING FORWARD(NEVER COME BACK)
# #     # IN THE THE ABOVE CASE THE POINTER IS ALREADY READ THE ENTIRE FILE, SO FOR THE NEXT LINE EXECUTION(WITHOUT CLOSING & RE-OPENING) IT WILL NOT GO BACK; SO IT JUST PRINT AN MPT LINE.
# # # SO IF WE READ-ALL FIRST THEN IN THE LINE WE WILL GET ONLY MPT SPACE
# #
# # ## similar is the phenamena of pointer with the line methd, i.e, never come back & reads everything:
# #     # it means we can't print line 1 after line 2 b\c the pointer is already moved to line 3.
# #     # for this we have to close and re-open the file.
# #                     # how will you specify no. of a line b\c for the fist time it will print line one, then 2nd and so on.???          (left for later, expert level!!!    inshallah)
# #
# #
# # # WRITING FILE:
# #         AS WE DO IN READING MODE, IN WRITING MODE WE ALSO HAVE TO OPEN THE FILE BEFORE WRITING IN IT.
# #         # TWO WAYS OF WRITING
# #             # "W"--> WRITE(OVER WRITE->{VANISH THE FILE 1ST AND THEN WRITE NEW DATA }) & "a"---->APPEND(ADD TO THE END).
# # # ## IN WRITING MODE
# # # data=open("demo.txt","w")
# # # data.write("i'm replacin gmy original data with new:->hmmmmmmmm")       # every thing in our file is replace dby the new data we   enter
# # # data.write("Hey! Guys how are you?\n\n              This is our demo file of type & suffex of .txt to perform basic operation on the file.")      # two \n one for the end of 1st line and next for the end of 2nd(empty) line:  if i didn't pass any \n then all the data in file were in a single line.
# # # # back to original
# # # data.close()
# #
# # ## IN APPENDING MODE
# #
# # data=open("demo.txt","a")
# # data.write("\nwe use th write func in append mode, to write at the end.")    # \n is for showing an empty line before adding the data as one is in the previous line end.
# # # it will add it every time i run it.
# # data.close()
# #
# #
# # ## OKAY:
# # # if we didin't create file before we write or append something and we call the file for writing\appending python will create it by itself in the same directory.
# #
# # new_file=open("Sample.txt","w")     # will crearte the file as i run it in my working directory abd write the data in it.
# # new_file.write("Hello World")
# # ## will create only once irrespective of my running attempt as no repeated(of same name) file can store.
# # new_file.close()
# #
# # # ## BUT:
# # # newfile_red=open("read.txt","r")
# # # print(newfile_red.read())       # FileNotFoundError: [Errno 2] No such file or directory: 'read.txt'
# # # # it will not create only in read mode, but
# # # newfile_redplus=open("read.txt","r+")
# # # print(newfile_redplus.read())
# # # also will not create, but
# # newfile_redplus_writes=open("read.txt","r+")
# # newfile_redplus_writes.write(" Hi. this is how we think....")
# # print(newfile_redplus_writes.read())
# # #### this time also not created.
# #
# #
# # #***so it means that only creates in write and in append mode
# #* {SHOULD STUDY}---> DIFFENCE B\W MODE[ON STACK OVERFLOW WEB](LINK IN DESC OF APNA COLLEGE LEC 7 ON FILE I\O)
# #
# # ## COMBINING DIFFERENT MODE:
# #     # 1) r+ => reading and writing(OVER WRITE),NO truncation(JUST replacing) occurs(only at beganing and equal to the amount of new data), but over writing happens at beginning(the stream / pointer at begganing)
# #         # so if we wanna add(replace by new data) data at beganing of file we can use the r+ mode
# #         # truncating data==new data
# # newf=open("demo.txt","r+")
# # newf.write("*hi at beganing*")
# # newf.close()
# # # so it will overwrites the data at beganing and replace them by new data
# #
# #     # 2) w+ => writing and reading, truncation occurs(of entire file), the stream is positioned at the beganning of a file()AS NO DSTA IS LEFT SO EVERY WHERE IS BEGANNING FOR ADDING NEW DATA
# #         # if we wanna replace the entire file with the new
# # newf=open("Sample.txt","w+")
# # newf.write(" in w+ mode python can create the file if not exist.")
# # newf.close()
# #
# #     # 3) a+ => append and read, no truncation occurs/ NO REPLACING, the stream is positioned at the end of the file
# #         # should use if we wanna add new data to the file through writing
# # newf=open("Append.txt","a+")
# # newf.write(" in a+ mode python can create the file if not exist.")
# # newf.close()
# # # will append as many time i run it at last
# #
# # # WITH() SYNTAX:
# #     THRE IS A BETETR WAY OF OPEN, CLOSE OF FILES
# #     SYNTAX:
# #         with open("FIILE_NAME", "MODE") as f:     # we called the entire stuff 'f' for easiness and THIS IS CALLED "ALIES"-> means that two different names refering to the same thing. i.e, tony stalk and iron man == 1 acter
# #             data = f.read()
# #
# #         the entire statements inside the body will depends upon the 'f'
# # let we have file {Sample1,txt} and we wanna open it, read it and close it
# # with open("Sample.txt","r") as f:       # the f is an alias for the stuff resulting from the statement, i.e, f and Sample.txt==same file
# #     data = f.read()
# #     print(data)
# #  # we don't need to close the file as the with will take care of that
# #
# #
# # ## DELETING FILE:
# #         # WE CAN'T SIMPLY DO F.DEL/REMOVE FOR DELETING A FILE THROUGH OUR CODE, we use a module for that
# #     # using the os module(os stands for operating system)
# #     # module(like a code library) is a file written by another programmer that generally has a func we can use
# #     # before using a module we have to import it:
# # # import os
# # # os.remove("filename" or path)     # the remove is a func written by someone leso in the mosule
# #
# # import os
# # os.remove("file_name.txt")
# # # so it is deleted.
# #
# #
# #
# # ## IF A MODULE DON'T COME PRE INSTALLED WITH PYTHON AND WE ENTER import name WE WILL GET MODULENOT FOUND ERROR
# #     # SO WE INSTALLED THEM FROM INTERNET
# #     # FOR INSTALLING WE WRITE: pip/pip3 install {tensorflow}            # pip3=> package installer for python 3
# #
#
#
# ## PRACTICE:
# # 1) Create a file " practice.txt " using python. add the following data to it:
#     # Hi everyone
#     # we are learning file i\o
#     # using Java
#     # i like programming in java
#
# # WAF that replace all occurance of "java" with "Python" in above file.
# # search if the world "learning " exist in the file or not.
# # sol:
with open("practice.txt","w") as practice:
    practice.write("Hi everyone\nwe are learning file i\\o\n")
    practice.write("using Java\ni like programming in Java")
    # print(practice.read())  ## ValueError: I/O operation on closed file.
# so we have to opoen it FOE READING
with open("practice.txt","r") as f:
    print(f.read())
# WAF that replace all occurance of "java" with "Python" in above file.
def rep(word,new_word):
  with open("practice.txt","r") as f:
      data=f.read()
      new_data=data.replace(word,new_word)
      print(new_data)
rep("Java","Python")
## for changing in the file
with open("practice.txt","w") as f:
    data=f.read()
    new_data = data.replace("Java", "Python")
    f.write(new_data)
    print(new_data)



# with open("practice.txt
# ","w+") as f:
#     f.write("Hi everyone\nwe are learning file i\\o\n")
#     f.write("using Java\ni like programming in Java")       # to reduce long line can helps reader
#
# # it will add as many time i  run it(in a+) so i convert it to w
# # NOW FOR ACCESSING THE WORDS TO MANIPULATE WE FIRST HAVE TO READ THE FILE
#
# with open("practice.txt","r") as f:
#     data=f.read()   # all the data of the file is now in the data var as we read to it
# ## as data is a string so we can use its methods
# new_data=data.replace("Java","Python")
# print(new_data)
#
# # now changing in the file
# with open("practice.txt","w") as f:
#     f.write(new_data)

## ioj euw9uidru98kjj9io8jj980uklc9o8 uoi 98889u89 p9-009km,nkj njhgyn ,jkoljkjniovm nzjkjszdjkdzjbcjhdhiu m jkj k jkf iunij hjk jijkjnhjk--------------->>>  i'M SORRY BUT I CELEBRATE MY HAPPINESS LIKE THIS. bye$!>>>....

##***
# print("jamal"
#       "nasar"
#       "khan")   ## jamalnasarkhan

##
# "/"  =>  inside &   "\"  =>  outside or escape
