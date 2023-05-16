class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        Node = self.head
        while Node:
            yield Node
            Node = Node.next

    def createList(self, nodeValue):
        node1 = node(nodeValue)
        node1.next = None
        node1.prev = None
        self.head = node1
        self.tail = node1
        return 'Successflly created'

    def inserNode(self, value, location):
        if self.head is None:
            print("no list")
        else:
            newNode = node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = None
                self.head.prev = newNode
                self.head = newNode

            elif location == -1:
                newNode.prev = self.tail
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    def reverseTraverse(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
    def search(self,nodeValue):
        if self.head is None:
            return 'No list is there'
        else:
             current = self.head
             while current:
                if current.value == nodeValue:
                    return nodeValue
                current=current.next
             return 'No such Node'
    def delete(self,location):
        if self.head is None:
            return 'No element in list'
        else:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            elif location==0:
                self.head=self.head.next
                self.head.prev=None
            elif location==-1:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                temp = self.head
                index=0
                while index<location:
                    if temp==self.tail:
                        return 'index out of range'
                    temp=temp.next
                    index+=1
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
    def deleteList(self):
        if self.head==None:
            return 'List already deleted'
        else:
            temp = self.head
            while temp:
                temp.prev=None
                temp=temp.next
            self.head=None
            self.tail=None


myList = doubleLinkedList()
myList.createList(8)
print([va.value for va in myList])
myList.inserNode(1, 0)
#print([nodes.value for nodes in myList])
myList.inserNode(20, -1)
#myList.traverse()
#print([node.value for node in myList])
myList.inserNode(33, 2)
#print([node.value for node in myList])
#myList.traverse()
#myList.reverseTraverse()
# print(myList.search(20))
# print(myList.search(1))
myList.inserNode(15,0)
myList.inserNode(30,-1)
myList.inserNode(99,5)
print([moo.value for moo in myList])
myList.delete(15)
myList.delete(1)
print([foo.value for foo in myList])

one = doubleLinkedList()
one.createList(20)
#print([my.value for my in one])
one.inserNode(10, -1)
#print([my.value for my in one])
#one.traverse()
