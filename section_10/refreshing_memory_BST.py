import json


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

    def remove(self, value):
        if not self.root:
            return False

        current_node = self.root
        parent_node = None
        while current_node:
            # If value is larger than the current node go to the right
            if value >= current_node.value:
                parent_node = current_node
                current_node = current_node.right
            # If value is smaller than the current node go to the left
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left

            # Value found, start deleting procedure.
            elif value == current_node.value:
                # Option 1, Node has no right child
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                    else:
                        # if parent is larger than current value, make current left child a child of a parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        # if parent is smaller than current value, make current right child a child of a parent
                        else:
                            parent_node.right = current_node.left

                # Option 2, Right child which does not have left child
                elif current_node.right.left is None:
                    current_node.left.right = current_node.left
                    if parent_node is None:
                        self.root = current_node.right
                    else:
                        # if parent is larger than current value, make right child of the left the parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        # if parent is smaller than current value, make right child a right child of the parent
                        else:
                            parent_node.right = current_node.right

                # Option 3, Right child has no left child
                else:
                    # Find the Right child most left child.
                    left_most = current_node.right.left
                    left_most_parent = current_node.right
                    while left_most.left is not None:
                        left_most_parent = left_most
                        left_most = left_most.left

                    # Parent's left subtree is now leftmost's right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if parent_node is None:
                        self.root = left_most
                    else:
                        # if parent is larger than current value, make right child of the left the parent
                        if current_node.value < parent_node.value:
                            parent_node.left = left_most
                        # if parent is smaller than current value, make right child a right child of the parent
                        else:
                            parent_node.right = left_most
        return True


tree = BST()

tree.insert(9)
tree.insert(20)
tree.insert(4)
tree.insert(1)
tree.insert(6)
tree.insert(5)
tree.insert(15)
tree.insert(7)
tree.insert(170)
tree.remove(5)

print(tree.lookup(5))


# Something to make something more readable which does not work and not cared to fix it. :D
def traverse(node):
    tree = {'value': node.value, 'left': None if node.left is None else traverse(node.left),
            'right': None if node.right is None else traverse(node.right)}
    return tree


print(json.dumps(traverse(tree.root)))
