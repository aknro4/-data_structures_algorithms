class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    # See the top item in the stack
    def peek(self):
        return self.top.value

    # remove/pop the top item
    def pop(self):
        self.length -= 1
        print("length ", self.length)
        # Could check with the length as well
        if not self.top.next:
            self.top = self.bottom
            return self
        self.top = self.top.next
        return self

    # Add item to stack
    def push(self, value):
        self.length += 1
        old_top = self.top
        new_node = Node(value)

        # Could also check with if not self.top.next
        if self.length == 1:
            self.bottom = new_node
            return self

        new_node.next = old_top
        self.top = new_node
        return self


stack = Stack()
stack.push("google")
stack.push("udemy")
stack.push("discord")

print("Peek ", stack.peek())
stack.pop()
print("After pop peek 1 ", stack.peek())
stack.pop()
print("After pop peek 2 ", stack.peek())

# discord
# udemy
# google
