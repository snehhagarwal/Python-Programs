l1=eval(input("enter a list:"))
l2=eval(input("enter a second list:"))
l=[]
for i in range(len(l1)):
    x=l1[i]+l2[i]
    l=l+[x]
print(l)
