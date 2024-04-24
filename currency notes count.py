amt=int(input("enter the withdrawn money:"))
l=[2000,500,100]
for i in l:
    c=amt//i
    print("we require %d notes of %d"%(c,i))
    amt=amt%i
    
    
