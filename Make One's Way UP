''' Write a complete program that takes an array A of an integer as input and displays True if the absolute difference between each adjacent pair of elements strictly increases otherwise False.'''
# mport numpy as np
n=int(input())
l=list(map(int,input().split()))
# arr=np.array(l)
l1=[]
for i in range(len(l)-1):
    if l[i]>=l[i+1]:
        l1.append(l[i]-l[i+1])
    else:
        l1.append(l[i+1]-l[i])
for i in l1:
    if l1.count(i)>=2:
        print("False")
        break
else:
    print("True")
