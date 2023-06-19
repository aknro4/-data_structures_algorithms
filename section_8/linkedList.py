class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

        return self

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

        return self


linked_list = LinkedList(10)
linked_list.append(5)
linked_list.append(16)
linked_list.prepend(1)
print(linked_list.head)
