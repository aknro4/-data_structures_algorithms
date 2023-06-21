class MyQueue(object):

    def __init__(self):
        self.array = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return self.array.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.array.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.array[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.array) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

