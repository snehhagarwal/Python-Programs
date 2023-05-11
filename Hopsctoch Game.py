'''Write a program for given an integer list where each number represents the number of hops you can make in hopscotch game, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False. '''
l=list(map(int,input().split()))
hope=0
for i in range(len(l)):
    if hope<i:
        print("False")
        break
    hope=max(hope,i+l[i])
else:
        print("True")
