class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear == None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        curr = self.front
        self.front = self.front.next
        return curr.data

    def __str__(self):
        curr = self.front
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]



q = Queue()
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
print(q)

q.dequeue()
print(q)