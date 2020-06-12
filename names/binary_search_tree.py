"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = new_node
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # pass
        # current = self
        # if target is current.value:
        #     return True
        # elif target < current.value:
        #     current = self.left
        #     if target is current.value:
        #         return True
        #     else:
        #         return current.contains(target)
        # else: # target > current.value
        #     current = self.right
        #     if target is current.value:
        #         return True
        #     else:
        #         return current.contains(target)    

        # current = self.value
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)             

    # Return the maximum value found in the tree
    def get_max(self):
        node = self.value
        if self.right:
            return self.right.get_max()
        else:
            return node

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)


# b = BSTNode(5)
# print(b.value, b.left, b.right)
# b.insert(2)
# print(b.value, b.left.value, b.right)
# b.insert(3)
# print(b.value, b.left.value, b.right.value)
# b.insert(7)
# print(b.value, b.left.value, b.right.value)
# b.insert(6)
# print(b.value, b.left.value, b.right.value)
# print("contains 7", b.contains(7))
# print("contains 8", b.contains(8))
# print("contains 6", b.contains(6))
# print("contains 5", b.contains(5))







    # # Part 2 -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     pass

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
