class BinaryTree(object):
    def __init__(self,rootdata):
        self.key=rootdata
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self,data):
        self.key=data
        
    def getRootVal(self):
        return self.key

b = BinaryTree(1)
b.insertLeft(2)
b.insertRight(3)

b.insertLeft(4)
b.insertRight(5)
b.setRootVal("x")

print(b.getRootVal())
print(b.getLeftChild().getLeftChild().getRootVal())
print(b.getRightChild().getRootVal())