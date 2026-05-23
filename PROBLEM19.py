#GREATEST COMMON DIVISOR (GCD) OF TWO NUMBERS
#ALSO CALLED AS HIGHEST COMMON FACTOR
#ALSO CALLED AS GREATEST COMMON FACTOR
#FOR EX: 12->1,2,3,4,6,12
#FOR EX: 18->1,2,3,6,9,18
#AMONG THIS TEH COMMON FACTORS ARE 1,2,3,6
#NOW FORM THIS FACTORS TEH LARGEST FACTOR 
#HENCE 6 IS CALLED AS LARGEST COMMON FACTOR
#GCD MEANS TEH LARGEST COMMON NUMBER THAT DIVIDES BOTH THE NUMBER PERFECTLY
#IF GCD IS 1 THEN IT IS CALLED: CO-PRIME NUMBERS
#GCD(A,A)->A,GCD(0,A)->A,GCD(0,0)->0
#FOR EXACT DIVISION GCD(5,20)-> GCD=SMALL NUMBER=5
#FOR PRIME NUMBERS GCD=1

#BRUTE FORCE APPROACH
def gcd_number(a,b):
    a=abs(a)
    b=abs(b)
    if a==0:
        return b
    if b==0:
        return a
    #THE COMMON NUMBER THAT DIVIDES EVERY NUMBER IS 1
    gcd=1
    #THE LOOPS ENDS AT SMALLEST NUMBER (12,18)->12 IS SMALL 
    #SO 1,2,3,4,5,6,7,8,9,10,11,12 ARE TEH NUMBERS OF I   
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd   #GIVES THE LATEST UPDATE GCD VALUE WHICH IS COMMON
print(gcd_number(12,18))

#USING REVERSE LOOP METHOD
def gcd_numbers(a,b):
    a=abs(a)
    b=abs(b)
    if a==0:
        return b
    if b==0:
        return b
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
print(gcd_numbers(12,18))

#EUCLIDEAN ALGORITHM
def gcd_numbers(a,b):
    a=abs(a)
    b=abs(b)
    while b!=0:
        a,b=b,a%b
    return a
print(gcd_numbers(12,18))

#RECURSIVE ECULIDEAN METHOD
def gcd_numbers(a,b):
    a=abs(a)
    b=abs(b)
    if b==0:
        return a
    return gcd_numbers(b,a%b)
print(gcd_numbers(12,18))