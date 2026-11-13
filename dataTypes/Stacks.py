class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

    def count(self):
            curr = self.top
            idx = 0
    
            while curr != None:
                idx += 1
                curr = curr.next
    
            return idx

    
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






def TextEditor(text, pattern):
    u = Stack()
    r = Stack()

    for i in text:
        u.push(i)

    for i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)

    result = ''

    while not u.isEmpty():
        result = u.pop() + result

    return result


