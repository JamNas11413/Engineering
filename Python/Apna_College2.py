# LEC2 STRINGS AND CONDITIONAL STATEMENTS
#STRINGS:
  #DATATYPE THAT STORE SEQUENCE OF CHARS
  #b.ope:
  # concatination
  # print('hello' + 'world')
      # len(str)
print(len("jamal nasar"))

str1 = 'this is a string\n'
str2 = "this is a string\n"
str3 = """this is a string"""
print(str1,str2,str3, sep='\n')

print("its's mine")

#ESCAPE SEQUENCE CHARS                                                 # "\" means pa de shate ke/na
    # TAB:"\t"  to print tab b/w strings
print("Hello \tWorld")
    #NEW LINE: "\n" to end the line
print("hello \nworld")
    # "\r" Carriage return   ->move curser to biggining of line and over writes
print("hello \rworld")     #world
        # "hello" printed
        # "\r" moves curser back to start
        # "world" over writes "hello"
    # "\b" bakspace   ->remove one char before it
print("hello \bworld")    #helloworld
    #"\f" Form feed    ->used to move to next page in printers, in consoles, it may just show as whitespace or an empty box
print("hello \f world")     #hello  world
    # "\a" bell/alert sound{beep}  ->doesn't print anything by default, also don't beep b/c modern sys mute it auto
print("\a")
    # "\\" backslash  ->1st one as a guard for 2nd and to prind "\"
print("hello \\word")    #hello \world
    #"\'" single quote
print('it\'s mine')   # tell python to ignore the just upcomming char ie.  # '
    # "\"" double quote
print("\"quote\"")
    # "\uxxx"  unicode chars
print("\u2764")   #heart emoje
     #"\Uxxxxxxxxxxxxxxxx" long unicode chars
print("\U0001F605")  #smile emoje
    #"\---" octal value
print("\141")    #a
    #"\x---" hex value
print("\x61")    #a

# RAW STRING: a raw str is a string literal prefixed with "r" or "R" that tells the python to treat the "\" char as a literal not an escape char, i.e,
print("hello \nworld")
# Hello
# World
# BUT if we wanna print it as it is we can use the raw str concept
# print(R"hello \nworld") # hello \nworld
# print(r"hello \nworld") # hello \nworld
# BUT but but
# print(r"hello \nworld\")    # SyntaxError: unterminated string literal (detected at line 56); perhaps you escaped the end quote?
# YOU CAN'T END THE RAW STR WITH A SINGLE BACK SLASH B\C PY THINK THAT IT IS FOR ESCAPING THE CLOSING QUOTE.
# TO DO THIS
print(r"hello \nworld\\")   # hello \nworld\\
print("hello \\nworld\\")   # hello \nworld\

c="\\"  # waht is happening here is that c is a str var and in str the \ is use for escaping. so we pass two slashes to ignore the 2nd through the first, So basically c have only one slash as its value
print(c)    # \
print(f"hello {c}nworld{c}")    # hello \nworld\
# INDEXING:  ->> REPRESENTING BY [] ON LEFT SIDE
#     -9-8-7-6-5-4-3-2-1
#     J  A M A L   N A S
#     0  1 2 3 4 5 6 7 8
str="jamal nas"
print(str[0], str[6])  #j n
print(str[-9], str[-3]) #j n

# string SLICING:
    str[starting_idx : ending_idx]   # including first and excluding last
print(str[2:7])  #mal n  # 7 which is last not included
    USING INDEXES IE:
print(str[3:], str[3:5], str[:5], str[:], sep='\t')    #al nas	al	jamal	jamal nas

print(str[3:len(str)]) #up to last ->> if last idx=5 then len=6, so it print upto index 5 and skip the remeining ie.
print(str[3:23])     #same as above


# STRINGS ARE IMMUTABLE:  -. U CAN'T MAKE CHANGES
# str[5]=e
# print(str)    #error

# STRING FUNCTIONS:
str="i'm studing python"
    #1. str.endswith("xx")  -> return boolean valve true if strings ends with substr otherwise false
print(str.endswith("on"))  #true
print(str.endswith("oj"))  #false
    #str.upper() ->give all to upper case
print(str.upper())   #I'M STUDING PYTHON
    #2. str.capitalize() -> cap 1st char
print(str.capitalize())  #I'm studing python
    #3. str.replace(old, now) -> replace all occurrence of old with the new provided
print(str.replace("on","oj"))   #i'm studing pythoj
    #4. str.find(world) -> return 1st index of 1st occurrer
print(str.find("n"))  #shows index  of 1st time occurance
    #str.title()  -> cap 1st char of each world like title
print(str.title())
    #4. str,count("am") -> counts occurrence of the substr in  availible string
print(str.count("o"))  #return no.

# if i wanna acces to all functions avilible for string i can simply type "print(dir(str))" in sheveron prompt or enter string var name ie "str." pycharm will show all availible fuctions(methods)
print(str)  #i'm studing python
# if we wanna update the existin string with the change we can simply update it ie
str=str.title()  #it creat a new string obj not change the original(immutable) ie  (one line above)
print(str)  #str now bocomwe titled

# STRING PRACTICES
1. WAP TO INPUT USER 1ST NAME AND PRINTS ITS NAME
name1=input("enter your 1st name: ")    #the input func take everything as a string so if you enter some int or soecial chars it will convert it to string automatically
print(len(name1), name1, type(name1))    #9 5678945+3 <class 'str'>

2. count no.s of $ in a string
print(name1.count("$"))



#CONDITIONAL STATEMENTS:
    # IF-ELIF...-ELSE(IF NEEDED)  ->>SYNTAX(WAY OF WRITING=RULES)
    #     IF(CONDITION):                return true or false if true statement executrd
    #         STATEMENT 1
    #     ELIF(CONDITION):
    #         STATEMENT 2
    #        .
    #        .
    #        .
    #     ELSE:                                      (IF NEEDEWD)
    #         STATEMENT N                            (STATEMENT W   HICH WILL EXECUTE IF NO OF THE ABOVE CONDITION IS TRUE)


# we can write as many statement we wanna write of if, and elif
# if one sate4ment executed py will skip all remaining and go out of block
# if we write all statements with if python will execute all even if first one is executed unlike if , elif
# we use else if all condition are false and we want to do something remaining, not necessarly to be used every time

light=input("enter color ")
if light=="red":
    print("stop")
elif light=="green":
    print("go")
elif light=="yellow":
    print("look")                      #indentation->proper spacing  ->>vvv imp in py
else:
    print("light is broken")

marks=float(input("eneter marks via %: "))
if marks>=90:
    print("Grade=\"A\"")
elif marks>=80 and marks<90:
    print("Grade=\"B\"")
elif marks>=70:
    print("Grade=\"C\"")
elif marks>=60:
    print("Grade=\"D\"")
else:
    print("Grade=\"F\"")


    ### OR ####
if marks>=90:
    grade="A"
elif marks>=80:
    grade="B"
elif marks>=70:
    grade="C"
elif marks>=60:
    grade="D"
else:
    grade="F"
print("Grade of the student is ->", grade)

# NESTING -> INSIDE OTHER
age=float(input("enter you age: "))
if (age>=18):                     #if this statement become true we go inside and check for othr statement
    if age >= 80:
        status="can't drive"
    else:
        status="can drive"

else:
    status="can't drive"

print(status)

# PRACTICE
1. WAP TO CHECK IF A NO. ENTERD BY THE USER IS ODD OR EVEN
num=int(input("enter the number: "))
if num%2==0:
    print("even")
else:
    print("odd")

2. wap to find the greatest of three no.s entered by user
a,b,c=int(input("enter a: ")),int(input("enter b: ")),int(input("enter c: "))
if a>b and a>c:
    status="A is greatest"
elif b>a and b>c:
    status="B is greatest"
else:
    status="C is greatest"

print("the no. A is", a , "and" ,status)

wap to check if a no. is multiple of 7 or not
num=int(input("enter number: "))
if num%7==0:
    print(num, "is multiple of 7")
else:
    print
