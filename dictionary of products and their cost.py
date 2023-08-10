d={}
while True:
    p=input("enter the product name or s to stop:")
    if p =="S" or p=="s":
        break
    else:
        v=int(input("enter the value:"))
        d[p]=v
print(d)
while True:
    i=input("enter the product name or s to stop:")
    if i =="S" or i=="s":
        break
    else:
      if i not in d:
          print("not present")
      else:
          print(d[i])
