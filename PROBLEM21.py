#PRIME FACTORS OF A NUMBER
#THE PRIME NUMBERS WHICH ARE MULTIPLY TOGETHER TO FORM A ORIGINAL NUMBER
#TAKE THE NUMBER AND CHECK IT DIVISIBLE BY SMALLEST PRIME NUMBER
#PRIME NUMBER ARE DIVISIBLE BY 1 AND ITSELF
#PROCESS:
        #TAKE THE SMALLEST PRIME NUMBER
        #CHECKS IT IT DIVIDES THE NUMBER COMPLETELY
        #IF YES,DIVIDE IT 
        #CONTINUE DIVIDING UNTIL NO LONGER DIVIDES
        #MOVE TO NEXT PRIME NUMBER
        #STOP WHEN THE REMAINING NUMBER BECOMES PRIME NUMBER

#USING NORMAL METHOD
def prime_factors(n):
    factors=[]
    divisor=2
    while n>1:
        while n%divisor==0:
            factors.append(divisor)
            n=n//divisor
        divisor+=1
    return factors
print(prime_factors(60))

#USING SQUARE ROOT METHOD
def prime_factors(n):
    factors=[]
    divisor=2
    while divisor*divisor<=n:
        while n%divisor==0:
            factors.append(divisor)
            n=n//divisor
        divisor+=1
    #REMAINING PRIME NUMBERS
    if n>1:
        factors.append(n)
    return factors
print(prime_factors(60))

#USING RECURSIVE METHOD
def prime_factors(n,divisor=2):
    if n==1:
        return
    if n%divisor==0:
        print(divisor)
        prime_factors(n//divisor,divisor)
    else:
        prime_factors(n,divisor+1)
prime_factors(60)

#USING EVEN ODD METHOD
def prime_factors(n):
    factors=[]
    #REMOVE ALL 2S
    while n%2==0:
        factors.append(2)
        n=n//2
    #CHECK ONLY ODD NUMBERS
    divisor=3
    while divisor*divisor<=n:
        while n%divisor==0:
            factors.append(divisor)
            n=n//divisor
        divisor+=2
    #REMAINING PRIME
    if n>1:
        factors.append(n)
    return factors
print(prime_factors(60))