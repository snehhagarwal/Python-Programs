''' We have three colors: red, green, and blue in a list. 
Replace the two different colors pair with third color in every dutye cycle of transformation. 

Given N colors are in a line, determine the last remaining color after any possible sequence of such transformations.

For example, given the list is ['R', 'G', 'B', 'R'] 
and the following steps we need to take in transformation.'''
l=eval(input())
i=0
ln=len(l)
f=0
while(i<=ln):
    f=0
    if l.count(l[0])==len(l):
        break
    if (l[i]=='G' and l[i+1]=='B') or (l[i]=='B' and l[i+1]=='G'):
        l[i]='R'
        f=1
    elif (l[i]=='G' and l[i+1]=='R') or (l[i]=='R' and l[i+1]=='G'):
        l[i]='B'
        f=1
    elif (l[i]=='R' and l[i+1]=='B') or (l[i]=='B' and l[i+1]=='R'):
        l[i]='G'
        f=1
    if f==1:
        l.pop(i+1)
        ln=ln-1
        i=0
        
    if f==0:
        i+=1
        
    if ln==1:
        break;
print(end='"')
print(end=l[0])
print(end='"')
