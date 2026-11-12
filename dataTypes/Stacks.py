class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stacks:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

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






a = Stacks()

a.push('o')
a.push('l')
a.push('l')
a.push('e')
a.push('h')

print(a)

a.reverse()
print(a)

print(a.pop())