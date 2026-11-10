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

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return 'Empty LinkedList'
        self.head = self.head.next
        self.n -= 1

    def pop(self):
        curr = self.head
        if curr.next == None:
            self.delete_head()
        while curr.next.next != None:
            curr = curr.next

        curr.next = None   
        self.n -= 1

    def delete(self, value):
        curr = self.head
        if curr.data == value:
            return self.delete_head()
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            print('Item not in linked list !')
            return
        curr.next = curr.next.next
        self.n -= 1

    def search(self, value):
        if self.head == None:
            return print('Empty')
        
        curr = self.head
        idx = 0

        while curr != None:
            if curr.data == value:
                break
            # increment
            curr = curr.next 
            idx += 1
        if curr == None:
            return print('not found')
        print(idx)

    def __getitem__(self, value):
        curr = self.head
        index = 0

        while curr != None:
            if index == value:
                return str(curr.data)
            # increment
            curr = curr.next
            index += 1
        return 'not found'

    def replace_max_value(self, value):
        temp = self.head
        max = temp
        
        # looping through the LL to find the maximum value
        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next

        # replacing the max value to the value given
        max.data = value

    def sum_odd(self):
        curr = self.head
        idx = 0
        sum = 0

        while curr != None:
            if idx % 2 != 0:
                sum += curr.data
            # increment
            curr = curr.next
            idx += 1
        return sum

    def reverse(self):
        curr = self.head
        previous = None

        while curr != None:
            # initialising and saving the next 
            next = curr.next
            curr.next = previous
            previous = curr
            curr = next

        # updating the head of LL

        self.head = previous
a = LinkedList()

a.Insert_Head(3)
a.Insert_Head(5)
a.Insert_Head(6)
a.Insert_Head(8)
a.Insert_Head(9)

# print(len(a))
print(a)
a.reverse()
print(a)



