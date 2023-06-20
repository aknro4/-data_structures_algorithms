class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    # End of the list
    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return self
    # add new node to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
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
        new_node.pre = pre
        pre.prev = new_node
        # Previous nodes new next value is the inserted value.
        pre.next = new_node
        self.length += 1
        return self

    def remove(self, index):
        if index == 1:
            self.head = self.head.next
            self.length -= 1
            return self

        # Remove
        lead = self.head
        for i in range(index - 2):
            lead = lead.next
        unwanted = lead.next
        lead.next = unwanted.next
        self.length -= 1

        return self.printList()


linked_list = LinkedList(10) # 2
linked_list.append(5) # 3
linked_list.append(16) # 4
linked_list.append(45) # 5
linked_list.append(123) # 6
linked_list.append(54) # 7
linked_list.append(6) # 8
linked_list.append(57) # 9
linked_list.append(23) # 10
linked_list.prepend(1) # 1
linked_list.insert(6, 19)


print(linked_list.printList())


