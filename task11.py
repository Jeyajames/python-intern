Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # using zip() function and list() function,create a merged list of tuples from the two list
>>> a=['z','y','x','f']
>>> b=[7,5,3,2]
>>> c=list(zip(a,b))
>>> print(c)
[('z', 7), ('y', 5), ('x', 3), ('f', 2)]
>>> 
>>> # 2.create a range from 1to8.using zip,merge the given list
>>> li=zip(range(1,9),'abcdefgh')
>>> li
<zip object at 0x000001FA29696380>
>>> list(li)
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h')]
>>> 
>>> #3.using sorted() function
>>> z=['d','b','e','a','f','c']
>>> x=sorted(z)
>>> print(x)
['a', 'b', 'c', 'd', 'e', 'f']
>>> 
>>> #4.write a program using filter function,filter the even number
>>> l1=[1,2,3,4,5,6,7,8,9]
>>> even= lambda x: x%2 ==0
>>> l2= list(filter(even, l1))
>>> print(l2)
[2, 4, 6, 8]
>>> 