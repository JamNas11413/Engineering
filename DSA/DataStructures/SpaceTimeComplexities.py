# BigO notation:
#     Big O notation is a mathematical notation that describes the limiting behavior of a function when the 
#     arguments tends towards a particuler value or infinity.

#     OR 

#     we use big O to describe the performance of an algorithm 
#         and this helps us determine if a given algorithm is scalable or not 

#             bascally means is this algorithm  going to do well as the input grows really large

#     O(n) -> big O notation

#     but why we need it:
#         certain operations can be more or less costly depending on what datastructure we use






# O(1)
#     i.e:
#         def print_first(arr):
#         print(arr[0])
        
#         array = [1, 2, 3, 4, 5]
#         print_first(array)

#             this func take an array of integers and print the 1st item, it does not matter how 
#             big the array is, all we  have to access the vary 1st element, so here is a single 
#             operation and it will take a constt amount of time to run independantly of input size

#             SO, this function runs in constt time and represented by O(1) (big o of one)  this is the runtime complexity of this method


#         BUT:
#             what what if we perform the operation twice i.e,
#                 def print_first(arr):
#                     print(arr[0])
#                     print(arr[0])
                    
#                 array = [1, 2, 3, 4, 5]
#                 print_first(array)

#                     i am getting the 1st element twice
#                         two operation both are running constt time 
#                         so, its time complexity is O(2)

#         HOWEVER, when we taking about the runtime complexity we don't really cares about the no. of operations, we just wanna know how 
#         much the algorithm slow down as the input grows larger

#         so we can simplify it to as O(1)   
#             O(2) simplifies to O(1) means same as they are taking constant time 



# # O(1):
# def print_first(arr):
#     print(arr[0])

# array = [1, 2, 3, 4, 5]
# print_first(array)

# # O(1) - constant time complexity, as we are accessing a specific index in the array regardless of its size.

# def print_first(arr):
#     print(arr[0])
#     print(arr[0])

# array = [1, 2, 3, 4, 5]
# print_first(array)

# # O(2) - still constant time complexity, as we are performing a fixed number of operations (2 print statements) regardless of the size of the array. However, we typically drop constants in Big O notation, so this would still be considered O(1).









# O(n)
#     i.e,
#         for i in array:
#         print(i)

#         here the input matters if we have a single item we gonna have a single print 
#         operation and if we have a million item we gonna have a million print opertions 

#         SO, the cost of this algoritms grows linearly as input grows 
#             neaning have a direct relation with the input size 

#         SO, the runtime complexity of this method can be represented by O(n) (big o oh n), where n represents the size of the input 
#             so as n grows the runtime also grows linearly 

#     BUT, what if we add two operation OR two loops
#         linearStructure.py

# # O(n):
# for i in array:
#     print(i)
# # O(n) - linear time complexity, as we need to iterate through each element in the array once. The time taken grows linearly with the size of the array.


# # time complexity of this method
# def method(arr):
#     print(i) # O(1) - constant time complexity, as it is a single print statement that does not depend on the size of the array.
#     for i in array: # O(n) - linear time complexity, as we need to iterate through each element in the array once. The time taken grows linearly with the size of the array.
#         print(i)
#     print(i) # O(1) - constant time complexity, as it is a single print statement that does not depend on the size of the array.
# method(array)

# # so, the overall runtime complexity of the method is:
# #    O(1) + O(n) + O(1) 
# #  = O(2) + O(n) or O(2 + n)
#         # as O(2) is a constant, we can drop it in Big O notation, so we are left with: 
# #  = O(1) + O(n) 
#         # while using the big(o) notation, we drop constants as it doesnot really matter i.e if we have 1M item in our array tow extra print statements will not make a difference in the overall runtime complexity, 
#         # so we can drop the constant time complexity and focus on the dominant term, which is O(n).
# #  = O(n)

# # two loops
# def two_loops(arr):
#     for i in arr: # O(n) - linear time complexity, as we need to iterate through each element in the array once. The time taken grows linearly with the size of the array.
#         print(i)
#     for j in arr: # O(n) - linear time complexity, as we need to iterate through each element in the array once. The time taken grows linearly with the size of the array.
#         print(j)

#         # SO, the overall runtime complexity of the method is:
#         #    O(n) + O(n)
#         #  = O(2n) or O(n + n)
#                 # as O(2n) is a linear time complexity, we can drop the constant in Big O notation, so we are left with: 
#         #  = O(n) + O(n) 
#                 # while using the big(o) notation, we drop constants as it doesnot really matter i.e if we have 1M item in our array two loops will not make a difference in the overall runtime complexity, 
#                 # so we can drop the constant time complexity and focus on the dominant term, which is O(n).
#         #  = O(n)

#         # meaning:
#             # all we cares is time complexity, 
#                 # and O(n) and O(2n) are both linear time complexity, so we can say that the overall runtime complexity of the method is O(n) regardless of the number of loops we have, as long as they are linear.

# two_loops(array)   

# # two loops and two arguments

# def two_loops_args(arr1, arr2):
#     for i in arr1: # O(n) {we can use n for th size fo 1st input}- linear time complexity, as we need to iterate through each element in the first array once. The time taken grows linearly with the size of the first array.
#         print(i)
#     for j in arr2: # O(m) {we can use m for the size of the second input} - linear time complexity, as we need to iterate through each element in the second array once. The time taken grows linearly with the size of the second array.
#         print(j)

#     # so the runtime complexity of the method is:
#     #    O(n) + O(m)
#     #  = O(n + m)
#     #  = O(n) 
#         # as the runtime complexity of both loops is linear, we can say that the overall runtime complexity of the method is O(n) regardless of the number of loops we have, as long as they are linear.









# O(n^2)

# printing all combination of elements in an aray 
from uvloop import Loop


array = [1,2,3,4,5,6,7,8,9,0]
def all_combo(arr):
    for i in arr: # O(n)
        for j in arr: # O(n)
            print(i , ':', j, end='  ,  ')

# all_combo(array)

# runtime complexity:
    # O(n) * O(n)  {as nested loops not separate, in separate we use plus}
    # O(n * n)
    # O(n^2)

        # we say this algorithm runs in quadratic time 


# ALGORITHMS THAT RUNS IB O(n^2) OR QUADRATIC TIME GETS REALY SLOWER REALLY QUICK

# ADDING ANOTHER LOOP 
def all_combo_loop(arr):
    for x in arr: # O(n)
        print(x)

    for i in arr: # O(n)
        for j in arr: # O(n)
            print(i , ':', j, end='  ,  ')

# all_combo(array) 
    # time complexity:
        # O(n) + O(n)* O(n)
        # = O(n + n * n)
        # = O(n + n^2)
            # as square of a number is alwyays greater than the number itself, so n^2 > n
            # we use the big O notation to approximate the cost of algorithm as input increases 
            # as we need an approximation not exact value so we can drop the n, i.e,
        # = O(n^2) # we concluded thatthis method rins in O(n^2) time 


# triple nested Loop 
def triple_nested_Loop(arr):
    for i in arr: # O(n)
        for j in arr: # O(n)
            for x in arr: # O(n)
                print(i , ':', j, ':', x,end='  ,  ')

# triple_nested_Loop(array)

# time complexity of triple_nested_loop method: 
    # O(n * n * n)   # as thgey are nested so multiply
    # = O(n^3) => time complexity os o of n cubed


        # O(n^3) GET MORE SLOWER THAN O(n^2) AND SO ON





# O(log n):
    # another growth rate is logarithmic growth
    # a linear algoritm grows as input grows while logarithmic curve slows down at some point 
        # so an alogorithm that runs in logarithmic time is more scalable than linear or quadratic time

    # i.e
        # we have a array of ten sorted integers from 1 to10
        # and we have to find the number 10  {find number ten means search for 10}
            # for searching we have searching algorithms i.e linear serach and binary search

                # one ways is to loop over each item and check if it is ten 
                    # this uproach is knowm as linear serach as it takes linear time (more items we have more time it gonna take)
                    # at worst case scenario if the 10 is at end of the array we have to loop ten times (maximum times)

                # 2nd way is binary search
                    # binary search algorithm runs at logarithmic time, so much faster than the linear search
                    # working
                        # as the array is sorted its 1st step will be to look at middle number (5) and check wheter this number is equl to 10, greater than 10 or less than 10
                        # if it is equal we found the number
                        # if it is less than targeted value 
                            # our targeted value must be in right partition of this array, so we ignore all on left and goes towards right 
                                # so we narrowed down our search by half
                            # again we will look at the middle number of the right partition (8) and check for the conditions
                            #if it is smaller so look at right of this number 

                            # so in each stepp we re narrowing down our serach by half


                        # so if we have 1M items in an array we can find the targeted item with maximum of 19 comparisons

                # so this is logarithmic time uin action 


        # it is proved that an algorithm with logarithmic time is more scallable than one with linear time 


    


# O(2^n)
    # another growth rate is exponential growth which is the complete opposite of logarithmic growth

    # the logarithmic curve slows down as the input grows while exponential curve grows faster and faster

    # obiviously an algorithm that runs in exponnetial timeis not scalable at all, as it will become very slow very soon 






# IN AN IDEAL WORLD WE WANT OUR ALGORITHM TO BE SUPER FAST AND SCALABLE AND TAKE MINIMUM AMOUNT OF MEMORY
    # but as the worls isn't an ideal sys(will in physics it just means where no loss of energy occurs, hhhhhh)
        # most of the time we have to do a trade off between time and space 
            # there are time where we have more space so we can use that to uptomize an algorithm and make it faster and more scalable 
            # but there are also time when we have limited spoce (like when we build an app for small mobile device ), in this situation 
                # we have to optimize for this space because scalability is not a big factor (only some user gonna use it concurrently)

            # so we need a way to talk about how much space an algorithm requires, AND THATS WHERE WE USE SPACE COMPLEXITY 





# Space Complexity:
    # O(x) -> big o notation for space 
# i.e, 
def greet(arr):
    for name in arr:
        print("hi!", name)

array = ["jamal","Ms maryam", "ijaz", "sana"]
greet(array)


# the loop is independant of the sise of the input array, this method will only allowcate some additonal memory fot the loop variable i.e name

# so it takes O(1) space as it tkes constt space of the one var

# but what if we declare a string array inside the method and copy the outer array to it i.e, 
def greet(arr):
    arryC = arr
    for name in arr:
        print("hi!", name)

# now th local variable to the functtion arryC is dependant on size of the array and it will grow as the size of the array grows    
    # here we will have:
        # sapce complexity:
            # O(n) -> the more item we have in the input array the more space the method gonna take 
            # and this is in direct proportion to the size of our input array that why we have O(n) here


    # AND BY THE WAT WHEN WE TALK ABOUT SPACE COMPLEXITY WE ONLY LOOK AT THE ADDITIONAL SPACE THAT WE SHOULD ALLOWCATE RELATIVE TO THE SIZE OF THE INPUT 
        # WE ALWAYS HAVE INPUT OF SIZE N SO WE DON'T COUNT IT WE ANALYZE IT, that how much extra space we need to allocate for this algorithm


        # so we should look at the sapce complexity of our algorithm and see if there are ways to preserve memory


    # space complexity of an algorithm/method depends on how much variables it have 
            # as time => speed = no. of ops/t
            # and space => storage = amount of memory neede tpo store the variables

                # so if a func have one var design for single value 
                    # space complexity of such funcs will be O(1) -> constant 
                # and if a func have a list etc declared and it dpends on the size of outer list(can have multiple values)
                    # then the space complexity of such methods will be O(n) - relative linear
