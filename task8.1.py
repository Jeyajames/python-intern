loop = 1
op = 0
while loop == 1:
    print("welcom calculator")
    print("options:")
    print("")
    print("1:addtion")
    print("2:subtraction")
    print("3:multiplication")
    print("4:division")
    print("5:quit")
    print("")
    op =int(input("select option:"))
    try:
        if op == 1:
            n1=int(input("a:"))
            n2=int(input("b:"))
            print("addition:",n1 + n2)
        elif op == 2:
           n1=int(input("a:"))
           n2=int(input("b:"))
           print("subtraction:",n1 - n2)
        elif op == 3:
           n1=int(input("a:"))
           n2=int(input("b:"))
           print("multiplication:",n1 * n2)
        elif op == 4:
            n1=int(input("a:"))
            n2=int(input("b:"))
            if n2 == 0:
               print("error")
            else:
               print("division:",n1 / n2)
        elif op == 5:
          loop = 0
        else:
           print("%d is not valid input.please enter correct option")

    except Exception:
          print("not valid")
