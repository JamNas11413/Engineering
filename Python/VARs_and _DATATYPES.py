# LEC1 VARs AND DATATYPES


# whitespaces->tab, newline, blank space
# WHAT IS A VARIABLE?
#     VAR IS A CONTAINER WHERE U CAN PUT VALUES, THE VALUE WILL STORE IN MEMORY AT A PARTICULAR ADDRESS; THE NAME OF THE VAR IS THE REFERENCE TO THE MEMORY OCCUPIED BY THE VALUE.
#     WE BUILT ONE WITH ASSIGNMENT STATEMENT
#     AS THEY ARE VARS WE CAN CHANGE ITS VALUE; IF WE UPDATE THE VAR WE WILL GET OLD AND UPDATED VALUE ACC TO THE FLOW OF EXECUTION
# WHY WE NEED VARIABLES?
#     FOR STORING DATA BY NAME AND MANIPULATING IT LATER
print("I am jamal kamal.\n"+"I love programming.")
print("\n11413")
x="\n11413"
print(type(x))
p=type(x)`
print(p)
# o=int(x)   #o isn't 54 now
print(o+1)
print(23+87*7%98-9867//5/5)
o=54
# print(o)     #updated from now    -=> flow of execution ->> top to bottom and left to right //one line at a time(interpreter)

f=5   #valve of right goes into var on left
w=78
y=w
print(y,w)  #same


# IDENTIFIERS->> RULES: -->>> name of vars, func etc
#                    can be upper, lower letter, digits,or _
#                    can't start with digits
#                    can't use special chars
#                    can be of any lenght
#               gen:
#                    A-Z,a-z,0-9,_...(lenght)
#               should have:
#                    simple
#                    short
#                    *meaningful->price, name etc(nemonically)

v=6.4      #nemonically typed lang-->>type determine as you pass valve from the right

print(type(v))
type(v)  #fruitful func_> do return a value ie.
r=type(v)
print(r)

# VOID FUNC:
#      perform an action ie having some side eefct
#      but doesn't return a value
#      eg:
#      result=print("hello")
#      print('rsult")
#      # hello None    ->>> u can not use result latter
#
#
# FRUITFUL FUNC:
#       returns a value you can store or pass around
#       ie n=type()
#       print(N)
#       # cls ---    ->>> we can now use n as a variable


# pecificDATA TYPES:
t=7          ##int
d=4.67           ##float
f=4.87           ##str
b=True, False     ## boolean
N=None        ##NoneType(it has only one object => None)

print(N, b, sep='\n')
print(type(N), type(d), type(f), type(b))

# RESERVED WORDS::KEYWORDS
                #PRE DEFINED NAME that is used for something s
#case sansitive == python ie True != true

##PB1:
A=3
E=5
sum=A+E
print(sum)


# single3 line comment #
# multi line comment """"""
#shortcut ctr+/ to comment out selected

#OPERATORS:-->> SIGH THAT PERFORM SOME OPERATION ON OPERANDS
       #1.Arithmatic operators:  +-*/,//%**
       #2.Relational/Comparison operators:    ==,!=,<>,<=,>+
       #3.Assignment operators:     =,+=,-=,*=,/=,%=,**=    (a+=1)
       #4.Logical operators:   not, and, or


      # 2. return true or false
      #3.  return true or false
          #         |
           #        ^
           # use in conditionals b/c it gives true if condition is coorrect and vice versa.
        #4. loops--> incrementing/decrementing etc

num = 10
num //= 2             #floor + assign  -. updating var
print(num)
            ## 4.a not: will return opposite ie
c=not True
print(c)        #false
            ##4.b and:  return true if both values are true ie
c=True and True
print(c)               #true
             ##4.c or:  return true if  ATLEAST one of them is true
c=True or False
print(c)

# exercise1
c=not True and True
print(c)  #false
exercise2
a,b,c,d=1,2,3,4

c=a<b and c<d        #true b/c both are true
print(c)
c=a<b and c>d     #false b/c one of them is false
print(c)

c=a<b or c>d      #truye b/c one of them is ture
print(c)
c=a<b or c<d        ##truye b/c BOTH of them ARE ture
print(c)
c=a>b or c>d
print(c)         #FALSE B/C BOTH ARE FALSE


num=0
print(not(num))   # true b/c 0 is consider false
user=None
if not(user):
    print("no user found.")
c=not True     #opposite
print(c)


# TYPE CONVERSION:
        # 2 TYPES:
             # 1. TYPE CONVERSION
                # PYTHON DO IT AUTOMATICALLY
            # 2. TYPE CASTING:
                # WE DO IT MANUALLY

a=2
b=4.6
sum=a+b     #python convert "a" into float b/c float is superior(b/c store more data) from int     2.0+4.6=6.6
print(sum)   #this is type conversion

but
a=int("2")   #a="2"  (initially)
b=4.6
sum=a+b
print(sum)   #error b/c concatination of two str possible not of float and str
# but if we want we can convert the str 2 into int MANUALLY
# type casting into int  (above)
print(sum)    #this is type casting

#cast to str
a=8765
s=str(a)
print(type(a),s ,sep="\n")

#INPUT IN PYTHON:
         # INPUT()  -->> TO TAKE INPUT FROM USER THROUGH INPUTR DEVICE(KEYBOARD)
         # GIVE STR DATA TYPE BY DEFAULT SO WE CONVERT IF NEED
         #IT ALSO PROMPT SOMETHING (PRINT SOMETHING)

name=input("enter your name plz! ")
print("Welcome!",name)
print(f"Welcome! {name}")

print(type(name))   # str even if i enter int

##type casting to float
a,b=float(input("enter first number ")),float(input("enter second number "))
sum=a+b
print(sum)


 # PRACTICE
#1: WRITE A PROGRAME TO INPUT TWO NO. AND PRINT THRIR SUM
no1=float(input("Please enter 1st no."))
no2=float(input("Please enter 2nd no."))
sum=no1+no2
print(sum)

#2: WAP  to input teo floating point no. and print their average
no1=float(input("Please enter 1st no."))
no2=float(input("Please enter 2nd no."))
avg=(no1+no2)/2
print(avg)

#3: WAP TO INPUT 2 INT NO., A AND B. PRINT TRUE IF A IS GREATERTTHAN OR EQUAL TO B. IF NOT PRINT FALSE
a=int(input('enter a '))
b=int(input('enter b '))
h=a>=b
print(h)        # return true b/c comparision operators return boolean valves

#4: WAP TO INPUT SIDE OF A SQUARE AND PRINT ITS AREA.
side = float(input("Enter the side of the square in cm: "))
print(f"The area of the square is: {side * side}cm^2")



# ````````````




# CONTANTS:
#     in python we don't have a way to make consttant(like js const) but we can use type innotation along with the capslock naming convention to show that it is  const

CONST: str = "dsfghj"
# or 
CONST = "bbhbhbh"

it is not really a const as we can change it values but it is for us to show that it should be treated like  c0nst