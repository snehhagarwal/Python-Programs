#if a number is divisible by 3 print tipsy.
#if a number is divisible by 7 print topsy.
#if a number is divisible by both 3 and 7 print tipsytopsy.
n=int(input("the number is:"))
if n>20:
   if n%3==0 and n%7==0:
       print("tipsytopsy")
   elif n%3==0:
       print("tipsy")
   elif n%7==0:
       print("topsy")
else:
    print("number is less than 20")
