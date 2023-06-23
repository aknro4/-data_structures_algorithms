class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            # Keep track of the current node.
            current_node = self.root
            while True:
                # If the current node value is smaller than the inputted value. Focus on the left side of the tree
                if current_node.value <= value:
                    # Check if there is a node on the right. if not new node is inserted.
                    if current_node.right is None:
                        current_node.right = new_node
                        return self
                    # Other cases we update the new node.
                    else:
                        current_node = current_node.right
                # If the current node is larger than the inputted value. Focus on the left side of the tree
                else:
                    # Check if there is a node on the left. if not new node is inserted.
                    if current_node.left is None:
                        current_node.left = new_node
                        return self
                    # Other cases we update the new node.
                    else:
                        current_node = current_node.left

    # Return true or false depending on if the value is in the tree.
    def lookup(self, value):
        if self.root.value == value:
            return True
        current_node = self.root
        while True:
            # Checks if the value is found. else keep looping.
            if current_node.value == value:
                return True

            # Check if the value is larger than the right value
            if current_node.value <= value:
                # If we are at the end of the tree should return false.
                if current_node.right is None:
                    return False
                # Else set the current node to the right value
                else:
                    current_node = current_node.right
            # If the value was smaller. Then we focus on the left side
            else:
                # If we are at the end of the tree should return false.

                if current_node.left is None:
                    return False
                # Else set the current node to the left value
                else:
                    current_node = current_node.left


tree = BST()

tree.insert(10)
tree.insert(20)
tree.insert(14)
tree.insert(4)
tree.insert(8)
tree.insert(11)
tree.insert(9)
print(tree.lookup(11))