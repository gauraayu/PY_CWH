def sum(a,b):
    c=a+b
    z=10 # local variable
    print(z)
    return c

z=8 # global variable
print(z)
print(sum(5,7))  # Output: 12

# a and  b are loacal variables
