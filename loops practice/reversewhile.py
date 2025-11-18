num=78999
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num/10
print("the reversed number is:",rev)