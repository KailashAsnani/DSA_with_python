import random

from useLinkedList import Linkedlist, Node


def removeDuplicate(workList):
    if workList.head is None:
        return 'No element in list'
    else:
        current = workList.head
        unique = set([current.value])
        while current.next:
            if current.next.value in unique:
                current.next = current.next.next
            else:
                unique.add(current.next.value)
                current = current.next
        return workList


def nfromlast(workList, n):
    result = workList.head
    counter = workList.head
    for i in range(n):
        if counter is None:
            return None
        counter = counter.next
    while counter is not None:
        result = result.next
        counter = counter.next
    return result.value

def reversesum(ll1, ll2):
    n1 = ll1.head
    n2 = ll2.head
    carry = 0
    ll3 = Linkedlist()
    while n1 or n2:
        result = carry
        if n1:
            result = result + n1.value
            n1 = n1.next
        if n2:
            result = result + n2.value
            n2 = n2.next
        ll3.add(int(result % 10))
        carry = result / 10
    return ll3


def partition(workList, x):
    current = workList.head
    workList.tail = current
    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = workList.head
            workList.head = current
        else:
            workList.tail.next= current
            workList.tail = current
        current = nextNode

def intersection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return False

    len1 = len(ll1)
    len2 = len(ll2)

    shorter = ll1 if len1 < len2 else ll2
    longer = ll2 if len1 < len2 else ll1
    longernode = longer.head
    shorternode = shorter.head

    diff = len(longer) - len(shorter)

    for i in range(diff):
        longernode = longernode.next

    while shorternode is not longernode:
        shorternode = shorternode.next
        longernode = longernode.next
    return longernode

#helping function


def addsimilar(ll1, ll2, num):
    temp = Node(num)
    ll1.tail.next = temp
    ll1.tail = temp
    ll2.tail.next = temp
    ll2.tail = temp


custom = Linkedlist()
custom.generate(20, 1, 50)
# print(custom)
#removeDuplicate(custom)
#print(custom)
print(nfromlast(custom,5))
partition(custom, 28)
# print(custom)
value1 = Linkedlist()
value2 = Linkedlist()
value1.generate(4, 0, 9)
value2.generate(4, 0, 9)
print(value1, value2)
# print(reversesum(value1, value2))
# addsimilar(value1, value2, random.randint(0, 9))
# addsimilar(value1, value2, 6)
# addsimilar(value2, value1, 0)
print(value1, value2)
print(intersection(value1, value2))