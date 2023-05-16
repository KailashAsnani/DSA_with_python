class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createList(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        node.prev = None
        node.next = None

    def insertNode(self, nodeValue, location):
        if self.head is None:
            return 'No list exists'
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                current = self.head
                index = 0
                while index < location:
                    current = current.next
                    index += 1
                    if current == self.tail.next:
                        print("Index out of range")
                        break
                newNode.prev = current.prev
                newNode.next = current
                current.prev.next = newNode
                current.prev = newNode

    def traverse(self):
        if self.head is None:
            print("No such list exists")
        else:
            current = self.head
            while current != self.tail:
                print(current.value)
                current = current.next
            print(self.tail.value)

    def reverseTraversal(self):
        if self.head is None:
            print("No such list exists.")
        else:
            current = self.tail
            while current != self.head:
                print(current.value)
                current = current.prev
            print(self.head.value)

    def delete(self, location):
        if self.head is None:
            print("List is not available")
        else:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None

            elif location == 0:
                self.tail.next = self.head.next
                self.head = self.head.next
                self.head.prev = self.tail

            elif location == -1:
                self.tail = self.tail.prev
                self.head.prev = self.tail
                self.tail.next = self.head

            else:
                current = self.head
                index = 0
                while index < location:
                    current = current.next
                    index += 1
                    if current == self.tail.next:
                        print("Index out of range.Please enter a valid index")
                        exit()
                current.prev.next = current.next
                current.next.prev = current.prev

    def search(self, value):
        if self.head is None:
            return 'No such list exists'
        else:
            index = 0
            current = self.head
            while current:
                if current.value == value:
                    return str(value) + ' found at index ' + str(index)
                current = current.next
                index += 1
                if current == self.tail.next:
                    return 'Node not found'

    def deleteByValue(self, value):
        pass

newList = CircularDoublyLL()
newList.createList(7)
print([val.value for val in newList])
newList.insertNode(10, 0)
newList.insertNode(20, -1)
print([val.value for val in newList])
newList.insertNode(9, 0)
newList.insertNode(11, 3)
newList.insertNode(32, 4)
print([val.value for val in newList])
#newList.traverse()
#newList.reverseTraversal()
newList.delete(0)
newList.delete(-1)
newList.delete(3)
#newList.delete(7)
print([val.value for val in newList])
print(newList.search(11))