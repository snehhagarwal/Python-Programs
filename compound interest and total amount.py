import math
p=int(input("enter the principal amt:"))
r=int(input("enter the rate:"))
t=int(input("enter the time:"))
e=pow(1+(r/100),t)
y=p*e
ci=y-p
ta=p+ci
print("the compund interest is %d and total amount is %d"%(ci,ta))
