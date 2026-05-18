#PALINDROME NUMBER

#FOR INTEGER
num=int(input("enter a number:  "))
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
    

#FOR STRING
str=input("enter  string:  ")
result=str[::-1]
if str==result:
    print("palindrome")
else:
    print("not a palindrome")