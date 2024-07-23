#Program to find the factorial of an entered number.
n=int(input("enter the number:"))
s=1
for i in range(1,n+1):
    s=s*i
print("the factorial of the number %d is %d"%(n,s))
