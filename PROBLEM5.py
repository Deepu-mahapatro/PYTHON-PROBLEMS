#PALINDROME NUMBER

#FOR INTEGER
num=int(input("enter a number:  "))
num=abs(num)
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
    

#USING STRING METHOD
text=int(input("enter  string:  "))
text=str(text)
result=text[::-1]
if text==result:
    print("palindrome")
else:
    print("not a palindrome")
    
#RECURSION METHOD
def prob(num,reverse=0,original=None):
    if original is None:
        original=num
    if num==0:
        return original==reverse
    rem=num%10
    reverse=reverse*10+rem
    return prob(num//10,reverse,original)
num=int(input("enter a number"))
if prob(abs(num)):
    print("palindrome")
else:
    print("not a palindrome")
    

#UsiNG RECURSION ANOTHER FORMAT
def prob(num, reverse=0):

    num = abs(num)
    original=num
    if num == 0:
        return reverse
    rem = num % 10
    reverse = reverse * 10 + rem
    return prob(num // 10, reverse)
num = int(input("Enter a number: "))
if original == prob(num):
    print("palindrome")
else:
    print("not palindrome")
    
