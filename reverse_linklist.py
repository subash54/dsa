class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class link_list:
    def __init__(self):
        self.head=None

    def rev(self):
        current=self.head
        prev=None
        next=self.head
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

    def disp(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next


one=node(1)
two=node(2)
three=node(3)
four=node(4)
l=link_list()
l.head=one
one.next=two
two.next=three
three.next=four
l.disp()
l.rev()
l.disp()
