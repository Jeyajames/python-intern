#1.multiple argument x with argument y
z =lambda x, y : x * y
print(z(5,2))

#2.to create fibonacci series on n using lambda
from functools import reduce
fib = lambda n: reduce(lambda x, _:x+[x[-1]+x[-2]],range(n-2),[0,1])
print(fib(6))

#3.multiply each number of given list with a given number
a=[3,6,1]
b=[1,2,3]
print(list(map(lambda y,z:y*z,a,b)))

#4.To find number divisible by 9 from a list of numbers
d=[5,9,15,18,81,7,999]
result=list(filter(lambda x:(x%9==0),d))
print("number divisible by 9 are",result)

#5.To count the evan number in a given list of integers
l1=[6,7,99,763,88]
even_count = len(list(filter(lambda g:(g%2 == 0),l1)))
print("even numbers are:",even_count) 
