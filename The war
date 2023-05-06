'''In War, The Enemy have placed their mines on the ground which can be considered as a grid of size NxM. N denotes Row and M is Column . Each cell(i,j) has a mine in it if (i+j) is divisible by 2 otherwise all the other cells are empty. i and j both are the rows and columns index.

Write the program to find out the number of empty cells where mines wan't blow if grid (matrix dimension ) size is given by user'''

size=input()
a=0
x,y=map(int,size.split('x'))
for i in range(int(x)):
    for j in range(int(y)):
        if (i+j)%2!=0:
            a+=1
print(a)
