class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    # return first element/node
    def peek(self):
        return self.first.value

    # add a new element to the queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return self
        # self.first.next = new_node
        # self.first = new_node
        # First time around did it reversed, and that got me confused.
        self.last.next = new_node
        self.last = new_node
        self.length += 1

        return self

    # Remove the first element from the queue
    def dequeue(self):
        # When deleting last item Return an error because of the None value.
        if self.first == self.last:
            self.last = None
            self.length -= 1

        self.first = self.first.next
        self.length -= 1
        return self


queue = Queue()

queue.enqueue("Joy")
queue.enqueue("Matt")
queue.enqueue("Pavel")
queue.enqueue("Samir")

print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
print(queue.length)
