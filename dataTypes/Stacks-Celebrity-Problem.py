class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def count(self):
        curr = self.top
        idx = 0

        while curr != None:
            idx += 1
            curr = curr.next

        return idx

    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node
    
    def __str__(self):
        curr = self.top
        result = ''

        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    def peek(self):
        return self.top.data

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data

    def reverse(self):
        curr = self.top
        previous = None

        while curr != None:

            next = curr.next
            curr.next = previous
            previous = curr
            curr = next

        self.top = previous


l = [
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
]


def Find_Celebrity(l):
    s = Stack()

    # Inserting Indexes into the stack
    for i in range(len(l)):
        s.push(i)

    # popint 2 at the same time and checking if they know each other or not
    while s.count() >= 2:
        c1 = s.pop()
        c2 = s.pop()

        if l[c1][c2] == 0:
            # means c2 is not a celeb
            s.push(c1)
        else:
            # means c1 is not a celeb
            s.push(c2)

    # looping through the last item 
    celeb = s.pop()

    for i in range(len(l)):
        if i != celeb:
            if l[i][celeb] == 0 or l[celeb][i] == 1:
                return print('No celebrity')

    return print(celeb)


Find_Celebrity(l)
