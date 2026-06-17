# AMICABLE NUMBERS PROBLEM
# APPROACH 1 (BRUTE FORCE METHOD)
# FIND SUM OF PROPER DIVISORS BY CHECKING FROM 1 TO N-1
# CHECK:
# sum_divisors(a) == b
# sum_divisors(b) == a
# a != b
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
# INTERVIEW VALUE: EASY TO UNDERSTAND
# APPROACH 2 (OPTIMIZED SQRT(N) METHOD)
# FIND DIVISORS IN PAIRS
# IF n % i == 0:
# DIVISORS ARE i AND n//i
# CHECK ONLY UP TO √n
# TIME COMPLEXITY: O(√n)
# SPACE COMPLEXITY: O(1)
# INTERVIEW VALUE: MOST RECOMMENDED
# APPROACH 3 (FUNCTION METHOD)
# CREATE divisor_sum() FUNCTION
# CREATE is_amicable() FUNCTION
# RETURN TRUE OR FALSE
# TIME COMPLEXITY: O(√n)
# SPACE COMPLEXITY: O(1)
# INTERVIEW VALUE: CLEAN AND REUSABLE
# APPROACH 4 (CLASS METHOD)
# CREATE CLASS AmicableChecker
# ADD divisor_sum() METHOD
# ADD is_amicable() METHOD
# TIME COMPLEXITY: O(√n)
# SPACE COMPLEXITY: O(1)
# INTERVIEW VALUE: OOPS PRACTICE
# APPROACH 5 (COMPETITIVE PROGRAMMING METHOD)
# TAKE INPUT USING:
# a, b = map(int, input().split())
# USE OPTIMIZED DIVISOR SUM LOGIC
# PRINT RESULT DIRECTLY
# TIME COMPLEXITY: O(√n)
# SPACE COMPLEXITY: O(1)
# INTERVIEW VALUE: CODING PLATFORMS
# FORMULA
# S(a) = b
# S(b) = a
# a != b
# WHERE S(n) = SUM OF PROPER DIVISORS OF n
# EDGE CASES
# 220, 284 → AMICABLE
# 1184, 1210 → AMICABLE
# 2620, 2924 → AMICABLE
# 10, 20 → NOT AMICABLE
# 6, 6 → NOT AMICABLE (PERFECT NUMBER)
# 1, 1 → NOT AMICABLE
# NEGATIVE NUMBERS → NOT AMICABLE
# 0, 0 → NOT AMICABLE
# IMPORTANT POINT
# PROPER DIVISORS EXCLUDE THE NUMBER ITSELF
# EXAMPLE
# 220 → SUM OF PROPER DIVISORS = 284
# 284 → SUM OF PROPER DIVISORS = 220
# THEREFORE (220, 284) IS AN AMICABLE PAIR
# CONCLUSION
# BEST APPROACH: OPTIMIZED SQRT(N) METHOD
# BEST TIME COMPLEXITY: O(√n)
# BEST SPACE COMPLEXITY: O(1)
# MOST ASKED IN INTERVIEWS

#BRUTE FORCE METHOD
def divisor_sum(n):
    #EDGE CASE 
    if n<=1:
        return 0
    total=0
#PROPER DIVISORS ARE FROM 1 TO N-1
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total
def is_amicable(a,b):
    return (
        divisor_sum(a)==b and divisor_sum(b)==a and a!=b
    )
a=220
b=284
if is_amicable(a,b):
    print("AMICABLE NUMBERS")
else:
    print("NOT A AMICABLE NUMBERS")
    

#USING OPTIMIZED METHOD
def divisor_sum(n):
    #EDGE CASE
    if n<=1:
        return 0
    total=1
    i=2
    while i*i<=n:
        if n%i==0:
            total+=i
            #AVOID DUPLICATES FOR PERFECT SQUARES
            if i!=n//i:
                total+=n//i
        i+=1
    return total
def is_amicable(a,b):
    if a<=0 or b<=0:
        return False
    return (
        divisor_sum(a)==b and divisor_sum(b)==a and a!=b
    )
a=220
b=284
print(is_amicable(a,b))

#BEST APPROACH
def divisor_sum(n):
    if n<=1:
        return 0
    total=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            total+=i
            if i!=n//i:
                total+=n//i
    return total
def is_amicable(a,b):
    return (divisor_sum(a)==b and divisor_sum(b)==a and a!=b)
a,b=map(int,input().split())
print("AMICABLE " if is_amicable(a,b) else "NOT A AMICABLE")

