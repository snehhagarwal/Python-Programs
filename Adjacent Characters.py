'''Given a string and we have to swap its adjacent characters(pairs).
Here, to swap adjacent characters of a given string - we have a condition, which is "string length must be EVEN i.e. string must contains even number of characters".'''
#Code-->

st=input()
re=''
if len(st)%2==1:
    print('Odd length.')
else: 
    for i in range(0,len(st),2):
        re+=st[i+1] +st[i]
    print(re)
