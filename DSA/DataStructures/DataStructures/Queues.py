# What Is a Queue?
    # A queue stores ordered items... again, kind of like a list, but again, like a stack, its design is more restrictive. 
    # A queue only allows items to be added to the tail of the queue and removed from the head of the queue.
        # It's called a "queue" because it behaves just like a line of people waiting for something. 
        # The first person in line is the first one to get served, and new people always join the end of the line. 
        # You'll often hear a queue referred to as a FIFO (first in, first out) data structure.

            # to access the last item we have to take off all the above

        # common use cases:
            # printer queue
            # etc

        # In the Lord's tongue (American English) we say "I'm waiting in line", but in the UK they say "I'm waiting in a queue". Alan Turing was British, so, we just gotta let them have this one

    #  DataStructures/DataStructures/picNotes/queue.png


# Queues are use more often as they perfectly model so many systems
    # wherever objects are processed in order of which they are recieved

# Three min ops:
    # enqueue(item) - add an item to the end of the queue
    # dequeue() - remove and return the item at the front of the queue
    # peek() - return the item at the front of the queue without removing it

    # only these three ops and no iteration or indexing

    # complexity:
        # enqueue and dequeue are both O(1) operations, as they only involve adding or removing an item from the front or back of the queue, 
        #   regardless of its size. 

        # peek is also O(1) since it only involves accessing the front item without modifying the queue.    

        # all ops = O(1) = means stay fast regardles of the size of the queue

from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        return self.items.pop(0)

    def peek(self) -> Any:
        return self.items[0] if self.items else None
        

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return f"Queue: {self.items}"
    

# term 1 	term 2 	description
# Push 	Enqueue 	Adds an item to the tail of the queue
# Pop 	Dequeue 	Removes and returns an item from the head of the queue


# Queue Speed:
#         So how fast are queue operations? Well, in an optimized queue, they'd be:
#     Operation 	Big O 	Description
#     push 	O(1) 	Add an item to the back of the queue
#     pop 	O(1) 	Remove and return the front item from the queue
#     peek 	O(1) 	Return the front item from the queue without modifying the queue
#     size 	O(1) 	Return the number of items in the queue

#     Just like a stack, all operations are O(1)! No matter how many items are in the queue, 
#     these operations will always take the same amount of time. The reason to choose a queue over a stack is 
#     all about ordering. Queues should be used when you need to process items in the order they were added.

#     LIFO (stack) vs FIFO (queue).




# A Problem

# Our current Queue class has a problem... take a look at the push method:

# def push(self, item: str) -> None:
#     self.items.insert(0, item)

# It's not O(1)! The List's insert method has to shift all the other items in the list down to make room for the new item.


# If an item could be anywhere in a queue, what is the Big O complexity to retrieve that item?
#     O(n) - because we might have to look through the entire queue to find the item we're looking for.


# Why is our list-based queue's push operation O(n)? 
#     Because the push method uses the list's insert method, which has to shift all the other items in the list down to make room for the new item.
#     The push operation in your list-based queue is O(n) because inserting an element at the front of a standard array or Python list forces every existing element to shift over by one position in memory.


# It's okay to violate academic constraints as software engineers as long as we understand the trade-offs involved.