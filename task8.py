#1.types of error
print("1.Zerodivisionerror")
try:
    print(36/0)
except ZeroDivisionError:
    print("unable to divided by zero")
print("2.key error")
a={1:'z',2:'y',3:'x'}
try:
    print(a[6])
except KeyError:
    print("key not found")
print("3.value error")
try:
    k=int(input("enter the number:"))
    print(k)
except ValueError:
    print("value error caught")
print("NEWS.txtindex error")
b=[1,3,8]
try:
    print(b[8])
except IndexError:
    print("index not found")
print("5.over flow error")
try:
    import math
    print(math.exp(100))
except OverflowError:
    print("over flow error caught")
    
print("6.moduler not found error")
try:
    import module
except ModuleNotFoundError:
    print("module not found")
print("7.indentation error")
try:
    def fun():
        prin("python internship")
except IndentationError:
    print("indentation error caught")
    
