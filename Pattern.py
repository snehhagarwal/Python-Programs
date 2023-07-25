for row in range(5):
    for column in range(3):
        if row-column==0 or (row-column==1 and row!=3) or row+column==4 or column==0:
            print("*",end='')
    print()
