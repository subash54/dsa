class Node:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.root = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.root
        self.root = newnode

    def pop(self):
        if (self.root == None):
            return -1
        temp = self.root.data
        self.root = self.root.next
        return temp
l=Stack()
d=l.pop()
print(d)
