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
            if current_node.value <= new_node.value:
                if current_node.right is None:
                    return False
                current_node = current_node.right
            else:
                if current_node.left is None:
                    return False
                current_node = current_node.left

    # Value to be removed will be replaced with by going to right and
    # then replace to be deleted node with the left value.
    # If no left value, we replace it with the right value
    # If the value is last item, just delete it. AKA if no right value else replace it with left value
    def remove(self, value):
        if not self.lookup(value):
            return False
        current_node = self.root
        node_before = current_node
        # Why I feel like this is really, awful code, well comments do make it awful to understand
        while True:
            print("Current node: ", current_node.value)
            print("Node before: ", node_before.value)
            if current_node.value == value:
                print("Current node right ", current_node.right, "Current node left ", current_node.left)
                # DO the removal process.
                # Case if at the end of the tree
                if current_node.right is None and current_node.left is None:
                    if value >= node_before.value:
                        node_before.right = None
                    else:
                        node_before.left = None
                    return self
                last_node = current_node.right
                # If the last node right is None then, set node before right
                # to current nodes left value which is not Null.
                if last_node is None:
                    node_before.right = current_node.left
                    print("Right was None")
                    return self
                while True:
                    print("Before if statements ", last_node.left, last_node.right)
                    # First go right and then Keep looping to the left until at the end of the tree
                    if last_node.left is None:
                        print("last_node left should be NONE ", last_node.left,last_node.value)
                        print("Node before, ", node_before.value, " the node to be deleted ", current_node.value)
                        # Check was the value larger than the node before value.
                        # So we know do we insert last item to left or right for the node_before
                        if node_before.value <= value:
                            node_before.right = last_node
                            print("right ", node_before.right.value)
                        else:
                            node_before.left = last_node
                            print("left ", node_before.left.value)

                        # Replace from the deleted node right and left to last node
                        last_node.left = current_node.left
                        # This line breaks the JSON code some-reason?
                        last_node.right = current_node.right
                        print("after if statements ", last_node.left, last_node.right)
                        print(current_node.right.value)
                        return self
                    # Set the last node to left until left is None.
                    last_node = last_node.left

            elif current_node.value <= value:
                node_before = current_node
                current_node = current_node.right
            else:
                node_before = current_node
                current_node = current_node.left


#      9
#   4    20
# 1  6  15 170

BST = BinarySearchTree()

BST.insert(9)
BST.insert(20)
BST.insert(4)
BST.insert(1)
BST.insert(6)
BST.insert(5)
BST.insert(15)
BST.insert(7)
BST.insert(170)
BST.remove(4)
BST.remove(5)

print(BST.lookup(5))
print(BST.lookup(6))
print(BST.lookup(4))
print(BST.lookup(1))
print(BST.lookup(5))
print(BST.lookup(7))


# Something to make something more readable which does not work and not cared to fix it. :D
# def traverse(node):
#     tree = {'value': node.value, 'left': None if node.left is None else traverse(node.left),
#             'right': None if node.right is None else traverse(node.right)}
#     return tree
#
#
# print(json.dumps(traverse(BST.root)))
