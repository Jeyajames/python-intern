#3.raise a name error
try:
    print(ans)
except NameError:
    print("name error caugh")
else:
    print("success")

#5.getting input inside the try
try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    print(a/b)
except ZeroDivisionError as e:
    print("zero error caugh",e)
    
