# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3

>>> L=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
>>> L
[21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39
>>> def even(L):
...     for i in L:
...             if i % 2 == 0:
...                     print i
...
>>> even(L)
22
24
26
28
30
32
34
36
38
>>> def multiply(L):
...     for i in L:
...             if i % 3 == 0:
...                     print i
...
>>> multiply(L)
21
24
27
30
33
36
39

# Exercise 2
# Print the last two elements of L 
>>> print(L[-1],L[-2])
(39, 38)

# Exercise 3
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once

L = ['1', '2', '3']
for i in range(10)
    if i in L:
    print(i is in the list)
    else:
    print(i not found)

>>> L=[1,2,3]
>>> for i in range(10):
...     if i in L:
...             print ('i is in the list')
...     else:
...             print ('i not found')
...
i not found
i is in the list
i is in the list
i is in the list
i not found
i not found
i not found
i not found
i not found
i not found
    


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 

>>> f=open('sprot_prot.fasta','r')
>>> f.readline()
>>> print(line.split("OS="))
['HGGCGRYQPRIRRSGLELYAEWKHVNEDSQEKKILLSPERVHEIFKRISDEECFVLGMEP\n']


# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string

>>> f = open('sprot_prot.fasta')
>>> line = f.readline()
>>> line = line.split("OS=")[1]
>>> line = line.split(" ")
>>> print(line[0], line[1])
('Homo', 'sapiens')


# Exercise 6
# reverse the string 'asor rosa'

>>> L = 'asor rosa'
>>> print(L[::-1])
asor rosa



# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]


>>> L = [1,7,3,9]
>>> L.sort()
>>> L
[1, 3, 7, 9]

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6

table = [[2,4],[3,6]]
