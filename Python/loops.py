
## LOOPS:
    # USED TO REPEAT INSTRUCTIONS (SET NO. OF TIME)
    # 2TYPES:
        # FOR LOOP AND WHILE LOOP
        # WHILE LOOP:
            # WHILE (CONDITION):    (IF THE CONDITION IS TRUE IT WILL EXE THE STATEMENT INSIDE BODY)
                # STATEMENT TO EXECUTE
while True:
    print("jamal nasar")     # INFINITE LOOP  # no practical use
# OR
o=3
while o<6:  # which will always true b/c we are initiate by 3
    print(o)
    o-=1
x=0 # ITERATOR  # ITERATION-> CHAKAR
while x<=100:     # GREATER THAN "OR" EQUAL TO  -> IF ONE IS TRUE THEN CONDITION WILL TRUE i.e if equal or graeter/lesser
    print(str(x)+". HELLO! ")    #
    x=x+1   #

# printing no. 1 to 5
i=1
while i<=5:
    print(i)
    i=i+1   # increment
# # in reverese
i=5
while i>=1:
    print(i)
    i-=1
print("loop ened")


## LET'S PRACTICE:
#1. PRINT N0.S FROM 1 TO 100
x=100
while x>=1:   # INDICATES SOPPING OF CODE
    print(x)
    x=x-1

#3. print multiplication tale a no. "N
# let n=5
i=int(input("Enter the no. you want table upto 16: "))
x=1
k=1
while x<=16:
    print(f"{k}). {x*i}")
    k=k+1
    x+=1

#4. print the element of a list using a loop
lst=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(lst):
    print(lst[i])
    i=i+1

""" WHILE LOOP:
        1ST WE INITIALIOZE A VARIABLE, THEN WE MAKE CERTAIN CONDITIONN WHICH DETERMINES UPTO WHICH THE LOOP WILL RUN.
        THEN WE SPECIFY THE STATEMENTS WE WANNA EXECUTE ON TRUEING OF THAT CONDITION CERTAIN NO. OF TIME."""

### *** THE CONDITION SHOULD BE BASED ON "UPTO WHAT YOU WANNA RUN IT".

# BREAK AND CONTINUE -> KEYWORDS
    # break:
        # used to terminate the loop when encounter.
i=1
while i<=5:
    print(i)
    if i==3:
        print("it is broke")
        break   # nothing happens after break in a block
    i=i+1

    # continue:
        #terminates execution in the current iteration & continue execution of the loop with the next iteration.

i=1
while i<=5:
    print(i)
    if i==3:
        i = i + 1     # as the last line does'nt exe so i will always 3 and thus it will become an infinite loop from here
        print("it is continue")
        continue   # skip the upcomming statements in this iteration
    i=i+1

i=0     # we define intialization
while i <= 10:      # we define end
    if i%2!=0:
        i = i + 1
        continue
    print(i)
    i=i+1

## FOR LOOP:
    # USED FOR SEQUENTIAL TRAVERSAL (TRAVEL IN SEQUENCE)
    # FOR TRAVELING LIST, STR,TUP ETC IN SEQUENCE ONE AFTER ONE
    # SYnTAX
        # FOR el IN lst:
            # statement
        # else:     (optional)      # only exe if loop run and without break
            # work when loop ends
lst=[1,2,3,4,5]
for num in lst:
    print(num)
# or using range func
for i in range(5):
    print(i)
str='jamal nasar'
for chars in str:
    print(chars)
else:
    print("This is break! ")

# PRACTICE:
#1. PRINT THE ELEMENT OF A LIST
lst=[1,4,9,16,18,0,123]
for i in lst:
    print(i)

#2. search for a num x in the tuple                 # this is linear search
tup=(1,4,9,16,18,0,123)
x=int(input("enter the number: "))
idx=0
for i in tup:
    idx = idx + 1
    if i==x:
        print(x, "is present in the list at index",idx)
        # break      -> only if i wanna found it once and then break the loop


## RANGE()
    # RANGE RETURN A SEQUENCE OF NO.S, STARTING FROM 0 BY DEFAULT, AN DINCREMENT BY 1 (BY DEFAULT), AND STOP BEFORE A SPECIFIED NO. (EXCLUDING LAST NO.)
        # range(START,STOP,STEP)
print(range(5)) # range(0, 5)  # START=0(optional)  # STOP=5  # STEP=1 ( optional/ if need)
x=range(0, 5)
print(x) # range(0, 5)
print(x[:]) # range(0, 5)

g=range(0,12)  # start and stop
d=range(0,12,2) # start and stop and step size
print(g,d)  # range(0, 12) range(0, 12, 2)

for i in x:
    print(i)    #  0,1,2,3,4
# OR
for i in range(10): #bstop    -> start and step =by default 0 and 1 respictively
    print(i)    # excluding 10

## PRACTICE
#1. WAP TO PRIN NO. FROM 1 TO 100
for i in range(101):
    print(i)

#2. print no. from 100 to 1
for i in range(100,-1,-1):      # start at 100 go to -1 (which will not included) and step -1 each time
    print(i)


#3. wap to print multiplication table of a no.
n=int(input("enter a no. "))
for i in range(1,17):
    print(i*n)

# ## PASS STATEMENT:
    # PASS MEANS NULL
    # PASS IS A NULL STATEMENT THAT DO NOTHING. IT IS JUST A PLACEHOLDER FOR FUTURE CODE
    # SYNTAX
        # FOR el IN RANGE(10):
            # PASS

# IF I NEED TO WRITE AN EMPTY LOOP   -> NO INSTRUCTION
for i in range(10):
    #empty

print("useful work")        # IndentationError: expected an indented block after 'for' statement on line 165
an error happend and after the mpt loop my useful work remain un exe s0. to silve:
for i in range(10):
    pass

print("useful work")        # useful work

# we can use pass in conditional too:
x=6
if x>7:
    pass

# we also use pass in excerption


PRACTICE
# WAP TO PRINT SUM OF 1ST N NATURAL NO.
n=int(input("enter n: "))
i=0
sum=0
while i<=n:
    sum=i+sum
    i=i+1
print(sum)

# FOR
add=0
for i in range(1,n+1):
    add=add+i
print(add)


