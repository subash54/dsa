class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def disp(self):
        t=self.head
        while(t):
            print(t.data)
            t=t.next

def insert(a,k):
    temp=node(k)
    if(a.head==None):
        a.head=temp
    else:
        t=a.head
        while(t.next!=None):
            t=t.next
        t.next=temp


a=linklist()
for i in range(1,10,2):
    insert(a,i)
a.disp()