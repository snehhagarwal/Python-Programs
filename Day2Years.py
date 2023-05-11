'''Write a program to convert specified days into years, weeks and days.

Note: Ignore leap year.

Test Data :
Number of days : 1329
Expected Output :
Years: 3
Weeks: 33
Days: 3 '''
d=int(input())
y=d//365
w=(d-y*365)//7
da=d-y*365-w*7
print(y,w,da,sep='\n')
