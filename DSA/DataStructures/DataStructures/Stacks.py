# Stacks
    # A stack is a data structure that stores ordered items. It's like a list, but its design is more restrictive. 
    # It only allows items to be added or removed from the top of the stack:
        # It's called a "stack" because it behaves just like a stack of physical items. 
        # Imagine a stack of plates: it's easy to take an item off the top of the stack, 
        # but you can't really get to the items in the middle or at the bottom without removing 
        # the items on top first. You'll often hear a stack referred to as a LIFO (last in, first out) data structure.

            # to access the last item we have to take off all the above
        
        # common use cases:
            # undo/redo 
            # browser arrows 
            # etc

    # COMPLEXITY:
        # pushing and poping item :
            # are both O(1)

from typing import Any

class Stack:
    def __init__(self) -> None:
        # Initialize an empty list to store stack elements
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        # Correctly append the item to the end of the list
        self.items.append(item)

    def pop(self) -> Any:
        # Traditional stacks also need a way to remove the top item
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        # Use the built-in len() function on the underlying list
        return len(self.items)
    
    # Pop and Peek
    #     Now that we can add items to our stack, we need to be able to view the top item, and remove the top item.

    def peek(self) -> Any:
        if len(self.items) == 0:
            return None
        return self.items[0] # The top of the stack is the first item in the list (index 0)

    def pop(self) -> Any:
        if not self.is_empty():
            return self.items.pop(0) # Remove and return the first item in the list (index 0)
        raise IndexError("pop from empty stack")

    def __str__(self) -> str:
        # Optional: Makes print(obj) look nice and readable  , without this the print will return = <__main__.Stack object at 0x7fd81e70dfd0>
        return f"Stack: {self.items}"


obj = Stack()
obj.push('t')
obj.push('a')
obj.push('b')

print(obj)          # Output: Stack: ['t', 'a', 'b']
print(obj.size())   # Output: 3



# Stack Speed:
#     You might be wondering, "why would I use a stack instead of a list?" or "Isn't this just a list with fewer features?"

#     And you'd be right! A stack is a list with fewer features, but that's the point. By restricting the ways we can interact with the data, 
#     we guarantee that certain operations are blazingly fast. Here are all the operations a typical stack supports, 
#     along with their Big O time complexity:
    #     Operation 	Big O 	Description
    #     push 	O(1) 	Add an item to the top of the stack
    #     pop 	O(1) 	Remove and return the top item from the stack
    #     peek 	O(1) 	Return the top item from the stack without modifying the stack
    #     size 	O(1) 	Return the number of items in the stack

#     It's all O(1)! That means no matter how many items are in the stack, these operations will always take the same amount of time. Stacks are really fast and are usually the best choice when the behavior of a stack is all you need.


    # Where can items be added to and removed from a stack? = top





# Stack Review
#     All supported operations are O(1) by themselves. However, some tasks, like getting to an item at the bottom of the stack have a higher time complexity because they require multiple pop operations.
#     Stack operations are limited: no searching, no sorting, no random access
#     Stacks, like all abstract data types, can store items of any type. What makes it a stack is the behavior of the operations, not the type of data it stores.
#     Stacks are often used in the real world for:
#         Function call management
#         Undo/redo functionality
#         Expression evaluation
#         Browser history

# What can be stored in a stack? = Any type of data can be stored in a stack, as long as it follows the LIFO 
#   (last in, first out) principle. 
#   This means that the last item added to the stack will be the first one to be removed. 
#   Stacks can store any type of data, including numbers, strings, objects, and even other stacks.

# If you want to get to an item at the bottom of a stack, what is the Big-O to retrieve that item? = O(n) 
#   because you would have to pop all the items above it to get to it, which takes linear time relative to 
#   the number of items in the stack.




# we use parenthesis for grouping data. hhhhhh
