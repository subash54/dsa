class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def insert(self,a):
        t=Node(a)
        if(self.head==None):
            self.head=t
        else:
            p=self.head
            while(p.next):
                p=p.next
            p.next=t
    def deleteAlt(self):
        t=self.head
        while(t and t.next):
            t.next=t.next.next
            t=t.next

    def disp(self):
        t = self.head
        while (t):
            print(t.data)
            t = t.next


l=linklist()
print("enter the length of link list")
d=int(input())
for num in range(0,d):
    l.insert(num)
l.deleteAlt()
l.disp()