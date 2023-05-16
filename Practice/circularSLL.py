class node:
    def __init__(self,value):
        self.value=value
        self.next=next

class circularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break

    def create(self,nodeValue):
        n = node(nodeValue)
        n.next=n
        self.head=n
        self.tail=n

    def insert(self,nodeValue,location):
        current = node(nodeValue)
        if self.head==None:
            return 'List is not made'
        elif location==0:
            current.next=self.head
            self.head=current
            self.tail.next=current
        elif location==-1:
            current.next=self.tail.next
            self.tail.next=current
            self.tail=current
        else:
            index=0
            temp = self.head
            while index<location-1:
                temp=temp.next
                index+=1
            nextNode = temp.next
            temp.next=current
            current.next=nextNode

    def traverse(self):
        if self.head==None:
            return 'No head in the list'
        temp = self.head
        while temp:
            print(temp.value)
            temp=temp.next
            if temp==self.tail.next:
                break
    def search(self,nodevalue):
        if self.head==None:
            return 'There is no head'
        current=self.head
        while current:
            if current.value==nodevalue:
                return current.value
            current=current.next
            if current==self.tail.next:
                return 'No such data'

    def deleteList(self):
        self.head=None
        self.tail.next=None
        self.tail=None

    def deleteNode(self,location):
        if self.head==None:
            return 'No such list.'
        if location==0:
            if self.head==self.tail:
                self.head.next=None
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.tail.next=self.head

        if location==-1:
            if self.head==self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next!=self.tail:
                    current=current.next
                current.next=self.head
                self.tail=current
        else:
            current = self.head
            index=0
            while index<location-1:
                current=current.next
                index+=1
            nextNode=current.next
            current.next=nextNode.next

    def deleteByValue(self, value):
        pass



cll = circularSLL()
cll.create(1)
cll.insert(1,0)
cll.insert(2,-1)
cll.insert(20,1)
cll.insert(30,-1)
cll.insert(15,4)
cll.traverse()
print(cll.search(20))
print(cll.search(23))

cll.deleteNode(1)
cll.deleteNode(3)
cll.traverse()