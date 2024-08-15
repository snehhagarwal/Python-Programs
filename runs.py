#Program to input the number of overs in a Cricket match and output the maximum runs a
#player can score in the match. Assume that there are no extra runs or NO balls in the match
#played. For example, in a 50 over match, the maximum runs scored are 1653
o=int(input("enter the number of overs:"))
mr=33*(o-1)+36
print("maximum runs a player can score are %d"%(mr))
