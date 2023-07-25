for r in range(5):
    for c in range(5):
        if r+c==2 or (r+c==4 and r!=0 and r!=4) or r+c==6:
            print("*",end='')
        else:
            print(end=" ")
    print()    
