def cal():
    a=float(input("Enter number1: "))
    b=float(input("Enter number2: "))
    opera=input("Enter the operation need to be performed: add,sub,mul,div,mod,floor: ").lower()
    if opera=="add":
        c=a+b
    elif opera=="sub":
        c=a-b
    elif opera=="mul":
        c=a*b
    elif opera=="div":
        c=a/b
    elif opera=="mod":
        c=a%b
    elif opera=="floor":
        c=a//b
    else:
        c="invalid"
    return c