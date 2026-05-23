#LEAST COMMON MULTIPLE(LCM) OF TWO NUMBERS
#THE SMALLEST NUMBER THAT BOTH NUMBERS CAN DIVIDE PERFECTLY
#FOR EX:LCM(4,6)
#MULTIPLES OF 4=4,8,12,16
#MULTIPLES OF 6=6,12,18
#AMONG BOTH TEH LEAST COMMON MULTIPLE THAT DIVIDES BOTH
#THE NUMBERS IF 12 HENCE LCM(4,6)->12
#LCM MAY BE GREATER THAN OR EQUAL TO NUMBERS
#RELATION BETWEEN LCM AND GCD
#GCD(A,B)*LCM(A,B)=A*B
#FOR EX: GCD(4,6)->2 AND LCM(4,6)->12
#HENCE A*B=2*12->24 AND FOR CO-PRIMES LCM=1
#FOR LCM(A,A)->A,LCM(1,A)->A,LCM(0,A)->0
#FOR PRIME NUMBERS LCM(A,B)->A*B
#LCM FOR EXACTLY DIVIDES LCM(4,20)->20
#LCM CAN NEVER BE SMALLER THAN (A,B) GIVEN NUMBERS

#BRUTE FORCE METHOD
def lcm_numbers(a,b):
    a=abs(a)
    b=abs(b)
    if a==0 or b==0:
        return 0
    #FIND MAX VALUE BECAUSE LCM CAN NEVER BE SMALLER TEH (A,B)
    largest=max(a,b)
    #LOOP RUNS UNLIMITED TIMES BECAUSE WE DON'T KNOW WHERE THE LCM WAS
    while True:
        if largest%a==0 and largest%b==0:
            return largest
        largest+=1
print(lcm_numbers(4,6))

#MULTIPLE JUMP METHOD
def lcm_numbers(a,b):
    a=abs(a)
    b=abs(b)
    if a==0 or b==0:
        return 0
    largest=max(a,b)
    lcm=largest
    while True:
        if lcm%a==0 and lcm%b==0:
            return lcm
        lcm+=largest
print(lcm_numbers(4,6))

#USING FORMULA
#LCM(A,B)=A*B/GCD(A,B)
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm_numbers(a,b):
    a=abs(a)
    b=abs(b)
    if a==0 or b==0:
        return 0
    return (a*b)/gcd(a,b)
print(lcm_numbers(4,6))

#USING BUILT IN PYTHON FUNCTION
import math
def lcm_numbers(a,b):
    return math.lcm(a,b)
print(lcm_numbers(4,6))

#USING RECURSIVE LCM + GCD METHOD
def gcd_recursive(a,b):
    if b==0:
        return a
    return gcd_recursive(b,a%b)
def lcm_recursive(a,b):
    a=abs(a)
    b=abs(b)
    if a==0 or b==0:
        return 0
    return (a*b)//gcd_recursive(a,b)
print(lcm_recursive(4,6))