Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1. create a list of n integer values
>>> a=[3,8,5,1,7,9,6]
>>> (a.append(2))
>>> print(a)
[3, 8, 5, 1, 7, 9, 6, 2]
>>> #delete
>>> a.remove(9)
>>> print(a)
[3, 8, 5, 1, 7, 6, 2]
>>> #store the largest number from the list to a variable
>>> A=max(a)
>>> print(A)
8
>>> #store the smallest number from the list to a variable
>>> A=min(a)
>>> print(A)
1
>>> # 2.create a tuple and print the reverse of the created tuple
>>> Z=('d','f','v','h','o')
>>> Z=tuple(reversed(Z))
>>> print(Z)
('o', 'h', 'v', 'f', 'd')
>>> # 3.create a tuple and convert tuple into list
>>> aList=list(Z)
>>> print(aList)
['o', 'h', 'v', 'f', 'd']
>>> 