#Big Bazaar specifies its customers into three categories as Bronze, Silver and Gold. If the
#shopping amount is greater than 25000, the category is GOLD. If the shopping amount is
#between 10000 and 25000, the category is SILVER, otherwise the category is BRONZE. The
#discount offered for GOLD customers is 20% of the shopping amount, for SILVER customers is
#10% of the shopping amount and 5% otherwise. Design a program in python that asks the user
#to input the total shopping amount, outputs the category and amount to be paid.
amt=int(input("enter the shopping amount:"))
if (amt>25000):
    print("GOLD")
    print(amt-(20/100)*amt)
elif (10000<amt<25000):
    print("SILVER")
    print(amt-(10/100)*amt)
else:
    print("BRONZE")
    print(amt-(5/100)*amt)
    
