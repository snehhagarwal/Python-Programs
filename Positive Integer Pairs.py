#Code
''' Write a program for the given integers P and X, that display the positive integer pairs (i, j) with satisfy the following conditions.

i + j == P
i XOR j == X '''
P = int(input())
X = int(input())

for i in range(P//2+1):
    j = P - i
    if i ^ j == X:
        print(i, j)
