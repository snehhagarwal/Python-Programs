#Program to find the maximum of the three entered numbers.
a=int(input("enter the 1st no:"))
b=int(input("enter the 2nd no:"))
c=int(input("enter the 3rd no:"))
if (a>b and a>c):
    print(a)
elif (b>a and b>c):
    print(b)
else:
    print(c)

