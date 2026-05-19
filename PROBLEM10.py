#STRONG NUMBER TO CHECK

#USING WHILE LOOP METHOD 
def strong_number(n):
    if n<0:
        return "negative are not strong"
    original=n
    total=0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact=fact*i
        total=total+fact
        n=n//10
    if total==original:
        return "STRONG NUMBER"
    else:
        return "NOT A STRONG NUMBER"
print(strong_number(145))

#USING FUNCTION FOR FACTORIAL
def factorial(n):
    if n<0:
        return "invalid input"
    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
    return fact
#LOGIC FOR STRONG NUMBER
def strong_number(n):
    if n<0:
        return "invalid number"
    original=n
    total=0
    while n>0:
        digit=n%10
        total+=factorial(digit)
        n=n//10
    if total==original:
        return "STRONG NUMBER"
    else:
        return "NOT A STRONG NUMBER"
print(strong_number(145))

#USING MATH FUNCTION (BEST METHOD)
import math 
def strong_number(n):
    if n<0:
        return "invalid input"
    original=n
    total=0
    while n>0:
        rem=n%10
        total+=math.factorial(rem)
        n=n//10
    if total==original:
        return "STRONG NUMBER"
    else:
        return"NOT A STRONG NUMBER"
print(strong_number(145))

#USING RECURSION METHOD()
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
#LOGIC FOR STRONG NUMBER
def strong_number(n):
    if n < 0:
        return "Invalid"
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += factorial(digit)
        n = n // 10
    if total == original:
        return "STRONG NUMBER"
    return "Not STRONG NUMBER"
print(strong_number(145))