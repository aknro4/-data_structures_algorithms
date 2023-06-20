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

    # Append new node to the end of the list
    def append(self, value):
        new_node = Node(value)
        # Adds the new node to the end
        self.tail = new_node
        # New next value to the head.
        self.head.next = self.tail
        self.length += 1

        return self

    # add new node to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        # Assign previous head as a new next value to new node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

        return self

    def insert(self, value,index):
        # If index is 1 we call the function to insert the value as first argument
        if index == 1:
            return self.prepend(value)
        # if index is same length as list length or larger than index
        # we call the function to insert the value at the end.
        if index >= self.length:
            return self.append(value)

        leader = self.head
        while index - 2 >= self.length:
            leader = self.head
        # Current nodes next node do not know better name for it
        after = leader.next
        new_node = Node(value)
        # That node is saved to new nodes next node
        new_node.next = after
        # and the current node or leader node next is the new node
        leader.next = new_node

        self.length += 1

        return self

    def remove(self,index):
        if index == 1:
            self.head = self.head.next
            self.length -= 1
            return self.printlist()
        # Issue, if we want to remove last node. WE get an error of NoneType.
        # Because the last nodes next node does not exist. So the second last node should have next value of none.
        leader = self.head
        for i in range(index - 2):
            leader = leader.next
        unwanted = leader.next
        leader.next = unwanted.next
        self.length -= 1

        return self.printlist()

    def printlist(self):
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next
        return array


linked_list = LinkedList(10)
linked_list.append(12)
linked_list.prepend(9)
linked_list.remove(5)

print(linked_list.printlist())
