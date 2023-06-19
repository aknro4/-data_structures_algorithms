class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return self

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

        return self

    def printList(self):
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next
        return array

    # Loop through the linked list. When at the index. set previous nodes next value to new inserted node.
    # and update all the nodes next value to new next values.
    def insert(self, index, value):
        # insert it as first node.
        if index == 1:
            return self.prepend(value)

        # insert it as last node.
        if index >= self.length:
            return self.append(value)

        # Tracing Leading node/value.
        pre = self.head
        # I honestly do not know why we have to index - 2, but somehow it does work.
        # problem was that it would insert 2 places off where it should have been.
        # So figured that we should - 2 the index.
        for i in range(index - 2):
            # While loop would have been better, but this works.
            # Looping nodes until i is at the index. And save the new leading value to pre.
            pre = pre.next
        # new_nodes next value.
        aft = pre.next
        new_node = Node(value)
        new_node.next = aft
        # Previous nodes new next value is the inserted value.
        pre.next = new_node
        self.length += 1
        return self


linked_list = LinkedList(10)
linked_list.append(5)
linked_list.append(16)
linked_list.append(45)
linked_list.append(123)
linked_list.append(54)
linked_list.append(6)
linked_list.append(57)
linked_list.append(23)
linked_list.prepend(1)
linked_list.insert(6, 19)
print(linked_list.printList())
