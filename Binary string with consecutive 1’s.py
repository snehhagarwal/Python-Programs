'''Write a program where user enter the integer number n and generate the binary number reprsentation of n digits width. Your task is to count those binary reprsentation's out of all the generated ones in which binary number string has consecutive 1's.'''
w=int(input())
count=0
for i in range(2**w):
    if '11' in  bin(i):
        count+=1
print(count)
