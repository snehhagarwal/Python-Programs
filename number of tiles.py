#Program that calculates the number of rectangular tiles required to cover a rectangular floor if
#the dimensions of the floor and the dimensions of a tile are entered by the user
lf=int(input("enter the length  of floor:"))
bf=int(input("enter the bradth of floor:"))
tl=int(input("enter the length of tile:"))
tb=int(input("enter the breadth of tile:"))
af=lf*bf
tf=tl*tb
a=af//tf
print("number of tiles required %d"%(a))
