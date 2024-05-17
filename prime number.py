#Program to find whether an entered number is prime or not.
n=int(input("enter the number:"))
s=0
for i in range(1,n+1):
    if (n%i==0):
        s+=1
if (s==2):
    print("prime")
else:
    print("not prime")
