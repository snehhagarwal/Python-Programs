#Program to find the series of all three digits Armstrong numbers
import math
for i in range(100,1000):
    s=0
    k=i
    l=len(str(i))
    while(i!=0):
         r=i%10
         i=i//10
         s=s+pow(r,l)
    if k==s:
        print(s)
        
