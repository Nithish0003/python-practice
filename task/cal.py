a=float(input("Enter number1: "))
b=float(input("Enter number2: "))
opera=input("Enter the operation need to be performed: add,sub,mul,div,mod,floor: ").lower()
if opera=="add":
    print(a+b)
elif opera=="sub":
    print(a-b)
elif opera=="mul":
    print(a*b)
elif opera=="div":
    print(a/b)
elif opera=="mod":
    print(a%b)
elif opera=="floor":
    print(a//b)
else:
    print("invalid")