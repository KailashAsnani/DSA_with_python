import sys
from array import *

x =2839
print(len(str(x)))
'''
def digitSum(n):
    if(n<10):
        return n
    return  n%10 + digitSum(n//10)

print(digitSum(78919))

def power(base,exp):
    if(exp==0):
        return 1
    return base * power(base,exp-1)
print(power(2,5))

def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
print(gcd(140,35))

def decToBinary(n):
    assert int(n)== n
    if(n==1):
        return 1
    return n%2 + 10*decToBinary(n//2)

print(decToBinary(8))
'''
a = array('i',[1,2,0,3,0,4,5,0,0,6])


def pushZeroEnd(array,n):
    count = 0
    '''traverse array and if not zero print it from 0'''
    for i in range(n):
        if(array[i]!=0):
            array[count]=array[i]
            count+=1
    '''from count to n make zeros'''
    res = count
    for j in range(count,len(array)):
        array[j]=0

    print(array)
    print(res)

pushZeroEnd(a,10)

def avgTemp(n):
    sum=0
    for i in range(1,n+1):
        temp = float(input("Enter day " + str(i) + "'s temperature"))
        sum+=temp

    return "Average temperature is " + str(sum/n)

# n = int(input("Enter the number of days: "))
# print(avgTemp(n))
#
new = [1,2,4,5,71,2,3,4,6]
news=[]
for i in new:
    if(i not in news):
        news.append(i)

print(news)
