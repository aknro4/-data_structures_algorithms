import json


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inserts a node into the tree
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                # Check if current node value is smaller than new value.
                if current_node.value <= new_node.value:
                    # If the value is none then the new node will be inserted to the right
                    if current_node.right is None:
                        current_node.right = new_node
                        print("Root right is none and value is larger than previous node inserting new value "
                              , new_node.value)
                        return self
                    else:
                        # And if the value is not None then set new current node and loop starts again
                        current_node = current_node.right
                        print("Root right is not none and value is larger than root setting new current_node "
                              , new_node.value)
                # if the value is larger than new nodes then...
                else:
                    # If the value is none then the new node will be inserted to the left
                    if current_node.left is None:
                        current_node.left = new_node
                        print("Root left is none and value is smaller than previous node inserting new value "
                              , new_node.value)
                        return self
                    # And if the value is not None then set new current node and loop starts again
                    else:
                        current_node = current_node.left
                        print("Root left is not none and value is smaller than root setting new current_node "
                              , new_node.value)

    # Finds the inputted value return true or false?
    def lookup(self, value):
        new_node = Node(value)
        # If root value is same return true
        if new_node.value == self.root.value:
            return True
        current_node = self.root
        # If not then start looping
        while True:
            # Before comparing which is larger. Always check if we have found the value.
            if current_node.value == value:
                return True

            # Compare which is larger and set current node accordingly
            # And return false if we have reached end of the tree. AKA None value.
            if current_node.value >= new_node.value:
                if current_node.left is None:
                    return False
                current_node = current_node.left
            else:
                if current_node.right is None:
                    return False
                current_node = current_node.right


#      9
#   4    20
# 1  6  15 170

BST = BinarySearchTree()

BST.insert(9)
BST.insert(20)
BST.insert(4)
BST.insert(1)
BST.insert(6)
BST.insert(15)
BST.insert(170)

print(BST.lookup(1701))


# Something to make something more readable
# def traverse(node):
#     tree = {'value': node['value'], 'left': None if node['left'] is None else traverse(node['left']),
#             'right': None if node['right'] is None else traverse(node['right'])}
#     return tree
#
#
# print(json.dumps(traverse(BST.root)))
