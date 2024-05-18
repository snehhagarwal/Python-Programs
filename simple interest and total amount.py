p=int(input("enter the principal amt:"))
r=int(input("enter the rate :"))
t=int(input("enter the time:"))
si=(p*r*t)/100
totalamt=p+si
print("the simple interest is %d and total amount is %d"%(si,totalamt))
