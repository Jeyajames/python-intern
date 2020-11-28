#5. multiplication table of 9
n=int(input("Enter the number:"))
for i in range(1,10):
    print(n,"*",i,"=",n*i)

#6.to convert the number of days to age
import datetime
year=datetime.datetime.now().year
year_of_birth=int(input("enter your birth year:"))
print(year-year_of_birth)

#7.check if a program is negative or positive
num=int(input("Enter a number:"))
if num > 0:
     print(num,"is positive")
elif num ==0:
     print(num,"is zero")
else:
     print(num,"is negative")

#8.trigonometry problem using math funtion
import math
print("sin(0):",math.sin(0))
print("cos(math.pi):",math.cos(math.pi))

#9.create a calculator
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
op=input("enter the operator [+,-,*,/]:")
if op == "+":
    print("ans is",n1+n2)
elif op == "-":
    print("ans is",n1-n2)
elif op == "*":
    print("ans is",n1*n2)
elif op == "/":
    print("ans is",n1/n2)
else:
    print("invalid choice")
    
    
