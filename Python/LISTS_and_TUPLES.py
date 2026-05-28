## LEC # 03 LISTS AND TUPLES -> SORT OF EQIUILANT TYPE OF ARRAYS(having same datatype) IN OTHER LANGS
##LIST:
    #BUILT-IN DATA TYPE  THAT STORES SET(multiple) OF VALUES
    #IT CAN STORE ELEMENT OF DIFFERENT TYPE(INT, STR,ETC)
std=["jamal", "86%", "10th", "blue"]
print(std)
    #TO STORE MORE VALUES IN SINGLE VAR IE
#in vars
marks1=45
marks2=12.3
marks3=55.5
marks4=55.5  #etc
print(marks1,marks2,marks3,marks4)

std=["jamal", "94%", "10th", "blue"]
marks = [45,12.3,55.5,55.5]
both = [std, marks]
print(both) # [['jamal', '94%', '10th', 'blue'], [45, 12.3, 55.5, 55.5]]
# # # in lists
marks = [45,12.3,55.5,55.5]
# print(marks, type(marks))

#empt list
lst=[]
print(lst, type(lst))   #[] <class 'list'>
 #INDEXING:
    #SIMILER TO STR
print(marks[0],marks[1],marks[2],marks[3])
print(marks[-4],marks[-3],marks[-2],marks[-1])  # we use when don't know lenth of list/str etc

#lenght
print(len(marks))

# MUTABLE: -> WE CAN CHANGE IN IT AFTER CREATION
marks[1]=72.3    # UPDATE EXISTING LIST (marks) (AFTER THIS LINE'S EXECUTION)
print(marks[1])
print(marks)

# INDEX OUT OF RANGE ie
#print(marks[7])   #out of range

##slicing:   -> sublist
   ## LEST_NAME(STARTING_IDX:ENDING_IDX)  #ENDING_IDX IS NOT INCLUDED
print(marks[:])   #OR print(marks[:len(marks)])   -> if last idx=5 then lenght will be 6, last is not included
print(marks[:45])  # no error   [45, 12.3, 55.5, 55.5]
print(marks[-3:-1])  #[12.3, 55.5]

#to print in reverse
print(marks[::-1])

# STRING
str="jamal nasar"
print(str[:87])  # start to last no error on exeding limit
print(str[11])   # error B/C ITS NOT PRESENT


#LIST METHODS:  -> methods means d.type specific FUNCTIONS
lst=[2,1,3]
    #list.append(4)  -> add one element at end
print(lst.append(4))  # None -> void func (do something but didn't return any thing)
print(lst)      #[1, 2, 3, 4]
    #lst.sort()  ->sort in ascending order
lst.sort()
print(lst)
    #lst.reverse()  -> in descending
lst.sort(reverse=True)     #these all are updating original list
print(lst) #[4, 3, 2, 1]

#SORTING IN STRINGS:  ->ACC TO ALPHABETICAL ORDER A-Z  (1ST LETTER)
fruit=["banana", "chery", "apple"]
fruit.sort()
print(fruit)    #['apple', 'banana', 'chery']
#OR
let=['a','b','g','j','t','u']
let.sort()
print(let)
    #lst.reverse()  -> reverse list
lst.reverse()
print(lst)
    #lst.inser(idx,ele)   ->insert element at index
lst.insert(1,8)
print(lst)
lst.remove(element)   #->remove 1st occurrence of element
lst.remove(1)
print(lst)    #[2, 3]
lst.remove(2)
print(lst)   #[3]
    #list.pop(idx)  ->remove element at idx
lst.pop(0)
print(lst)   #[]  with above
lst.pop()   # remove last one
#(ctr+space-> to access methods for a D-type)



#TUPLES:
    # A BUIL-IN DATA TYPE THAT LET US BUILT CREATE IMMUTABLE SEQUENCE OF VALUES
    # TO STORE MULTIPLE VALUES IN SINGLE VAR BUT IMMUTABILY
tup=(1,2,3)
print(type(tup), tup)

#indexing
print(tup[1])   #2

#slicing
print(tup[1:3])  #(2, 3)

# but
tup[1]=6
print(tup)  #error

# empt tuple
tup0=()
print(tup0)  #()

# tuple having single char/element
# tup1=(1)
# print(tup1, type(tup1))   #1 <class 'int'>
# !!!
tup1=(1,)  # the *comma* indicates that it is a tuple
print(tup1, type(tup1))   #(1,) <class 'tuple'>

# *le ele
tupm=(1,2,3,4,) #== tupm=(1,2,3,4) # the lest comma is opptional as it is tuple determined

# slicing:
# same as in str or lists

# TUPLE METHODS:
    # TUP.INDEX(ELE)   ->RETURN INDEX OF THE 1ST OCCURANCE
print(tup.index(2))  # 1  # fruitful func ie do and return
tup.count(el)  # -> count total occurrence
print(tup.count(2))  # 1

# SINCE WE DON'T CHANGE THE VALUE OF TUPLE SO, ITERATION IN TUPLE IS FASTER THAN LIST, SO IT ENHANCE SPEED OF EXECUTION.
 #1. WAP TO ASK THE USER TO ENTER THREE NAMES OF THIER FAV MOVIES AND STORE THEM IN A LIST
mov1=input("enter name of 1st movie: ")
mov2=input("enter name of 2nd movie: ")
mov3=input("enter name of 3rd movie: ")
mov=[mov1,mov2,mov3]
print(mov)

OR
mov=[]
mov1=input("enter name of 1st movie: ")
mov2=input("enter name of 2nd movie: ")
mov3=input("enter name of 3rd movie: ")
mov.append(mov1)
mov.append(mov2)
mov.append(mov3)
print(mov)

OR
mov=[]
mov.append(input("enter name of 1st movie: "))
mov.append(input("enter name of 2nd movie: "))
mov.append(input("enter name of 3rd movie: "))
print(mov)

# * PALINDROME -> OBJ THAT ARE SAME FROM 1ST TO LAST AND LAST TO 1ST. ie.
#     RECECAR=PALINDROME
#
#2. WAP TO CHECK THAT A LIST contain PALINDROME of element OR NOT(hint: use copy mthd)
lst=[1,2,3,2,1]   # The list are palindrome.
#lst=[1,2,3,2,6]    # The list are not palindrome.
lst_copy=lst.copy()   # creat a copy in memory without updating noriginal
lst_copy.reverse()
if lst==lst_copy:
    print("The list are palindrome.")
else:
    print("The list are not palindrome.")


#3. WAP TO COUNT THE NUMBER WITH THE "A" GRADE IN THE FOLLOWING TUPLE:  ("C","D","A","A","B","","A")
tupg=("C","D","A","A","B","","A")
print(tupg.count("A"))  #3

##4. store the above values in a list & sort them from "A" tp "D"
lstg=list(tupg)
print(lstg)    #['C', 'D', 'A', 'A', 'B', '', 'A']
lstg.sort()
print(lstg)    #['', 'A', 'A', 'A', 'B', 'C', 'D']  # SPACE WILL FIRST

