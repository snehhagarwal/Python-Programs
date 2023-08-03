n=int(input("the number is:"))
d=0
r=n%10
d=d*10+r
n=n//10
r=n%10
d=d*10+r
n=n//10
print("the reversed no is:",d)
