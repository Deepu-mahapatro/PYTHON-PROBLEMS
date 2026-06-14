#POWER OF A NUMBER(RECURSION)
#CORE IDEA:
#CALCULATE BASE RAISED TO EXPONENT
#USE RECURSION
#EDGE CASES:
#EXP<0
#EXP=0
#EXP=1
#BASE=0
#BASE=1
#BASE=0 AND EXP<0
#LARGE EXPONENT
#KEY OBSERVATION:
#BASE^EXP=BASE*BASE^(EXP-1)
#RECURSION CONTINUES UNTIL EXP=0
#NEGATIVE EXPONENT
#BASE^-N=1/(BASE^N)
#EXAMPLE:
#2^4
#2*2*2*2
#OUTPUT=16
#APPROACH 1(STANDARD RECURSION):
#CHECK NEGATIVE EXPONENT
#BASE CASE EXP==0
#RETURN BASE*POWER(BASE,EXP-1)
#APPROACH 2(DIVIDE AND CONQUER):
#FIND HALF POWER
#SQUARE THE RESULT
#IF ODD MULTIPLY BY BASE
#APPROACH 3(NEGATIVE EXPONENT SUPPORT):
#CONVERT NEGATIVE EXPONENT TO POSITIVE
#RETURN 1/POWER(BASE,-EXP)
#HANDLE UNDEFINED CASE
#BASE=0 AND EXP<0
#TIME COMPLEXITY:
#STANDARD RECURSION->O(N)
#DIVIDE AND CONQUER->O(LOGN)
#NEGATIVE EXPONENT VERSION->O(N)
#SPACE COMPLEXITY:
#STANDARD RECURSION->O(N)
#DIVIDE AND CONQUER->O(LOGN)
#NEGATIVE EXPONENT VERSION->O(N)
#CONCLUSION:
#BETTER SOLUTION
#STANDARD RECURSION
#OPTIMAL SOLUTION
#DIVIDE AND CONQUER
#ADVANCED SOLUTION
#NEGATIVE EXPONENT SUPPORT
#MOST INTERVIEWERS EXPECT
#STANDARD RECURSION
#TOP INTERVIEW ANSWER
#DIVIDE AND CONQUER(BINARY EXPONENTIATION)

#POWER OF A NUMBER
def power(base,exp):
    #EDGE CASE
    if exp<0:
        return " NEGATIVE EXPONENTIAL ARE NOT ALLOWED"
    #BASE CASE
    if exp==0:
        return 1
    #RECURSIVE CASE
    return base*power(base,exp-1)
base=int(input("enter base number"))
exp=int(input("enter exponential"))
print(power(base,exp))

# DIVIDE AND CONQUER METHOD
def power(base, exp):
    # BASE CASE
    if exp == 0:
        return 1
    half = power(base, exp // 2)
    # EVEN POWER
    if exp % 2 == 0:
        return half * half
    # ODD POWER
    return base * half * half
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print(power(base, exp))

# POWER OF A NUMBER USING RECURSION
def power(base, exp):
    # EDGE CASE
    if base == 0 and exp < 0:
        return "Undefined"
    # NEGATIVE EXPONENT
    if exp < 0:
        return 1 / power(base, -exp)
    # BASE CASE
    if exp == 0:
        return 1
    # RECURSIVE CASE
    return base * power(base, exp - 1)
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print(power(base, exp))