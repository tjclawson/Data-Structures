import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value and self.right is not None:
            self.right.insert(value)
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
        elif value < self.value and self.left is not None:
            self.left.insert(value)
        elif value < self.value and self.left is None:
            self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        elif target > self.value and self.right is None:
            return False
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        elif target < self.value and self.left is None:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is None:
            print(node.value)
        else:
            self.in_order_print(node.left)
            print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # ititialize queue
        queue = Queue()
        # push root to queue
        queue.enqueue(node)
        # while queue not empty
        while queue.size > 0:
            # pop top item out of queue into temp
            temp_node = queue.dequeue()
            # Do the thing
            print(temp_node.value)
            # if temp has right, put into queue
            if temp_node.right:
                queue.enqueue(temp_node.right)
            # if temp has left, put into queue
            if temp_node.left:
                queue.enqueue(temp_node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # ititialize stack
        stack = Stack()
        # push root to stack
        stack.push(node)
        # while stack not empty
        while stack.size > 0:
            # pop root out of stack to temp
            temp_node = stack.pop()
            # Do the thing
            print(temp_node.value)
            # if temp has right, put into stack
            if temp_node.right:
                stack.push(temp_node.right)
            # if temp has left, put into stack
            if temp_node.left:
                stack.push(temp_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
