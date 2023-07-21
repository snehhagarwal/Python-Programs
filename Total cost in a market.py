#calculate the total cost in a market based on the number of items.
#If items are more than 100 then each item is of 70rs,
#if items are less than 100 greater than 10 then each item 100rs,
# if items are less than 10 then each item is of 120 rs
n=int(input("no. of items:"))
if n<10:
     print("the total cost is:",n*120)
elif n>10 and n<100:
    print("the total cost is",n*100)
elif n>100 :
    print("the total cost is :",n*70)
