#REVERSE A NUMBER

nums=int(input("enter a number"))
sign=-1 if nums<0 else 1
nums=abs(nums)
reverse=0
while nums>0:
    rem=nums%10
    reverse=reverse*10+rem
    nums=nums//10
print("reverse of a number:",reverse*sign)

#USING STRING SLICING
num=int(input("enter a number"))
sign=-1 if num<0 else 1
reverse=int(str(abs(num))[::-1])
print("reversed number :",reverse*sign)

#USING RECURSION METHOD
def prob(num,reverse=0):
    if num==0:
        return reverse
    rem=num%10
    reverse=reverse*10+rem
    return prob(num//10,reverse)
num=int(input("enter a number"))
sign=-1 if num<0 else 1
result=prob(abs(num))
print("reversed number:",result*sign)