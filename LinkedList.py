class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def app(self,data):
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=data
            
        else:
            self.head=data
            
    def addAtStart(self,data):
        #current=self.head
        if self.head:
            data.next=self.head
            self.head=data

    def rev(self):
        prev=None
        current=self.head
        if self.head:
            while current:
                next=current.next
                current.next=prev
                prev=current
                current=next
            self.head=prev


    def Print(self):
        current=self.head
        if self.head:
            while current:
                print(current.data)
                current=current.next


ll=LinkedList()
l=int(input())
for i in range(l):
    data=int(input())
    n=Node(data)
    ll.app(n)
    #ll.addAtStart(n)
ll.rev()
ll.Print()