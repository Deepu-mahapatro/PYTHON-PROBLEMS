#REVERSE A NUMBER

nums=int(input("enter a number"))
reverse=0
while nums>0:
    rem=nums%10
    reverse=reverse*10+rem
    nums=nums//10
print("reverse of a number:",reverse)