from random import randint

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        result = 0
        temp = self.head
        while temp:
            result += 1
            temp = temp.next
        return result

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return self.tail

    def generate(self, num, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(num):
            self.add(randint(min_value, max_value))
        return self

    def average(self):
        if self.head is None:
            return 'No element in list.'
        else:
            result = 0
            count = 0
            current = self.head
            while current:
                result += current.value
                current = current.next
                count +=1
            return result/count


# mylist = Linkedlist()
# mylist.generate(8, 1, 100)
# print(mylist)
# print(len(mylist))
# print(mylist.average())