#SPY NUMBER 
#SUM OF DIGITS=PRODUCT OF DIGITS
#TAKE A NUMBER AND SEPARATE THE DIGITS
#AND FIND THE SUM OF DIGITS
#NOW FIND THE PRODUCT OF DIGITS
#IF SUM OF DIGITS=PRODUCT OF DIGITS
#IT IS S SPY NUMBER

#USING BASIC MATHEMATICAL METHOD
num=int(input("enter a number"))
temp=num
sum=0
product=1
while temp>0:
    rem=temp%10
    sum+=rem
    product*=rem
    temp//=10
if sum==product:
    print("spy number")
else:
    print("non spy number")
    
#USING STRING CONVERSION
num=int(input("enter a number"))
sum=0
product=1
for i in str(num):
    sum+=int(i)
    product*=int(i)
if sum==product:
    print("SPY NUMBER")
else:
    print("NOTA  SPY NUMBER")
    
#BEST VERSION
def is_spy(num):
    if num<0:
        return False
    if num==0:
        return False
    total=0
    product=1
    while num>0:
        rem=num%10
        total+=rem
        product*=rem
        num//=10
    return total==product
num=int(input("enter a number"))
if is_spy(num):
    print("SPY NUMBER")
else:
    print("NON SPY NUMBER")