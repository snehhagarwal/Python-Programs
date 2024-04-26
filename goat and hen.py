#Program to input the number of heads and feet in a farm and identify the number of chickens
#and goats in the farm. For example, if there are 340 heads and 1,060 feet, there are 150
#chickens and 190 goats.
h=int(input("enter the no. of heads"))
f=int(input("enter the number of feets:"))
r=(f-2*h)//2
c=h-r
print("the number of chicken are %d and number of goats %d"%(c,r))
