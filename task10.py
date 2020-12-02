#1. python program for all use cases
import re
#match()
a = re.match('[A-Z]+','I like red color')
print(a)
#search()
a_se = re.search('Red','i like Red color')
print(a_se)
#findall()
a_fn = re.findall("[a-zA-Z0-9]+","Welcome to our internship day10")
print(a_fn)
#split()
a_spl = re.split('[l]+','welcome')
print(a_spl)
#sub()
a_su = re.sub('day10','day-11','welcome to our internship day10')
print(a_su)

#2.program that matches a word containing 'ab'
import re
b=re.match('ab','ab is lowercase letter')
print(b)

#3.python program to check for a numnber at the end of a word or sentence
import re
b_fn = re.findall('[0-9]+','my data birth is july 2000')
print(b_fn)

#4.python program to search the number (0,9)of length between 1 to 3 in a given string
import re
result=re.findall(r"([0-9]{1,3})","the numbers are 5,20,135 and 23")
print(result)

#5.python program to match string that contains only uppercase letters
import re
c_ma = re.match('[A-Z]+','PYTHON ia an high level programming language')
print(c_ma)
