a=int(input("enter a num"))

match a:
    case 222:
        print("value is 222")
    case 333:
        print("value is 333")       
    case 444:
        print("value is 444")   
    case _:
        print("value is not in 222,333,444")