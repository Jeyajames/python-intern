# addition of two number is+ value
# subtraction of two number is +value
# division of two number is +value
# multiplication of two number is +value
def arth(x,y):
    return x+y,x-y,x/y,x*y
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=arth(a,b)
print("addition subtraction division and multiplication",a,"and",b,"is",c)

# create a function covid() and it should accept patient name,and body temprature by default the body temprature should be 98 degree
def covid(name,temp='98'):
    print(name,'temprature is',temp)
covid('janu')
covid('ramya')
