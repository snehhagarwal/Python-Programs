a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start, end = 2, 6
while start < end:
  
    a[start], a[end] = a[end], a[start]
    
    start += 1
    
    end -= 1

print(a)
