class Node:
    def __init__(self, value):
        self.previous = None
        self.data = value
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def append(self, value):
        new_node = Node(value)

        new_node.next = self.head
        if self.head != None:
            self.head.previous = new_node
        self.head = new_node

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    def reverse(self):
        curr = self.head
        previous = None

        while curr != None:
            next_node = curr.next
            curr.next = previous
            curr.previous = next_node
            previous = curr
            curr = next_node

        self.head = previous



DLL = DoubleLinkedList()
DLL.append(2)
DLL.append(3)
DLL.append(5)
DLL.append(24)
DLL.append(45)
DLL.append(66)
DLL.append(90)
DLL.append(6)
print(DLL)

DLL.reverse()

print(DLL)