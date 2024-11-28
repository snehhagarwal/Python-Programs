#Program to input the centre of a circle, radius of the circle and an arbitrary point P(x,y) and
#to determine whether the point is inside the circle, on the circle or outside the circle.
import math
cx=int(input("centre point of the circle:"))
cy=int(input("centre point of the circle:"))
r=int(input("radius of the circle:"))
x=int(input("enter the point:"))
y=int(input("enter the point"))
e=pow((x-cx),2)+pow((y-cy),2)
d=math.sqrt(e)
if (d>r):
    print("outside the circle")
elif (d==r):
    print("on the circle")
else:
    print("inside the circle")
