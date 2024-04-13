''' Exceptions
Errors detected during execution are called exceptions.

#Handling Exceptions
'''The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.'''

#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
    
Output

Error Code: integer division or modulo by zero    
Task

You are given two values a and b. Perform integer division and print a/b.'''
i=int(input())
for p in range(i):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except(ZeroDivisionError,ValueError) as e:
        print("Error Code:",e)
