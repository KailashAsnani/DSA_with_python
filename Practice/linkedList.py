
class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        def __iter__(self):
            node = self.head
            while node:
                yield node
                node = node.next

    def insertNode(self,value,location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            if location == -1:
                self.tail.next = newNode
                self.tail=newNode
                newNode.next = None
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverseSLL(self):
        if self.head == None:
            print("The List is empty")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def searchNode(self, nodeValue):
        if self.head == None:
            return "The Linked List is empty"
        node = self.head
        while node:
            if node.value==nodeValue:
                return node.value+10
            node = node.next
        return "tHE value does not exist"

    def deleteNode(self,location):
        if self.head == None:
            return "The list is already empty"
        elif location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head=self.head.next
        elif location == 1:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                node.next=None
                self.tail=node
        else:
            tempNode = self.head
            index = 0
            while index<location-1:
                tempNode = tempNode.next
                index+=1
            nextNode = tempNode.next
            tempNode.next = nextNode.next


singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head=node1
node1.next=node2
singlyLinkedList.tail=node2

singlyLinkedList.insertNode(1,1)
singlyLinkedList.insertNode(3,2)
singlyLinkedList.insertNode(2,1)
singlyLinkedList.insertNode(0,4)
# singlyLinkedList.traverseSLL()
print(singlyLinkedList.searchNode(3))
print(singlyLinkedList.traverseSLL())
singlyLinkedList.deleteNode(2)
print(singlyLinkedList.traverseSLL())
