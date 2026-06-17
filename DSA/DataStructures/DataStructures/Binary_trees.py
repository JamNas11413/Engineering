# Trees
#     Trees are a widely used data structure that simulate a hierarchical... well... tree structure. That said, 
#     they're typically drawn upside down - the "root" node is at the top, and the "leaves" are at the bottom.

        # DataStructures/DataStructures/picNotes/tree.png


    # Trees are kind of like linked lists in the sense that the root node simply holds references(kind of like root folder in UNIX file system which holds references to its child folders and there no directory above it to hold a name / refrence to it so its name is just "/")
    #   to its child nodes, which in turn hold references to their children, but Tree's nodes can have multiple children instead of just one. A generic tree structure has the following rules:

    #     Each node has a value and may have a list of "children"
    #     Children can only have a single "parent"

    # Linked List

    #     node -> node -> node

    # Tree

    #     Drawn from left to right in this case:

    #             > node
    #         > node
    #     > node
    #     > node
    #             > node
    #         > node
    #             > node
    #         > node
    #     > node
    #         > node


# Multiple nodes in a tree can have the same value?
#     Yes, multiple nodes in a tree can absolutely have the same value. In computer science, a clear distinction exists between a node (the physical container or memory address) and its value/key (the data stored inside that container)


# Parent nodes can have multiple child(ren), and children can have one parent




# Binary Trees
#     Trees aren't particularly useful data structures unless they're ordered in some way. One of the most common types of ordered tree is a Binary Search Tree or BST. A BST has some additional constraints:

#         Instead of an unbounded list of children, each node has at most 2 children
#         The left child's value must be less than its parent's value
#         The right child's value must be greater than its parent's value
#         No two nodes in the BST can have the same value

# By ordering the tree like this, we can traverse the tree to find the node we want much faster.

# Nodes in a binary tree can have at most two child nodest 

    # it is fast because it is always presorted in a way that allows us to quickly eliminate half of the remaining nodes at each step.
        # it often store numbers but if there are stri g/names etc we just needa give them an id 
            # that is why itmuse in database to retriveban obj by its id


# Binary search trees, as opposed to generic trees, must be ordered in a specific way. Each node can have at most two children, and the left child must be less than its parent, while the right child must be greater. This ordering allows for efficient searching, insertion, and deletion operations. Additionally, no two nodes in a binary search tree can have the same value, ensuring that each value is unique within the tree.



# Insert Nodes
#     The building blocks of a BST are Nodes. 
#   In our implementation, we will only use a single class, the BSTNode class. 
#   Any BSTNode is technically also a full Binary Search Tree, with itself as the root node (it's not aware of any potential parents). 
#   Most of the methods that traverse the tree will do so recursively... have fun!


# {
#     traversal refers to the process of visiting or accessing every element in a data structure exactly once in a specific order
# }


# from typing import Any


# class BSTNode:
#     def __init__(self, val: Any = None) -> None:
#         self.left: "BSTNode | None" = None
#         self.right: "BSTNode | None" = None
#         self.val = val

#     def insert(self, val: Any) -> None:
#         if self.val is None:
#             self.val = val
#             return

#         if val < self.val:
#             if self.left is None:
#                 self.left = BSTNode(val)
#             else:
#                 self.left.insert(val)
#         elif val > self.val:
#             if self.right is None:
#                 self.right = BSTNode(val)
#             else:
#                 self.right.insert(val)


# Inserting into a binary search tree (like most of its operations) is very fast. Picture the algorithm that you just wrote in your head: how many comparisons does it take to find the right spot for a new node?

# It only requires one comparison for each level of the tree, making it O(log(n))! (At least in a balanced tree, we'll talk about this later).

# Order log(n) is very fast - it's practically as good as O(1) in most cases. If our tree has 1,000,000 nodes, we only need to make 20 comparisons to find the right spot for a new node. If our tree is 2x larger (2,000,000 nodes), we only need to make one more comparison per insert, 21 total.

        # DataStructures/DataStructures/picNotes/insert.png

# What is the average Big O complexity of the .insert method?
# The average Big O complexity of the .insert method in a binary search tree is O(log(n)), where n is the number of nodes in the tree. This is because, in a balanced tree, the height of the tree is logarithmic in relation to the number of nodes, and each insertion operation requires traversing from the root to a leaf node, which takes time proportional to the height of the tree.


# Min and Max
#   ome of the simpler BST algorithms are the get_min and get_max methods.

# from typing import Any


# class BSTNode:
#     def get_min(self) -> Any:
#         current = self
#         while current.left is not None:
#             current = current.left
#         return current.val

#     def get_max(self) -> Any:
#         current = self
#         while current.right is not None:
#             current = current.right
#         return current.val


#     def __init__(self, val: Any = None) -> None:
#         self.left: "BSTNode | None" = None
#         self.right: "BSTNode | None" = None
#         self.val = val

#     def insert(self, val: Any) -> None:
#         if not self.val:
#             self.val = val
#             return

#         if self.val == val:
#             return

#         if val < self.val:
#             if self.left:
#                 self.left.insert(val)
#                 return
#             self.left = BSTNode(val)
#             return

#         if self.right:
#             self.right.insert(val)
#             return
        # self.right = BSTNode(val)




# Delete
#     We also need a way to remove users from our BST if a user decides to delete their account.
from typing import Any


class BSTNode:
    def delete(self, val: Any) -> "BSTNode | None":
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self

        # If we get here, we found the node to delete
        if not self.left and not self.right:
            return None
        if not self.left:
            return self.right
        if not self.right:
            return self.left

        # If we get here, the node has two children
        min_larger_node = self.right.get_min()
        self.val = min_larger_node
        self.right = self.right.delete(min_larger_node)
        return self
        


    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self) -> Any:
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self) -> Any:
        current = self
        while current.right is not None:
            current = current.right
        return current.val


# Deletion Review
#     The delete method is O(log(n)) because, like most binary tree operations, we don't have to search the entire tree. We only have to search one path from the root to the leaf node we want to delete.

# The depth of the tree on average is equal to log base 2 of the number of nodes in the tree. For example:
    # Nodes 	Depth
    # 1 	0
    # 2 	1
    # 4 	2
    # 8 	3
    # 16 	4
    # 32 	5
    # 64 	6
    # 128 	7
    # 256 	8
    # 512 	9
    # 1024 	10
    # 2048 	11
    # 4096 	12

# We only need to use ~10 steps to delete a node from a tree of ~1000 nodes.


# what is the approximate depth of a tree with 16,000 nodes?
#     The approximate depth of a tree with 16,000 nodes can be calculated using the formula for the depth of a binary tree, 
#     which is log base 2 of the number of nodes.

#     depth = log2(16,000) ≈ 14

# What is the average Big O of the delete method?
#     The average Big O complexity of the delete method in a binary search tree is O(log(n)), 
#     where n is the number of nodes in the tree. This is because, on average, the delete operation requires traversing from the root to a leaf node, 
#     which takes time proportional to the height of the tree. In a balanced binary search tree, the height is logarithmic in relation to the number 
#     of nodes, resulting in O(log(n)) complexity for deletion.









# Preorder Traversal
#     A "preorder" traversal is a way to visit all the nodes in a tree. It's called "preorder" because the current node is visited before its children. 
#     This tree:

        # DataStructures/DataStructures/picNotes/preorder.png
            # Would be traversed in this order:
                # [5, 3, 2, 8, 7, 10, 9, 12]

from typing import Any


class BSTNode:
    def preorder(self, visited: list[Any]) -> list[Any]:
        visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)



# Postorder Traversal
#     A "postorder" traversal also visits all the nodes in a tree. It's called "postorder" because the current node is visited after its children. 
#     The following tree:

        # DataStructures/DataStructures/picNotes/postorder.png
            # Would be traversed in this order:
                # [2, 3, 7, 9, 12, 10, 8, 5]

from typing import Any


class BSTNode:
    def postorder(self, visited: list[Any]) -> list[Any]:
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)




# Inorder Traversal
#     An "inorder" traversal is the most intuitive way to visit all the nodes in a tree. 
#     It's called "inorder" because the current node is visited between its children. 
#     It results in an ordered list of the nodes in the tree. 
# 
#       The following tree:

        # DataStructures/DataStructures/picNotes/inorder.png
            # Would be traversed in this order:
                # [2, 3, 5, 7, 8, 9, 10, 12]

from typing import Any


class BSTNode:
    def inorder(self, visited: list[Any]) -> list[Any]:
        if self.left:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


# Node Exists
#     On LockedIn, it's common for one user to navigate directly to another user's profile. We even creepily give the stalked user a notification that someone is looking at their profile.

# To make this feature work, we need to be able to quickly check if a user exists in our tree.

from typing import Any


class BSTNode:
    def exists(self, val: Any) -> bool:
        if self.val == val:
            return True

        if val < self.val:
            if self.left:
                return self.left.exists(val)
            return False

        if self.right:
            return self.right.exists(val)
        return False

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


# Height
#     Our DevOps team has been concerned with the hardware required to run the software using our BST. In an effort to diagnose the issue, they've asked us to write a method that returns the height of the tree. For example, this tree:

#         > Elrond#3
#     > Elian#2
#         > Astram#1

# Has a height of 2 because the longest path from the root node to a leaf node is 2 nodes long.

from typing import Any


class BSTNode:
    def height(self) -> int:
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1
        return 1 + max(left_height, right_height)

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return  

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)



        # Stacks and queues are O(1) which is less than O(log(n)) but they are not searchable
            # binary search trees are O(log(n)) which is more than O(1) but they are searchablekkk
