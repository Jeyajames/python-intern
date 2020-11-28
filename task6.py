#1.program to loop through a list of number
z=[4,3,2,6]
for i in z:
    print(i,i+2) #add +2 value for each element
    
#2.write a program
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print("\n")

#3.print the fibonacci sequence
def fib(n):
    a=0
    b=1
    if n == 1:
        print(n)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(5)

#4.armstrong number
x=int(input("Enter the number:"))
sum=0
temp=x
while temp>0:
    digit=temp%10
    sum +=digit **3
    temp //=10
if sum==x:
    print(x,"is armstrong number")
else:
    print(x,"is not armstrong")
