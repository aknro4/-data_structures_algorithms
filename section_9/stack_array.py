class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.array = []

    # See the top item in the stack
    def peek(self):
        return self.array[-1]

    # remove/pop the top item
    def pop(self):
        return self.array.pop()

    # Add item to stack
    def push(self, value):
        return self.array.append(value)


stack = Stack()
stack.push("google")
stack.push("udemy")
stack.push("discord")

print(stack.peek())
stack.pop()
print(stack.peek())
