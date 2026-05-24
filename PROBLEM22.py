#TWIN PRIME NUMBERS UPTO N
#A PRIME NUMBER IS A NUMBER IF :
# IT HAS EXACTLY TWO FACTORS
#ONLY DIVISIBLE BY 1 AND ITSELF
# A TWIN PRIME NUMBER IS CALLED AS :
#TEH DIFFERENCE BETWEEN TWO PRIME NUMBERS IS 2
#(SECOND PRIME)-(FIRST PRIME)=2

#USING BRUTE FORCE APPROACH
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def twin_prime(num):
    result=[]
    for i in range(2,num-1):
        if is_prime and is_prime(i+2):
            result.append((i,i+2))
    return result
print(twin_prime(20))

#USING SQUARE ROOT METHOD
def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True
def twin_primes(n):
    result = []
    for i in range(2, n - 1):
        if is_prime(i) and is_prime(i + 2):
            result.append((i, i + 2))
    return result
print(twin_primes(20))

#USING RECURSION METHOD
def is_prime(num, divisor=2):
    # EDGE CASE
    if num < 2:
        return False
    # BASE CONDITION
    if divisor * divisor > num:
        return True
    # NOT PRIME
    if num % divisor == 0:
        return False
    # RECURSIVE CALL
    return is_prime(num, divisor + 1)
print(is_prime(24))
