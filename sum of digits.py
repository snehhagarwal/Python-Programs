#Program to find the sum of digits of an entered number.
n=int(input("enter the number:"))
s=0
while(n!=0):
    r=n%10
    n=n/10
    s+=r
print("sum of digits is %d"%(s))
