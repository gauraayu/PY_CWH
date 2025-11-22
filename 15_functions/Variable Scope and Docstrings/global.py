def sum (a,b):
    print("hey i am sum function")
    global z #plz modify global variable
    z=0 # global variable
    return a+b
z=8 # global variable
print(sum(5,7))  # Output: 12
print(z)