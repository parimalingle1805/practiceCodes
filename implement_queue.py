class queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

q = queue()
q.enqueue(1)
q.enqueue('hahaha')
q.enqueue(True)
q.dequeue()
print(q.size())
print(q.isEmpty())