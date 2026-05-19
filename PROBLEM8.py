#FACTORIAL OF A NUMBER

#USING LOOP METHOD
def factorial(n):
    # Edge case for negative numbers
    if n < 0:
        return "Factorial does not exist for negative numbers"
    # Factorial of 0 is 1
    if n == 0:
        return 1
    fact = 1
    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))


#USING RECURSION METHOD
def factorial(n):
    if n<0:
        return "FACTORIAL DOES NOT EXIST"
    #Base case
    if n==0 or n==1:
        return 1
    #recursive call
    return n*factorial(n-1)
print(factorial(5))

#USING BUILT IN FUNCTION 
import math
print(math.factorial(5))

#USING REDUCE() METHOD
from functools import reduce 
def factorial(n):
    if n<0:
        return "INVALID NUMBER"
    if n==0:
        return 1 
    return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(5))