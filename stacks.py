class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self,head=None):
        self.head=head
    
    def push(self,data):
        newNode=Node(data)
        if self.head:
            newNode.next=self.head
        self.head=newNode
    
    def delete(self):
        if self.head.next: 
            self.head=self.head.next
        else:
            self.head=None
    def print_max(self):
        Max=self.head.data
        current=self.head
        if self.head:
            while current:
                if current.data>Max:
                    Max=current.data
                current=current.next
        return Max
s=Stack()
N=int(input())
for i in range(N):
    In=list(map(int,input().split()))
    if In[0]==1:
        s.push(In[1])
    elif In[0]==2:
        s.delete()
    elif In[0]==3:
        print(s.print_max())
