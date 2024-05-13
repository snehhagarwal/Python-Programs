''' Write the program to create building structure like the burj khaleefa with equivalent binary numbers '''
#Code->
num = int(input())
w = len(bin(num)) - 2
for i in range(num+1):
    d = bin(i)[2:]
    print(d.rjust(w))
