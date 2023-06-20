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
        self.tail.next = new_node
        self.tail = new_node
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
        for i in range(index - 2):
            leader = leader.next
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
        # Instead of trying to access the next node which does not exist
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

    def reverse(self):
        if self.length == 1:
            return self.printlist()

        first = self.head
        # Tail is now first item
        self.tail = self.head
        # Hold next node from the first node
        second = first.next
        while second:
            # Holds third node
            temp = second.next

            # Second node next node which is third node, is now first node.
            second.next = first

            # First node is second node
            first = second

            # Second becomes third
            second = temp

        self.head.next = None
        self.head = first

        return self.printlist()



linked_list = LinkedList(10)
linked_list.append(5) # 3
linked_list.append(16) # 4
linked_list.append(45) # 5
linked_list.append(123) # 6
linked_list.append(54) # 7
linked_list.append(6) # 8
linked_list.append(57) # 9
linked_list.append(23) # 10
linked_list.prepend(1) # 1
linked_list.insert(index=6, value=19)

print(linked_list.printlist())

print(linked_list.reverse())


