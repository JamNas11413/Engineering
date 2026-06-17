# Linked Lists
    # Remember how the push method on our Queue is O(n) instead of O(1)?

    # most common after arrays
    # it solves many problem with arrays and are also used in building more complex data steuctures

# linked list:  
    # we use linked liast to store a list of objects in sequence but unlike arrays linked list can grow 
    # and shrink automaticaly

    # a linked list consist of a group of nodes in sequence  
    # each node holds two pieces pf data one is a value and the other is the address of the next node in the list
        # so we say each node refrence to / point to the next node  and that is why we refered to this sequence a 
        # linked list because thses nodesare linked together
    # we call the 1st node the "head" and the last node the "tail"

# COMPLEXITIES:
    # look up:
        # by value: O(n) # the value may be at end
        # by index: unlike arrays/ list where items are stored sequentialy, the nodes of a linked list can be all over the place in memory they may nort be next t each other 
            # that why each node nedda keep reprence to the next 
            # so we can't look at it by index we have trverse the list until we find it 
                # so in worst case the value can be at end so O(n)

    # insertion:
        # at the end: we simply have to carete a new node and make the last node(tail) refrence to it(we should ahve a refrence to the las node some where so we don't needa traverse the list every time ) and make
               # so it an O(1) 
        # at the beggining: O(1) as we should have a refrence to the head/1st node, so insert a new item at the beggining we vreatea new node, ink it to the 1st node and then change the head to point to this new node {unlike arrays we don't have to shift items up 1 index}
        # in the middle: lets sayafter 10th node, so we have to find the node and then insert the new node 
            # O(n)

    # Deletion:
        # from the beggining: we simplty set the head to point to the 2nd node and also remove the the refrence fron the 1st item to the 2nd, so it doesnot refrence the 2nd node anymore (because if we don't do that language garbage collecter will think that this obj is still in use and won't removed , so we should unlink)
        # from the end: we we can easily get the tail but we should know the previous node, so we can hjave the tail point to that node, so we have totraverse the list all the way to the tail as soon as we get to the node before the last node we keep a refrence to tit as prevous node, then we will unlinked this node from the last node and finnally we hav to make tail point to the prevous node 
            # O(n)
        # from the middle: we have to traverse the list and find the node and also its prevous node,
                #  then we should link the previous node to the node after this node and then the remove the extra link 
                #  O(n)


from networkx import nodes
from objgraph import at


def push(self, item: str) -> None:
    # everything in self.items has to shift
    # up a position, which takes O(n) time
    self.items.insert(0, item)

# Let's fix that.
    # To build a faster queue, we'll use a Linked List instead of a regular List (array) 
        # under the hood. A linked list is where elements are not stored next to each 
        # other in memory, instead, each item references the next in a chain.To build a 
        # faster queue, we'll use a Linked List instead of a regular List (array) under 
        # the hood. A linked list is where elements are not stored next to each other in memory, 
        # instead, each item references the next in a chain.



        # DataStructures/DataStructures/picNotes/linkedlists.png



# Nodes
#     Our nodes will be represented by a simple class with two fields:
    #     val - The raw string value that the node holds (e.g. 'Carla', 'James', etc)
    #     next - A reference to the next node in the list



from typing import Any


class Node:
    def __init__(self, val: Any) -> None:  # node constructer    # will be calle dfor every obj(node) so each node will have these two fields
        self.val: Any = val
        self.next: "Node" | None = None

    def set_next(self, node: "Node") -> None:
        self.next = node


    def __repr__(self) -> str:
        return self.val
    

node1 = Node("Carla")
node2 = Node("James")
node1.set_next(node2)
print(node1)

cars = ["BMW", "Mercedes", "Audi", "Lexus"]


# Linked List vs. List   {video 34++ in mosh DSA playist===remaining}
    # A linked list is a collection of ordered items, so it's similar to a "normal" list (also called an "array" or "slice" in other languages).

        # DataStructures/DataStructures/picNotes/linkedlistVSlist.png

    # Items in a "normal" list are stored next to each other in memory, and to get an item from a normal List we have to use a numbered index:


car = cars[3] # 4th item in the list, which is "Lexus"

    # You can think of the "index" as simply an offset from the start. The cars list in this example refers to the start of the list, and 3 is just 
    #   the 4th item in that section of memory. With a normal list, all the data is stored in the same place in memory and the index is just a 
    #   way to find the right spot.
    # In a linked list, there are no indexes! Each node contains two things: the data itself, and a reference 
        # to the next node in the list. Iterating over a linked list requires starting at the head node and following 
        # the next references until you reach the end.
head_car_node = Node("BMW")
current_car_node = head_car_node
while current_car_node is not None:
    print(current_car_node.val)
    current_car_node = current_car_node.next

# Frankly, linked lists can be annoying to use and incur more overhead, so why use a linked list at all? 
#     It's because sometimes linked lists are much faster to make updates to, particularly when inserting or 
#     deleting items from the middle.

# In a normal list, if you insert an item in the middle, you have to shift all the items after it down one spot, 
# which takes O(n) time:

cars.insert(2, "Tesla") # insert "Tesla" at index 2, which is the 3rd item in the list

            # DataStructures/DataStructures/picNotes/insurtion.png
# In a linked list, once you've traversed to a given node, insertion is (O(1)) because you can simply update two references:


        # DataStructures/DataStructures/picNotes/insertion_linkedlist.png

# You can find an item in a linked list by... Iterating through all the nodes by following the 'next' references
# Linked lists have a faster time complexity than regular lists when it comes to... Inserting/deleting items in the middle of the list



# Iterating
#     Even though iterating with linked lists kinda sucks compared to the simplicity of arrays (normal lists), 
#         we've got to do it. Although the implementation is more complex and slow, we can still make it easy 
#         for users of our class by providing an __iter__ method.

#     The yield Keyword
#         The yield keyword in Python returns a value, kind of like return. 
#         However, it's used to turn the function into a generator function.

#         A generator function creates a new function object. When that function 
#             is called, it executes the code in the generator function until it hits a 
#             yield statement. At that point, the function pauses and returns the value of 
#             the yield statement. The next time the function is called, it picks up right where it left off.

def create_message_generator():
    yield "hi"
    yield "there"
    yield "friend"

gen = create_message_generator()
first = next(gen)
print(first)  # prints: hi
second = next(gen)
print(second)  # prints: there
third = next(gen)
print(third)  # prints: friend

# Every time you call create_message_generator(), it creates a new generator instance. To continue from where you left off, you need to assign this generator to a variable (like gen in the example above). This way, when you use next() or loop over the generator, you're continuing with the same instance rather than starting a new one.





# class LinkedList(Node):
#     def __init__(self) -> None:
#         self.head: Node | None = None

#         def __iter__(self):
#             node = self.head
#             while node is not None:
#                 yield node
#                 node = node.next

#         def __repr__(self) -> str:
#             nodes = []
#             for node in self:
#                 nodes.append(node.val)
#             return " -> ".join(nodes)

# By overriding the __iter__ method, Python will allow us to use a for loop to iterate over the linked list:





# Add to Tail
    # Time to allow our LinkedList to add new nodes to the end of the list. Kind of like a regular Python List's 
    #   .append method.

        # DataStructures/DataStructures/linkedlists.png

    
# class LinkedList(Node):
#     def __init__(self) -> None:
#         self.head: Node | None = None

#     def add_to_tail(self, val: Any) -> None:
#         new_node = Node(val)
#         if self.head is None:
#             self.head = new_node
#             return
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#         current_node.next = new_node

#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next

#     def __repr__(self) -> str:
#         nodes = []
#         for node in self:
#             nodes.append(node.val)
#         return " -> ".join(nodes)
    


# Add to Head
#     For added flexibility, let's allow users to add items to the front of our linked list as well.

class LinkedList(Node):
    def __init__(self) -> None:
        self.head: Node | None = None

    def add_to_tail(self, val: Any) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
    
    def add_to_head(self, val: Any) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
    

# Linked List Queue
#     To use our Linked List as a fast queue (O(1) pushes and pops) we need our add_to_tail function to be O(1). 
#         Currently, it iterates over the entire list before appending an item. 
#         We can fix this by keeping track of the last item with a new data member: tail.

# Note: It's common in algorithms to make this kind of trade-off. By using a little extra memory (keeping track of tail), we can make our operations faster. 
#   Sometimes you might need to go the other way, and use more computation time to save memory.

class LLQueue(Node):
    def remove_from_head(self) -> Node | None:
        if self.head is None:
            return None
        removed_node = self.head
        self.head = self.head.next
        removed_node.next = None
        return removed_node

    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self) -> None:
        self.tail: Node | None = None
        self.head: Node | None = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)
    



# Remove from Head
#     We're one method away from having a fully functioning O(1) Queue! We just need a way to remove the first element from the linked list in constant time. When we're finished, our LinkedList will fulfill the basic requirements of a Queue:

#         add_to_tail: Constant time insert
#         remove_from_head: Constant time pop

# Let's rename the LinkedList class to LLQueue and remove the add_to_head functionality because Queues don't allow inserting into the wrong end.

# We've also flipped the arrows in the printed representation to reflect the change.






# Let's recap a few key points about linked lists and queues:

#     The problem with our array (normal Python list) implementation of a queue was that it had O(n) push operations.
#     The linked list implementation of a queue has O(1) push operations.
#     Linked lists are usually a worse choice than standard arrays because:
#         They are less performant due to more memory overhead
#         They are more complex to work with, debug, and reason about
#         They have no random access (indexing to a specific element)
#     Doubly linked lists are a better choice than arrays in very specific circumstances because they have O(1) insertions and deletions at both ends of the list.


# A Queue made with a linked list instead of an array... ...can have O(1) pushes and pops
# A Queue that uses an array doesn't have O(1) pushes and pops because...When elements are added or removed from the first index of the array all the items need to shift, which takes O(n) time