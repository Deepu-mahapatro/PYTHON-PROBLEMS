#HARSHAD NUMBER CHECK
#A NUMBER IS SAID TO BE HARSHAD NUMBER 
#IF IT DIVISIBLE BY SUM OF ITS DIGITS
#MEANS FOR 18-> 1+8 = 9 -> 18%9 = 2 
#HENCE THIS NUMBER IS DIVISIBLE 
#SO THIS NUMBER IS A HARSHAD NUMBER

#BASIC ALTERNATIVE APPROACH
def harsh_num(n):
    if n==0:
        return "INVALID NUMBER"
    original =n
    total=0
    while n>0:
        rem=n%10
        total+=rem
        n=n//10
    if original%total==0:
        return "HARSHAD NUMBER"
    return "NOT A HARSHAD NUMBER"
print(harsh_num(18))

#USING STRING CONVERSION METHOD
def harsh_num(n):
    original =n
    total=0
    for i in str(n):
        total+=int(i)
    if original%total==0:
        return "HARSHAD NUMBER"
    return "NOT A HARSHAD NUMBER"
print(harsh_num(18))

#USING RECURSIVE APPROACH
def total(n):
    if n==0:
        return 0
    return (n%10)+total(n//10)
def harsh_num(n):
    result=total(n)
    if n%result==0:
        return "HARSHAD NUMBER"
    return "NOT A HARSHAD NUMBER" 
print(harsh_num(18))   

#USING SUM AND LIST COMPREHENSION METHOD 
def harsh_num(n):
    total=sum([int(i)for i in str(n)])
    if n%total==0:
        return "HARSHAD NUMBER"
    return "NOT A HARSHAD NUMBER"
print(harsh_num(18))        