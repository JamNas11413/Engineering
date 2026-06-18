# reguler binary search tress have a problemm, they have no buuilt in protection againist unbalanced 
    # so if we insert an ordered list to a binary tree, you will endup ina single branch in your tree, which is 
        # no better than a linked list, the efficient order log n lookups degrades into O(n)

        # but a balanced tree is faster 

    # so how van we keep our tree balanced:
        # this is where red-black data structure comes in => it solves the problem 
        # when item are inserted or removewd from a redblack tree we have a little extra step
        #   # take insertion:   
        #        after inserting a new item into RB tree, we have a fix step 
                    # in the fix step we check the state of the tree and if it ks strated to become unbalnced 
                    # we perform a rotatiton(which is where we take the longer branch of the tree and it foled it back into the rest which flattened the tree as a whole )

        # the colors red and black:
            # red and black: they are just boolean values that we attached to each node (True = black or False = red)
            # we use the color sowe can draw out and visualize 

            # the idea is every node has a extra bit of info (self.red = False) 
            # and we use the colors to know wheter the tree is sufficiently balanced or not 


            # the last rule is realyy the ticket
                    # when a branch start to get too long we rebalance the tree and perform a rotation to make shure it still follow the rules
                    # rotationm can be both left and right the right is just mirrorof the left 

# Unbalanced Trees    
#     BSTs have a problem. While it's true that on average a BST has O(log(n)) lookups, deletions, 
#         and insertions, that fundamental benefit can break down quickly.

    # If mostly sorted data, or even worse, completely sorted data, is inserted into a binary tree, the tree will be much deeper than it is wide. 
    #     As you know by now, the Big O complexity of the tree's operations depend entirely on the depth of the tree.



# Unbalanced Tree
    # unbalanced trees are binary trees that do not enforce any specific rules on their structure.

    # DataStructures/DataStructures/picNotes/unbalanced_tree.png

# Balanced Trees
    # Balanced trees are a class of binary trees that maintain their depth to be O(log(n)) for all operations. 
    #     This is done by enforcing a set of rules on the tree's structure. 
    #     The rules are designed to ensure that the tree remains balanced,
    #     meaning that the left and right subtrees of any node differ in height by at most one. 
    #     This balance ensures that the tree remains efficient for lookups, insert


        # DataStructures/DataStructures/picNotes/balanced_tree.png



# Notice that both trees are valid BSTs, and both have the same number of nodes. The trouble is, 
#   in the unbalanced tree, there are more levels to traverse, bringing the Big O complexity closer 
#   to O(n) than O(log(n)).



# If 100 sorted items are inserted into a BST in order, what will be the Big O complexity of lookups? and why
    # Inserting 100 sorted items into a binary search tree (BST) in order will result in an unbalanced tree that resembles a linked list. 
    #  In this case, the depth of the tree will be equal to the number of nodes, which is 100.
        # every node will have only the right chiled and it will behave like a linnked list 

        # so complexity of lookups will be O(n) because in the worst case, you may have to traverse all 100 nodes to find a specific item.

# Assuming the tree remains balanced, will a balanced tree's operations ever degrade past O(log(n))?
    # No, a balanced tree's operations will not degrade past O(log(n)) as long as the tree remains balanced. 
    # The balancing rules ensure that the height of the tree is kept in check, preventing it from becoming too deep. 
    # Therefore, the time complexity for lookups, insertions, and deletions will remain O(log(n)) in a balanced tree.





# Red-Black Tree
#     A red-black tree is a kind of binary search tree that solves the "balancing" problem. It contains a 
#         bit of extra logic to ensure that as nodes are inserted and deleted, the tree remains relatively 
#         balanced.



# How It Works
#     Each node in an RB Tree stores an extra bit, called the "color": either red or black. 
#       The "color" ensures that the tree remains approximately balanced during insertions and deletions. 
#       When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties 
#       that constrain how unbalanced the tree can become in the worst case.

            # DataStructures/DataStructures/picNotes/red_black.png

        # The "red" and "black" nomenclature is arbitrary - you could call them "red vs blue" trees (shout-out rooster teeth), or not even call it "color" at all. The important part is just that we now have two "types" of nodes and that will affect the algorithm for balancing it.


# Rules
#     In addition to all the rules of a Binary Search Tree, a red-black tree must follow some additional ones:
#         Each node is either red or black
#         The root is black. (This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.)
#         All Nil leaf nodes are black.
#         If a node is red, then both its children are black.
#         All paths from a single node go through the same number of black nodes to reach any of its descendant NIL(black) nodes.



from typing import Any


class RBNode:
    def __init__(self, val: Any) -> None:
        self.red = False
        self.parent: "RBNode | None" = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val: Any) -> None:
        

# Perfectly Balanced? 
#     The re-balancing of a red-black tree does not result in a perfectly balanced tree. 
#     It only limits how unbalanced a tree may become. However, its insertion and deletion operations, 
#     along with the tree rearrangement and recoloring, are always performed in O(log(n)) time.


        # DataStructures/DataStructures/picNotes/perfectly_balanced.png


# Red-black trees are perfectly balanced
    # False. Red-black trees are not perfectly balanced, but they do maintain a balance that ensures O(log(n)) time complexity for operations. 
    # The rules of red-black trees allow for some level of imbalance, but they prevent the tree from becoming too unbalanced, ensuring efficient performance.

# Red black trees always have worst-case O(log(n)) insertions, deletions, lookups and rearrangements
    # True. Red-black trees maintain a balance that ensures that the height of the tree is O(log(n)). 
    # This means that the worst-case time complexity for insertions, deletions, lookups, and rearrangements in a red-black tree is O(log(n)). 
    # The properties of red-black trees guarantee that the tree remains balanced, preventing it from degrading to O(n) in the worst case.





# Rotation
    # "Rotations" are what actually keep a red-black tree balanced. Every time one branch of the tree 
    #    starts to get too long, we will "rotate" those branches to keep the tree shallow. A shallow 
    #    tree is a healthy (fast) tree!

    #     A properly-ordered tree pre-rotation remains a properly-ordered tree post-rotation
    #     Rotations are O(1) operations 
    #     When rotating left:
    #         The "pivot" node's initial parent becomes its left child
    #         The "pivot" node's old left child becomes its initial parent's new right child

    # Here's the process of a "left rotation":
        # DataStructures/DataStructures/picNotes/left_rotation.png


from typing import Any


class RBNode:
    def __init__(self, val: Any) -> None:
        self.red = False
        self.parent: "RBNode | None" = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, pivot_parent: RBNode) -> None:
        pass

    def rotate_right(self, pivot_parent: RBNode) -> None:
        pass


    def insert(self, val: Any) -> None:
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

# Fix Insert
#     Rotations are only useful if we can use them. When new nodes are inserted into the tree, they can break the red-black properties. We'll fix that by rotating the tree as new nodes are inserted, ensuring the tree remains balanced.

#     When we're done here, we will have a fully functional (albeit insert-only) red-black tree. As you can see if you look at the bottom of the test suite, we'll be inserting numbers into our tree in order. A normal binary tree would break down into a single unruly branch:

#                   > 7
#                > 6
#             > 5
#          > 4
#       > 3
#    > 2
# > 1


#     But our red-black tree will remain balanced, 

#      > 7
#    > 6
#       > 5
# > 4
#       > 3
#    > 2
#       > 1


from typing import Any


class RBNode:
    def __init__(self, val: Any) -> None:
        self.red = False
        self.parent: "RBNode | None" = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val: Any) -> None:
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # ?

    def fix_insert(self, new_node: RBNode) -> None:
        pass

    def exists(self, val: Any) -> RBNode:
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

# To be a valid RB tree, a black node must have red children
    # False. In a red-black tree, a black node can have either red or black children. 
    # The only requirement is that if a node is red, then both of its children must be black. 
    # There is no restriction on the color of the children of a black node.