import math
a=int(input("enter the 1st side:"))
b=int(input("enter the 2nd side:"))
c=int(input("enter the 3rd side:"))
if ( a+b>c or b+c>a or a+c>b):
    print("valid triangle")
    if(a==b or b==c or a==c):
            print("isoceles")
    if ((a*a)+(b*b)==(c*c) or (b*b)+(c*c)==(a*a) or (a*a)+(c*c)==(b*b)):
            print("right angled")
    if (a!=b!=c):
           print("scalene")
else:
    print("invalid")
    
    
