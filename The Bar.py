''' At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.'''
def intersection(l1,l2):
    flag =False
    for i in l2:
        if i in l1:
            flag = True
            break
    return flag

s = input() #input section starts
s1 = s
k =''
while(k!='}'):
    k = input()
    s1+=k
dic =eval(s1) #input section ends

l =[]
p =0
for i,j in dic.items():
    #print(j,sep ="\t")
    if intersection(l,j) == False:
        p+=1
        l.extend(j)
    else:
        continue
    #print(l)
print(p)
