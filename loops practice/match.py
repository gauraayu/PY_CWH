a=int(input("enter a num 1"))
b=int(input("enter a num 2"))
c=input("enter opeararor (+,-,*,/)")
match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)          
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("invalid operator")
