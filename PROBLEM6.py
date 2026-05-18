#SUM OF DIGITS OF A NUMBER

#USING WHILE LOOP METHOD

num=int(input("enter a number"))
num=abs(num)
sum=0
while num>0:
    rem=num%10
    sum+=rem
    num=num//10
print("sum of digits: ",sum)

#USING RECURSION METHOD

def prob(nums):
    nums=abs(nums)
    if nums==0:
        return 0
    return (nums%10) +prob(nums//10)
nums=int(input("enter a number"))
print("sum of digits:",prob(nums))
    
    