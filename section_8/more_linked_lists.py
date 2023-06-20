class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head

        self.length = 1

    # Append new node to the end of the list
    def append(self,value):
        new_node = Node(value)

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return self

    # prepend new node to the beginning of the list
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

        return self

    def insert(self, index, value):
        if index == 1:
            return self.prepend(value)

        if index >= self.length:
            return self.append(value)

        leader = self.head
        for i in range(index - 2):
            leader = leader.next
        after = leader.next
        new_node = Node(value)
        new_node.next = after
        leader.next = new_node
        self.length += 1

        return self

    def printlist(self):
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next
        return array

    def remove(self,index):
        if index == 1:
            self.head = self.head.next
            return self.printlist()

        to_remove = self.head
        for i in range(index - 2):
            to_remove = to_remove.next

        not_wanted = to_remove.next
        to_remove.next = not_wanted

        self.length -= 1

        return self.printlist()

    def reverse(self):
        if not self.head.next:
            return self.printlist()

        first = self.head
        self.tail = self.head
        second = first.next
        for i in range(self.length):
            # Third item
            tmp = second.next

            second.next = first

            first = second

            second = tmp

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
