class Node:
    def __init__(self, value):
        self.data= value
        self.next = None

class LinkedList:
    def __init__(self):
        # empty linked list
        self.head = None
        # number of nodes
        self.n = 0

    def __len__(self):
        return self.n

    def Insert_Head(self, value):
        # create node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        # update current head value and node count
        self.head = new_node
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

    def append(self, value):
        new_node = Node(value)
        self.n += 1
        if(self.head == None):
            self.head = new_node
            return
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node

    def insert(self, currValue, nextValue):
        new_node = Node(nextValue)
        self.n += 1
        if self.head == None:
            self.head = new_node
            return

        curr = self.head
        while curr != None:
            if curr.data == currValue:
                break
            curr = curr.next

        if curr == None:
            print('Value not Found')
            return
         # updating the new_node data first
        new_node.next = curr.next

        curr.next = new_node

    



    
a = LinkedList()

a.Insert_Head(1)
a.Insert_Head(2)
a.Insert_Head(3)
a.Insert_Head(4)

a.insert(30, 3.6)
# print(len(a))
print(a)
