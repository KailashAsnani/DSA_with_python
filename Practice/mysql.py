'''import sqlite3

connection = sqlite3.connect("gfg.db")

crsr = connection.cursor()

print("Connected to the database")
# connecting to the database
connection = sqlite3.connect("gfg.db")

# cursor
crsr = connection.cursor()

# primary key
pk = [2, 3, 4, 5, 6]

# Enter 5 students first names
f_name = ['Nikhil', 'Nisha', 'Abhinav', 'Raju', 'Anshul']

# Enter 5 students last names
l_name = ['Aggarwal', 'Rawat', 'Tomar', 'Kumar', 'Aggarwal']

# Enter their gender respectively
gender = ['M', 'F', 'M', 'M', 'F']

# Enter their jpining data respectively
date = ['2019-08-24', '2020-01-01', '2018-05-14', '2015-02-02', '2018-05-14']

for i in range(5):
    # This is the q-mark style:
    crsr.execute(f'INSERT INTO emp VALUES ({pk[i]}, "{f_name[i]}", "{l_name[i]}", "{gender[i]}", "{date[i]}")')

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# close the connection
connection.close()'''

'''n = int(input("Enter a number "))
osum = 0
esum = 0
for i in range(1,n+1):
    if(n%i==0):
        if i%2==0:
            esum += i
        else:
            osum += i


print("Sum of even factors is ", esum)
print("sum of odd factors is ", osum)

import math

r = float(input("Enter the radius"))
ar = float(input("enter the area of square"))

cir = 2*math.pi*r
side = ar**0.5
perimeter = 4*side
if(cir>perimeter):
    print("True")
else:
    print("False")


import socket
s=socket.socket()
host_ip=socket.gethostbyname("www.google.com")
s.connect((host_ip,80))
print("The socket is successfully connected to google",host_ip)
s.close()'''


'''d = {}
n = int(input())
for i in range(1,n+1):
    d[i] = i*i

print(d)


def answer(X, K):
    # Computing MAX
    MAX = pow(10, K) - 1

    # returning ans
    return (MAX - (MAX % X))


X = 40
K = 3

print(answer(X, K))'''

file = open("sample.txt",'w')
file.write("kailash is a great boy i love him and he is the best and will always be")
print(file.tell())

file = open("sample.txt",'r')
file.seek(4)
#to read the next 5 characters
print(file.read(5))

pos = file.tell() +10
print(pos)

file  = open("test.txt",'w')
file.write("kailash")
file.write("\n" )
file.write("satvik")

file = open('test.txt')
letter = file.read(4)
print(letter)

# read the content of the file opened
content = file.readlines()

# to read the first line
print("first line", content[0])


