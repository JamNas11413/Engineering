# Lists:
#     Okay, we know what lists are, BUT from a data structures and algorithms perspective, WHAT ARE THEY GOOD FOR? Let's break it down by operation:
#         Append: Appending an element to the end of a list, e.g. cars.append("ford") 
#             is (on average) O(1). 
#             We go directly to the end and add the element.

#         Index: Accessing an element by index, e.g. cars[2] 
#             is O(1). 
#             We go directly to the index and return the element.

#         Delete: Removing an element from the middle of a list, e.g. cars.pop(2) 
#             is O(n). 
#             We have to shift all the elements after the deleted element down one index.

#         Search: Searching for an element in a list, e.g. cars.index("ford") 
#             is O(n). 
#             We have to iterate over the list until we find the element.

#     In other words, lists start to struggle in two primary areas:
#         When you need to frequently delete elements from the middle of the list
#         When you need to frequently search for specific elements in the entire List



#     Looking up an item in a list by index is much faster than searching for items using iteration. O(1) vs O(n).

#     What is the Big-O complexity of the last_work_experience() function, 
#     where n is the length of the work_experiences array?

#     def last_work_experience(work_experiences: list[str]) -> str | None:
#     if len(work_experiences) > 0:  # O(1)
#         return work_experiences[len(work_experiences) - 1] #O(1) - work_experiences[i] # O(1) - len(work_experiences) - 1     # the len() function is called twice in the func and each time it will be exe as pyhton does not store values automtically untill we don't i,e with vars etc
#     return None

#     ANS: O(1) + O(1) + O(1) 
#         = O(1) 

#     Why is index-lookup so much faster than iteration?
#         The computer can jump straight to the location of an index - an index is like an address of an item in a list
        
#         Target Address = base address + (index * pointer size)
#             Because it knows the starting address and the exact slot size, the hardware jumps directly to the target location instantly.