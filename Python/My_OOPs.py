# ##OOps:    OBJECT-ORIENTED PROGRAMMING SYSTEM
#     # TO MAPE REAL WORLD SCENARIO, WE STARTED USING OBJECTS IN CODE.
#     # THIS IS CALLED OOPs
#
#     # 1ST WE DOES PROCEDURAL PROGRAMMING
#     # I.E:
# s=4
# x=2
# sum = s+x
# print(sum)
#         # the statement will execute onle line after one this is called procrdural (execution in a sequence)
#     # then we started using function(block ob code that execute when call)
#         # due to it we can reduce redundancy and increase reusabilty
#     # we can also level up from function to even encrease more reusabilty and write structered code
#     # through a programming pattern known as OOPs
#




# # Object:
#     # as evry thing is an object in real world, we can also make everything obj in python, but for it we have to define classes first for the obj
#     # we already deal with obj, i.e. list is an class we maked an lst collection data structer to access the class through the obj
# lsr=list()  # we create an object of list class called lst
# # classes:
#     # class is a blue print for an obj(what will be in the object)
# # creating class
# class Students: # name of the class should be start from an opper case letter
#     name="JamNas"   # let every std will have this name
# # to use the class and manipjulate the data inside it we have to define objects for the class
# #creating obj(instance) -> for the blueprints
# s1=Students()   # s1 is a varible which is an object, obj=>var=name of class+parenthesis[()]
# print(s1)   # <__main__.Students object at 0x00000284218A6F90>  # means that it is an obj at this location in memory of class Student
# # if i wanna print the nam eof my std one
# print(s1.name) # JamNas
# # creating 2ng obj
# s2=Students()
# print(s2.name)  # JamNas   # as for every std we have the same name
#
# ##$$$ && *** the type fo every object is the name of its class i.e, the above obj(s1) is of type Student-> meaning that its a student
#
#
# #another class
# class Car:      # blue print for my car
#     color = "red"   # i want all cars red
#     brand = "BMW"
#     # PROPERTIES OF MY CAR BLUE PRINT
# # object
# car1=Car()
# print(car1.color,car1.brand) # red BMW
#
# ## CONSTRUCTER=__INIT__(): FUNCTION     # init is short for initialization
#     # IT INVOKE/EXECUTE AT TIME OF OBJ CREATION
#     # ALL HAVE A FUNC CALLED THE __INIT__() FUNC, WHICH IS ALWAYS EXECUTED WHEN THE OBJECT IS  BEING INITIATED.
#     # AS WE DIDN'T WRITE IT IN ABOVE EG BUT IT IS STILL EXECUTED BY THE PYTHON (WILL ALWAYS EXCUTE)
#
# class Students:
#
#     def __init__(self): # the constructer always take a perameter called the "self"
#         print("Initializing Students")
# s1=Students() # as we created our s1 obj the init func called automatically     # when we write name class with parenthesis; the parenthesis is for calling thje constructer
# # self is a refrence for the object
# # if i run: # initializing Students # we didn't call the obj but the object callled it
#
# class Students:
#
#     def __init__(self):
#         print(self) # <__main__.Students object at 0x000001EFEA416F90> # same addres as of s1 # so it means that the two name refrences to same thing in memory
#         print("Initializing Students")
# s1=Students()
# # self == object (at time ( the running one))
#
# # we can also take multiple perameters
# class Students:
#
#     def __init__(self, name):   # self will always the first perameter
#         self.Name = name    # the one with self i.e. "Name" is the name of my variable            # GENERALLY SAME NAME FOR THE PERAMETER AND VARIABLE IS A GOOD IDEA/CHOICE I.E self.name = name
#         print(name) # inside func i can't play with my variables so i do for perameters
#         print(self.Name) #%$ same as above
# s1=Students("Maryam:-> my love")
# print(s1.Name)  # having same value as above of name perameter
#
# ## ** the SELF PREFIX FOR MY VARS OF CLASS IS ACTUALLY REFERING TO THE OBJECT
# # SELF.NAME == S1.NAME==NAME OF CURRENT ONJ
#
#
# ## if we didn't define our constructer python will do it by it self
# ##we can also kept name of the self perameter as we want
# class Students:
#
#     def __init__(abcd, name):   # we gave name to our obj but generally self is good choice # THE "name"==WHICH IS PASSED IN THE PERAMETER AND "Name" == OBJECT'S NAME
#         abcd.Name = name
#         print(abcd.Name)    # jmaal
# s1=Students("jamal")
# print(s1.Name)
#
# # # the self perameter is  reference to the current obj/instance of the class, and is used to access variables that belongs to the class(inside the class)
# # print(self.Name)  # error b/c self outside the clas doesn't work
# # object name is used as a prefix to access vars of obj  outside class
#
# # 2nd obj
# s2=Students("ijaz")
# print(s2.Name)
#
# ## if i run this class
# # jamal
# # jamal
# # ijaz
# # ijaz
#
# ## mechanism:
# """ we created class Students but for using the class we maked objects (s1 and s2) now the class willl executed when the obj calls th init func
#  and it become initialize, 1stly the s1 obj called the init func by passing an argument(as the init func take two arguments self and name, the self is refrence to the current object itself so we  will pass only one argument )
#   it will take the pass argument and execute the func using this argument and when the functon execution is completed, it comes outside the classs and execute statements after the call.  SIMILARLY, for the other obj.  """
#
# # the constructer is calling with every new obj acc to flow of execution
#
# ## ATTRIBUTES:
#     # THE DATA/VARS WE STORE IN THE CLASS OR OBJ ERE KNOWN AS ATTRIBUTES
#     # DATA/VARIABLES(IN ANY OTHER PATTERN)==ATTRIBUTES(IN OOPS)
#
#
#
#
# # practice:
# class Student:
#     def __init__(self, name,subject,marks):
#         self.name = name
#         self.subject = subject
#         self.marks = marks
#         print(f"{self.name} score: {self.marks} in {self.subject}")
#
#
#     # def get_score(self,sub,marks):
#     #     self.subject = sub
#     #     self.marks = marks
#     #
#     # def print_score(self):
#     #     print(f"{self.name} score: {self.marks} in {self.subject}")

# std1=Student(input("Enter Student Name: "),input("Enter Subject: "),input("Enter Marks: "))
# # std1.get_score(input("Enter Subject: "),input("Enter Marks: "))
# # std1.print_score()
#
# class Account:
#     def __init__(self, name,account_no, balance):
#         self.account_no = account_no
#         self.name = name
#         self.balance = balance
#
#     # def credit(self,amount_credit):
#     #     self.balance += amount_credit
#     #
#     # def debit(self,amount_debit):
#     #     self.balance -= amount_debit
#     #
#     # def all_record(self):
#     #     print(f"dear, {self.name} with acc no. {self.account_no} your current ballence is: {self.balance}")
#
#
# cus1 = Account("Jamal Nasar", 15327286366166762, 100000 )
# # cus1.credit(2343)
# # cus1.debit(3476)
# # cus1.all_record()
#
#
#
# # THE INFO WE INITIALIZE THE CLASS BY(__INIT__(INFO)) WILL COMMON FOR ALL IBJECTS
# ## CONSTRUCTER:
#     # TWO CATEGORIES:
#         # 1.) DEFAULT COMSTRUCTER->HAVING ONLY THE SELF PERAMETER
# class Account:
#     def __init__(self): # -> default constructer
#         pass
#                 # if we didn't define it, python will do it automatically by itself but this will run/executed
#
#
#         # 2.) perametarized constructer:-> having perameters other than self
#  def __init__(self, name,account_no, balance):  # -> perametarized constructer
#         self.account_no = account_no
#         self.name = name
#         self.balance = balance
#
#
#     # if i write both in one class?
# class Account:
#     def __init__(self): # -> default constructer
#         pass
#
#     def __init__(self, name,account_no, balance):     #-> perametarized
#         self.account_no = account_no
#         self.name = name
#         self.balance = balance
#         print(f"dear, {self.name} with acc no. {self.account_no} your current ballence is: {self.balance}")
#
# cus1 = Account("Jamal Nasar", 15327286366166762, 100000 )
# ## the perametarized one will execute-> which mathched with my argument passed
# #  the default one will ignore
#
#
# # gdhggdghgfh jhhsjdhhjadfsh h ->>> we have fife errors in this line b\c 1 bug for 1st word (gdhggdghgfh), one for the empty space b\w 2nd and 1st word as pyhon thinks that there is a miss operator, similarly for remaining.
#
# # TYPES OF ATTRIBUTES:
#     # 1.) CLASS ATTRIBUTES
#         # COMMON FOR ALL OBJECT,  REP: CLASS.ATTR
#             # NAME OF SCHOOL FOR STDS
#     # 2.) OBJ\INSTANCE VARIABLE\ATTRIBUTES
#         # ONLY FOR THE OBJECT TO WHICH THE SELF IS REFERING, REP: SELF.ATTR (INSUDE THE CLASS), OBJ.ATTR(OUTSIDE THE CLASS)
#             # NAME OF EVERY STD
# # EVERY OBJECT OCCUPY SEPARETE SPACE IN MEMORY -->> SO OBJ ATTR  WILL STORE SEPARATELY FOR EACH OBJ AND CLASS.ATTR WILL STORE ONLY ONCE FOR ALL OBJ
# class Students:
#     school_name="tipu shaheed school and college kabal swat"    #--->>> class attributes
#     def __init__(self, name, score):
#         self.name = name    #-> obj attributes
#         self.score = score
#         print("Initializing Students")
# s1=Students("MARYAM BIBI", 98)
# print(s1.school_name,Students.school_name)  # tipu shaheed school and college kabal swat tipu shaheed school and college kabal swat
# ## same for both obj and class attr respectively
#
#
# ## IF I HAVE SAME OBJ AND CLASS ATTRIBUTES
# class Students:
#     school_name="tipu shaheed school and college kabal swat"
#     def __init__(self, name, score,school_name):
#         self.name = name
#         self.score = score
#         self.school_name = school_name
# s1=Students("MARYAM BIBI", 98,"KABAL MODEL")
# print(s1.school_name,Students.school_name)  # KABAL MODEL tipu shaheed school and college kabal swat
# #BUTTTTTT
# class Students:
#     school_name="tipu shaheed school and college kabal swat"
#     name="annonymous"
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
# s1=Students("MARYAM BIBI", 98)
# print(s1.name)  #MARYAM BIBI
# ##** usually object attr have high precedence value than class-> so it print out the one of obj
# # obj.attr > class.attr
#
#
#  ## METHODS:
#     # CLASS HAVE TWO THING: ATTRIBUTES(PROPERTIES)-> WHAT IT HAVE, AND METHODS(FUNCTIONS)->WHAT IT CAN DO
#     # METHODS==FUNCTION, FUNCTIONS ARE KNOWN AS METHODS IN OOPs
#     # METHODS ARE FUNCTIONS THAT BELONG TO OBJECT.
#     #
#
#     # UPTO NOW ANY METHOD THA WE USE FOR A DTA TYPE i.e, LIST METHODS:
#         # LIST IS A BUILT-IN CLASS AND WE USED ITS METHODS, SO WE MAKED OBJ TO USE THE METHODS OF CLASS  i.e, LST=[6,7,,8,9]-> OBJ OF LIST
# # SYNTAX:
# """      DEF MTHD_NAME(SELF):    # ALWAYS PASS THE SELF PERAMETER
#             STATEMENTS
#
#
# OBJ_NAME.MTHD_NAME(args_if)"""      # -> CALL FOR THE OBJ
#
# class Persion:
#     def __init__(self, name):
#         self.name = name
#
#     def hello(self,Class):                ## this is an error b\c we have to write argoment anme in lower case
#         self.Class = Class
#         return print(f"Hello! {self.name} to {self.Class}")
#
# person1 = Persion("Jamal Nasar")
# person1.hello("10th blue")
#
#
#
# ## practice:
# # create a student class takes namwe & marks of 3 sub as args in constructor. then create a method to print he avg.
#
#
#
#
#
# ## STATIC METHODS:
#     # METHODS THAT DON'T USE THE SELF PERAMETER IN OOPs.
#     # BUT IF WE DON'T WANNA USE THE SELF->> THEN WE CAN MAKE IT STATIC MTHD
#     # SELF IS USED FOR OBJECTS BUT IF WE DONT CREATE AN OBJECT, THEN WE DON'T WANT THE SELF(AS IT DEFINED BY DEFAULT IN CONSTRUCTOR)  IE. EG #1
#   #  in that case when we create a methd at class level -> its called static methd
# EG1:
# class Static:
#     def static_methd():
#         print("it's a Static Method, BYEEEEE")
# Static.static_methd()   #it's a Static Method, BYEEEEE
# class Persion:
#     def __init__(self, name):
#         self.name = name
#
#     def hello(self,dlass):
#         self.dlass = dlass
#         return print(f"Hello! {self.name} to {self.dlass}")
#
#     def static_methd():
#         print("it's a Static Method, BYEEEEE")
#
#
# person1 = Persion("Jamal Nasar")
# person1.hello("10th blue")
# person1.static_methd()
#
# ## THE ABOVE PROGRAME IS EXCUTED UPTO THE FIRST DEFINED METHOD AND SHOW AN ERROR IN EXECUTION OF 2ND ONE
# # THIS IS B\C 1ST PERAMETER OF ANY CLASS METHOD SHOULD HAVE "SELF "
# ## OUTPUT:
#
#
# #Hello! Jamal Nasar to 10th blue
# # Traceback (most recent call last):
# #   File "C:\Users\SALAMAN COMPUTERS\PycharmProjects\Apna_College\Apna_College\My_OOPs.py", line 292, in <module>
# #     person1.static_methd()
# #     ~~~~~~~~~~~~~~~~~~~~^^
# # TypeError: Persion.static_methd() takes 0 positional arguments but 1 was given
#
#
# # BUT: the more good way will to create a static mthd
# class Persion:
#     def __init__(self, name):
#         self.name = name
#
#     def hello(self,dlass):
#         self.dlass = dlass
#         return print(f"Hello! {self.name} to {self.dlass}")
#     @staticmethod               # its a decorater       # it coverts a method to be a static methd
#     def static_methd():
#         print("it's a Static Method, BYEEEEE")
#
#
# person1 = Persion("Jamal Nasar")
# person1.hello("10th blue")
# person1.static_methd()
# # output:
# # Hello! Jamal Nasar to 10th blue
# # it's a Static Method, BYEEEEE
#
# # decorator:
#     # decoraters allows us to wrape another func in order to extend the behaviour of the wrapped func, without permanently modifying it.
#     # in simple words, there a func that take a function as argument, change its behavior and also return function as a result and the func is decorator
#
# # so if we have a method that don't need any instance(self), we can bring it to class level and we can make that method a static mthd by the decorator.
#
#
# #***
# ## OOPs:-> FOUR PILLURS\COLLUMNS OF OBJECT ORIENTATION
#     # 1.)-> ABSTRACTION
#     # 2.)-> ENCAPSULATION
#     # 3.)-> INHERITANCE
#     # 4.)-> POLYMORPHISM
#
# # 1): ABSTRACTION
#     # ABSTRACT==HIDE\NOT CLEAR
#     # HIDDING THE IMPLEMENTATION DETAILS OF A CLASS AND ONLY SHOWING THE IMPORTANT\ESSENTIAL FEATURES TO THE USER.
#     # UN-NECESSARY == HIDE and NECESSARY == SHOW
#         # i.e WHEN A CAR STARTS  THE DRIVER DOM'T KNOW WHAT HAPPENING IN THE ENGINE
#         # SO CAR MANIFACTURER HIDE THE IMPLEMENTATIOPN DETAILS AND O0NLY SHOW THE INTERACTION PART
#
# class Car:
#     def __init__(self):     # when our class will initialize in that time it will be un-start
#         self.acc = False        # un pressed
#         self.clutch= False
#         self.brk = False
#         print("you didn't stat it yet...")
#
#     def start_car(self):
#         self.acc = True
#         self.clutch = True
#         for i in range(5): print("          .")
#         print("\nCar is started, so far...")
#
# car1 = Car()
# car1.start_car()    # to start my car
#
# # # assume that its an automatic car i didn't see what is happening in class\engine, that all unnecessary stuff is inside the class not outside
# # i only saw the car start method not what it doing in background
# #
# #
# # 2): ENCAPSULATION:
# #    CAPSULE = WE MAKE CAPSULE OF DATA+METHODS==INSTANCE\OBJECT
# #    ENCAPSULATION IS WRAPPING DATA AND RELATED FUNCTIONS INTO A SINGLE UNIT(OBJECT).
# #        AN OBJ HAVE ITS OWN DATA AND ITS FUNCTIONS WHICH ARE ALL WRAPPED IN IT
#
#
#
# ### practice:
# # CREATE ACCOUNT CLASS WITH TWO ATTRIBUTES - BALLANCE AND ACCOUNT NO. CREATE METHODS FOR DEBIT (SUBTRACTING VALUE\TACKING OUT VALUE\-VE VALUE) CREDIT (ADDING VALUE\PUT INTO VALUE\+VE VALUE) & PRINTING THE BALLENCE.
#
#
# ## All power is within you; You can do anything and everything.
#
# #***
# ## OOPS ==> Object-Oriented Programming System
#
# ## object have:   2 things;
#     # 1)-> what it have => properties \ data \ variables
#     # 2)-> what it can do => methods \ functions
#
#     #program have two things:
#     #1) CODE-->STATEMENTS, EXECUTION, AND FUNCTIONS ETC.
#     #2) DATA--> VARIABLE WHICH IS USED\ MANIPULATE BY THE FUNCTIONS
# ##
# ## DEL KEYWOR:
#     # ANY OBJECT WE CREATE IN PYTHON IT OCCUPY SOME SPACE IN MEMEORY(OBJ HAVE DATA AND ITS METHOD,SO IT TAKE SPACE IN MEMORY) AS OTHER DATA STRUCTER WE CAN DELETE IT
#     # THE DEL KEYWORD IS USED TO DELETE PROPERTIES(attributes) OR OBJECT ITSELF
# class Student:
#     def __init__(self, name,marks):
#         self.name = name
#         self.score = marks
#
#
# s1=Student("Jamal Nasar of CS department",956)
# print(s1.name,s1.score) #Jamal Nasar of CS department 956
# ## deleting object
# # del s1
# # print(s1)   #NameError: name 's1' is not defined -> as we deleted s1
# ## deleting property\attributes/data fron an obj
# del s1.name # syntax
# print(s1.score)
# print(s1.name)      #AttributeError: 'Student' object has no attrib


## PRIVATE (LIKE) ATTRIBUTES & METHODS
# conceptual implementation
#   # private methods and attributes are meant to be used only within class and are not accessible from outside the class
    # IN OTHER LANGUAGES WE HAVE CONCEPTS OF PUBLIC AND PRIVATE METHODS AND ATTRIBUTES; PUBLIC(WE CAN ACCESS IT OUT OF THE SCOPE OF CLASS ) & PRIVATE (WE CAN ONLY ACCESS IT INSIDE OUR CLASS)
    # but
    # IN PYTHON

# class Account:
#     def __init__(self, account_no, password):
#         self.account_no = account_no
#         self.password = password
#
# cus1=Account(7647634768478, 2468)
# print(cus1.account_no)
# print(cus1.password)
# i don't wanna make the passward accessable to anyone(out of the class) b\c it can be stolen are can be changed.
# so i can make my attr private in order to protect confidendial info
# and we do that in pyhton by entering double underscore  before the attr
#
#
# class Account:
#     def __init__(self, account_no, password):
#         self.account_no = account_no
#         self.__password = password
#
# cus1=Account(7647634768478, 2468)
# print(cus1.account_no)
# print(cus1.__password)  # AttributeError: 'Account' object has no attribute '__password'
# but i can access it inside my class ie :
# class Account:
#     def __init__(self, account_no, password):
#         self.account_no = account_no
#         self.__password = password
#
#     def printing_pass(self):
#         print(self.__password)
#
# cus1=Account(7647634768478, 2468)
# print(cus1.account_no)
# print(cus1.printing_pass()) # in this way i can acces it inside my class
#
#
## privatization in python doesn't  works exactly like how it works in other languages
# in pyhon we implement this conceptualy; it means that it will not fully private it will private like
#
#
# method privatization:
# class Account:
#     def __init__(self, account_no, password):
#         self.account_no = account_no
#         self.__password = password
#
#     def __pvt_methd(self):      # coceptually privated
#         print("Hey! its me, the PVT one. BYE...")
#
# cus1=Account(7647634768478, 2468)
# print(cus1.account_no)
# print(cus1.__pvt_methd())   # AttributeError: 'Account' object has no attribute '__pvt_methd'
#
# # we usualy make a private method that we wanna used by another method in the class
# # ie:
# class Hello:
#
#     def __init__(self,name):
#         self.name=name
#
#     def __hello(self):
#         print("Hello! Mr.", self.name)
#
#     def welcome(self):
#         self.__hello()
#
#
# pers1=Hello()
# pers1.welcome()     # this function will call the privated one inside the class
# "Jamal Qadar"
#
#
#
# ## COLUMNS-->OOPS
# ## 3) INHERITANCE:
#     # FROM  ONE GENERATION OF CLASS WE PASS SOMETHING TO NEXT GENERATION OF CLASS:
#         # CLASS PARRENT -------------> CHILD\NEW CLASS
#     # WHEN ONE CLASS(child \ derived) DERIVES THE PROPERTIES(attributes) & METHODS OF ANOTHER CLASS(parent \ base)
#         # CLASS CAR:
#         #     BRAND="JAMALIA"
#             # START CAR()
#             # STOP_CAR()
#             # ACC+CAR()
#
#
#      #syntax:   class nw_class(_passing name of parent class_):   -->> all the props and methds of parent class are now part of the child class.
#         # CLASS ToyotaCar(Car):         #-> having all the attributes and methods of the parent (Car) class(as we don't wanna write the methods and properties of Car class again in our new class-> sowe simply inherite that to our new class )
#
#      # base \ parent class:
#         # which is the donner of props and mthds.   OR from which the chiled class derived.
#
#     # derived \ chiled clas:
#         # which accepts the props and methds of parent class. OR which are derived from base class.
#
# # parent class
# class Car:
#     color = "red"
#     @staticmethod
#     def start_car():
#         print("Car is starting...")
#
#     @staticmethod
#     def stop_car():
#         print("Car is stopping...")
#  # child class
# class ToyotaCar(Car):
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#
# car1=ToyotaCar("kharchunar", 2025)
# print(car1.brand)   # kharchunar
# print(car1.start_car()) # Car is starting...        # b\c all data and code of the program of the 1st class is now part of our new class too
# print(car1.color)   #red
#
# ## SO WE INHERITE CAR TO TOYOTACAR
#
# ## TYPES OF INHERITANCE:
#     # 1) SINGLE INHERITANCE \ SINGLE LEVEL INHERITANCE
#         # FROM ONE BASE CLASS -------> ONE DERIVED CLASS
# class Car:                  # ONE PARENT CLASS
#     color = "red"
#     @staticmethod
#     def start_car():
#         print("Car is starting...")
#
#     @staticmethod
#     def stop_car():
#         print("Car is stopping...")
# class ToyotaCar(Car):                       # ONE DERIVED CLASS
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#
# car1=ToyotaCar("kharchunar", 2025)
# print(car1.brand)
# print(car1.start_car())
#
#
#      # 2) MULTI-LEVEL INHERITANCE
#         # BASE CLASS -----> DERIVED CLASS...(*)
#             # DERIVED (NOW PARENT)...(*) -----> DERIVED-DERIVED CLASS...(@){CHILED OF (*)}
#                 # DERIVED-DERIVED CLASS...(@){NOW PARENT} -----> DERIVED-DERIVED-DERIVED CLASS...($){CHILED OF(@)}
#                     # and so on...
#                     # IT MEANS THAT:
#                     # BASE CLASS + DERIVED CLASS...(*) + DERIVED-DERIVED CLASS...(@) ---------->  DERIVED-DERIVED-DERIVED CLASS...($)
#                         # CONTAINING ALL DATA AND METHODS OG ALL PARENT CLASSES IN THE CHILD MOST CLASS(DERIVED-DERIVED-DERIVED CLASS...($) )
#
# class Car:                  # PARENT CLASS
#
#     @staticmethod
#     def start_car():
#         print("Car is starting...")
#
#     @staticmethod
#     def stop_car():
#         print("Car is stopping...")
# class ToyotaCar(Car):                       # DERIVED CLASS(*)          (level 1)
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#
# class Prius(ToyotaCar):         # derived derived class(@)                  (level 2)
#     def __init__(self,type):
#         self.type = type
#
# ## 1st we inherite Car to ToyatCar then ToyotaCar to Prius  ----> prius will have all attr and methds of ToyotaCar, which have all of Car so, eventually all the props and mthds go to Prius(containg of both parrent classes)
# car1=Prius("electric")
# car1.start_car()        # Car is starting...        # method of parent most class now in child most
#
#
#         # 3) MULTIPLE INHERITANCE
#             # BASE1 + BASE2... ----> DERIVED    (MULTIPLE PARENT TO ONE DERIVED)
# class A:
#     varA="welcm to class 'A'"               # we didn't created our constructor so py will do it by default(default constructor)
#
# class B:
#     varB="welcm to class 'B'"
#
# class C(A,B):       # aprent classes sep by comma
#     varC="welcm to class 'C'"
#
# # creating obj of C
# objC=C()
# print(objC.varA)    # welcm to class 'A'
# print(objC.varB, objC.varC, sep=", ")     # welcm to class 'B' ,  welcm to class 'C'        # sep has comma and space
# B doesn't contain A but C contain A and B
#
#
#
# ## SUPER() method:
#     # SUPER() METHOD IS USED TO ACCESS METHODS OF PARENT CLASS
# class Car:
#     def __init__(self,type):
#         self.type = type
#
#     @staticmethod                   # static method so means that will not created for each obj separately, but it its comman for all obj so, far class and we create it static b\c it doesn't deal with properties etc of obj
#     def start_car():
#         print("Car is starting...")
#
#     @staticmethod
#     def stop_car():
#         print("Car is stopping...")
# class ToyotaCar(Car):
#     def __init__(self,brand,model,type):
#         self.brand = brand
#         self.model = model
#         super().__init__(type)      # syntax: supper().methd_name(perameter_if)       # if an perameter then also add it to the initialization of the child func, so we can pass argument it while creating obj
#         super().start_car()         # also working
# # newcar=ToyotaCar("Toyota",2025)
# # print(newcar.type)      # as we didn't pass ANY TYPE TO 1ST CLASS
# # #     # AttributeError: 'ToyotaCar' object has no attribute 'type'
# #
# # newcar=ToyotaCar("Toyota",2025, "AUTO")         # IF I ALSO PASS THE TYPE TO MY OBJ OF OTHER INHERITED CLASS(CLASS CAR {HERE})
# #     # TypeError: ToyotaCar.__init__() takes 3 positional arguments but 4 were given
# #BUT
#     # if i add supper to our child class it will pointing to parent class METHOD
# nawcar=ToyotaCar("Toyota",2025, "AUTo")
# print(nawcar.type) # working
#
#
# ## CLASS METHODS:
#         # generally we create a method static when we don't use instance or class attr in the method
#     # but:
#         # NOTE:
#             # STATIC METHODS CAN'T ACCESS OR MODIFY CLASS STATE & GENERALLY FOR UTILITY.        (that's why we use class method)
#     # "A CLASS METHOD IS BOUND TO THE CLASS AND RECIEVES THE CLASS AS AN IMPLICIT FIRST ARGUMENT."
#         # SYNTAX:
#             # class cls_name:
#             # @ classmethod                 # decorater
#             # def methd_name(cls):          # class(cls) as an implicit 1st argument
#                 # pass
# class Person:
#     name="ANONYMOUS"
#     def changeName(self,newName):       # assumption to change the default name to newname
#         self.name=newName
#
# p1=Person()
# print(p1.name)  # ANONYMOUS
# p1.changeName("Maryam")
# print(p1.name)  # Maryam
# # BUT
# print(Person.name)  # ANONYMOUS
# # but we have to change the class attr not the obj one
# # a normal method like the changeName doesn't change the original attr of class it creates a new var storing value of name ie, self.name=newName
# # so here the class and object name is now two separate things
#
# ## ways to change my class attr:
# # 1st way
# class Person:
#     name="ANONYMOUS"
#     def changeName(self,newName):       # assumption to change the class attr
#         Person.name=newName         # one way           # doesn't create new var it just update the original
#
# p1=Person()
# p1.changeName("maryam")
# print(p1.name)  # maryam
# print(Person.name)  # maryam
#
# # 2nd way
# class Person:
#     name="ANONYMOUS"
#     def changeName(self,newName):
#         self.__class__.name=newName         # another way       # basically it means, var(name) of class(__class__==Person) of the obj(self==p1) = ....update...
#
# p1=Person()
# p1.changeName("maryam")
# print(p1.name)
# print(Person.name) # working
#
# # BUT IF WE WANNA DIRECT ACCESS TO OUR CLASS INSIDE FUNCTION
# # we can do that via class  methods
#     # instance methods have the implicit 1st argument == self
#         # WHERE WE HAVE ONLY BUSINESS WITH INSTANCE ATTR \ METHODS, THERE WE WILL USE INSTANCE METHODS
#     # class methods have the implicit 1st argument == cls  (class is a keyword, so we write cls)
#         # WHERE WE HAVE ONLY BUSINESS WITH CLASS PROPERTIE\methods(not sure if exist) THERE WE WILL USE CLASS METHODS
#     # static methods can't access to any attr of cls or obj, so it doesn't take any implicit arg(LOGIC_FOR_ALL.PY)
#         # SO WHEN WE HAVEN'T ANY BUSINESS WITH ANY CLS OR OBJ ATTR \ METHDS, THERE WE WILL USE STATIC METHDS
#
# class Person:
#     name="ANONYMOUS"
#
#     @classmethod        # this decorater take the func as an input and return its bettr version that can chnge in cls attr
#     def changeName(cls, name):      # cls refering to the class and one is arg
#         cls.name = name
#
# p1=Person()
# p1.changeName("Marayam")        # FUNCTION NAME SHOULD BE all LOWErCASE(HERE IS A WARNING{WEAK})
# print(p1.name)
# print(Person.name)      # working
#
#
# ## PROPERTY --> DECORATER
#     # WE USE THE @PROPERTY DECORATER ON ANY METHOD IN THE CLASS TO USE THE METHOD AS APROPERTY.
# class Student:
#     def __init__(self,math,phy,che):
#         self.math = math
#         self.phy = phy
#         self.che = che
#
#     # now wanna there should be a percentage attr, so we can
#         self.percentage=str(((self.math+self.phy+self.che)/3))+"%"      # concatinating str+str
# std1=Student(98,97,96)
# print(std1.percentage)
#
# ## let a teacher recheck the papers and know that 98 of mak=th is actually 89, so she can change        # 300/100 = 3
# std1.math=89
# print(std1.math)    # 89 # so it is changed
# print(std1.percentage)  # 97%   # doesn't changed b/c sitted acc to original values
# # but
# # %age remains the same, which should be changed
#
# #`in cases like this when we can't give a fixed value to an attr, then its value will depends uppon another attr or calculation
#
# class Student:
#     def __init__(self,math,phy,che):
#         self.math = math
#         self.phy = phy
#         self.che = che
#
#         # so we can make a method that will calculate percentage
#     def calc_percentage(self):
#         self.percentage = str(((self.math + self.phy + self.che) / 3)) + "%"
#
#
# std1=Student(98,97,96)
# std1.calc_percentage()
# print(std1.percentage)# 97%
# std1.math=89
# print(std1.math)
# std1.calc_percentage()  # call again, after updation
# print(std1.percentage)  #94.0%
#
# # it works but its a lettle junky. we have simpler and easy way
# class Student:
#     def __init__(self,math,phy,che):
#         self.math = math
#         self.phy = phy
#         self.che = che
#
#     @property
#     def percent(self):
#         return str(((self.math + self.phy + self.che) / 3)) + "%"
#
#
# std1=Student(98,97,96)
# print(std1.percent)
#
# std1.math=89
# print(std1.percent) # 94.0% # working2
#
# ## OTHER DECORATORS:(SHOULD EXPLORE)
#     # @GETTER
#     # @SETTER
 #
##  4) POLYMORPHISM:        (I.E, OPERATER OVERLOADING IN PYTHON)
#     # POLY-->MANY & MOPHO---> SHAPE\FORM
#     # WHEN THE SAME OPERATOR IS ALLOWED TO HAVE DIFFERNT MEANING ACCORDING TO THE CONTEXT.
#     # I.E, PLUS OPERATER
# print(3+7)      # addition  #10
# print("Jamal "+"Nasar")     # concatination     # Jamal Nasar
# print([2,1,3,7]+[4,5,6,7,8])    # merging   #[2, 1, 3, 7, 4, 5, 6, 7, 8]
# # it is happenning b\c in each class i.e, list, str etc it is pre defined that what will the plus(+) operater do
# print(type(3))  # <class 'int'> # bassicly in python we have built-in class called int and 3 is an obj of this class similarly 7 is another obj of this class, now if i write plus b\w them the int class performs addition(which already defined func of plus in int) on its obj
#
# # IN THIS WAY IN EVERY CLASS THE MEANING OF DIFFERENT OPERATERS IS DEFINED ALREADY FOR DIFFENT DATA TYPES(CLASS)
#
# # similarly when we create our own class we can also do operater overloading for our self
#
# # all of the above is implicit overloading(python did it already)
# # we can do the similar ope overloading for our classes EG: COMPLEX NO.
# # REAL NUMBERS--> NORMAL NO. LIKE 2,-4,12.6 ETC
#     # ADDITIOB OF R: 3+4==9
# # COMPLEX NUMBER---> REAL+IMAGENARY PART(WE IMAGINED) ==> 2i+3j
#     # ADDITION OF COMPLEX NO.: REAL + REAL & IMG +IMG PART (2i+3j)+(5i+7j)==7i+10j
#         # WE USE COMPLEX NUMBER IN VOICE RECOGNITION(in ML)
# # THERE IS NO BUIL-IN COMPLEX CLASS SO WE WILL CREATE BY OWN:
# # class Complex:
# #     def __init__(self, realpart, imagpart):     # every complex no. will have two parts real and imagenary
# #         self.realpart = realpart
# #         self.imagpart = imagpart
# #
# #     def shownum(self):
# #         print(self.realpart,"i +",self.imagpart,"j")
# #
# # comp1=Complex(2,3)
# # comp1.shownum()     # 2 i + 3 j
# #
# # comp2=Complex(4,5)
# # comp2.shownum()     # 4 i + 5 j
#
# # we wanna add them
# # when we do operation overloading(like defing meaning of plus in Complex), we use dunder functions

# ## DUNDER FUNCTION:
#     # WHEN WE WRITE DOUBLE UNDERSCORE IN FRONT OF FUNCTION NAME, WE CALL THEM DUNDER FUNCTION
#     # MANY DUNDER FUNCTION ALREADY EXIST IN PYTHON
#     # eg:
# # for Complex i create  func for addition
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.realpart = realpart
#         self.imagpart = imagpart
#
#     def shownum(self):
#         print(self.realpart,"i +",self.imagpart,"j")
#
#     def add(self,num):
#         self.realpart =self.realpart + num.realpart
#         self.imagpart =self.imagpart + num.imagpart
#         # creating new complex num inside class
#         return Complex(self.realpart,self.imagpart)
#
# comp1 = Complex(2, 3)
# comp1.shownum() # # 2 i + 3 j
#
# comp2=Complex(4,5)
# comp2.shownum()     # 4 i + 5 j
#
# comp3=comp1.add(comp2)   # add comp2 to comp1
# comp3.shownum() # 6 i + 8 j
#
# # BUT I DON'T WANNA USE THE FUNC, AND SIMPLY ERITE COMP1+COMP2
# # so i can make my add func dunder
#
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.realpart = realpart
#         self.imagpart = imagpart
#
#     def shownum(self):
#         print(self.realpart,"i +",self.imagpart,"j")
#
#     def __add__(self,num):
#         self.realpart =self.realpart + num.realpart
#         self.imagpart =self.imagpart + num.imagpart
#         # creating new complex num inside class
#         return Complex(self.realpart,self.imagpart)
#
# comp1 = Complex(2, 3)
# comp1.shownum() # # 2 i + 3 j
#
# comp2=Complex(4,5)
# comp2.shownum()     # 4 i + 5 j
#
# comp3=comp1 + comp2  # add comp2 and comp1
# comp3.shownum() # 6 i + 8 j
#
# # worrking
#
# # similarly i can do for subtraction
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.realpart = realpart
#         self.imagpart = imagpart
#
#     def shownum(self):
#         print(self.realpart,"i -",self.imagpart,"j")
#
#     def __sub__(self,num):
#         self.realpart =self.realpart - num.realpart
#         self.imagpart =self.imagpart - num.imagpart
#         # creating new complex num inside class
#         return Complex(self.realpart,self.imagpart)
#
# comp1 = Complex(2, 3)
# comp1.shownum() # # 2 i + 3 j
#
# comp2=Complex(4,5)
# comp2.shownum()     # 4 i + 5 j
#
# # comp3=comp1.sub(comp2)    # sub 2 from 1
# # comp3.shownum() # -2 i - -2 j
# # # but using dunder
# comp3=comp1 - comp2
# comp3.shownum()   # -2 i - -2 j
#
# ## MORE ABOUT DUNDER FUNC:  PYTHON DOCUMENTATION, SECTION: 3.3.8
#
#
#
#
#
#
#
#
#
# ## OPERATORS AND DUNDER FUNCTIONS:
#     # a+b   # addition  a__add__
#     # a-b   # subtraction   a__sub__
#     # a*b   # multiplication    a__mul____
#     # a/b   # division  a__truediv____
#     # a%b   # modulius  a__mod____
#
# # basiclly when we write a+b or a*b etc. (a,b can be any type\class), internally in that class we call a DUNDER function for the objects



## PRACTICE
# 1) Define a Circle class to create a circle with radius r using the constructor.
#   # define an area() method of the class which calculates the area opf the circle
    # define a perameter() method of the class which allow you to calculate the perameter of the circle.

# 2) Define a Employee class with attr role, daoertment, & salary. this class also has a showdetail() method.
#   # create an engineer class that inherites prioperties from Employee & has additional attr name and ag.

# 3) Create a class called Order which store item anf their price. Use Dunder function __gt__() to covey that:
            # order1>oredr2if price of order1>price of order2


