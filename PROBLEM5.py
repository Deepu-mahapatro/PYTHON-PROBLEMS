#PALINDROME NUMBER

num=int(input("enter a number"))
original=num
sum=0
while num>0:
    rem=num%10
    sum=sum*10+rem
    num=num//10
if sum==original:
    print("palindrome")
else:
    print("not a palindrome")