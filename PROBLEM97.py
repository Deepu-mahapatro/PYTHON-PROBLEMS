# GOLDBACH CONJECTURE (EXPRESS N AS SUM OF TWO PRIMES)
# APPROACH 1 (OPTIMIZED PRIME CHECK METHOD)
# CHECK NUMBERS FROM 2 TO N//2
# VERIFY BOTH NUMBERS ARE PRIME
# RETURN VALID PRIME PAIR
# TIME COMPLEXITY: O(N√N)
# SPACE COMPLEXITY: O(1)
# INTERVIEW VALUE: GOOD OPTIMIZATION
# APPROACH 2 (STORE ALL PRIME PAIRS)
# FIND ALL POSSIBLE PRIME PAIRS
# STORE RESULTS IN LIST
# RETURN ALL VALID COMBINATIONS
# TIME COMPLEXITY: O(N√N)
# SPACE COMPLEXITY: O(K)
# INTERVIEW VALUE: USEFUL WHEN ALL PAIRS ARE REQUIRED
# APPROACH 3 (SIEVE OF ERATOSTHENES)
# PRECOMPUTE ALL PRIME NUMBERS
# CHECK PRIME PAIRS USING ARRAY LOOKUP
# TIME COMPLEXITY: O(N log log N)
# SPACE COMPLEXITY: O(N)
# INTERVIEW VALUE: BEST OPTIMAL SOLUTION
# EDGE CASES
# N=4 → (2,2)
# N=6 → (3,3)
# N=8 → (3,5)
# N=10 → (3,7)
# N=20 → (3,17),(7,13)
# N=26 → (3,23),(7,19),(13,13)
# INVALID CASES
# N=1 → INVALID INPUT
# N=2 → NO SOLUTION
# N=3 → NO SOLUTION
# N=15 → INVALID INPUT (ODD NUMBER)
# N=0 → INVALID INPUT
# N<0 → INVALID INPUT
# KEY OBSERVATION
# FIND TWO PRIME NUMBERS
# SUCH THAT:
# PRIME1 + PRIME2 = N
# EXAMPLE
# N=20
# 3+17=20
# 7+13=20
# INTERVIEW COMPARISON
# PRIME CHECK METHOD → SIMPLE AND EFFICIENT
# STORE ALL PAIRS → RETURNS ALL ANSWERS
# SIEVE METHOD → BEST OPTIMIZED APPROACH
# CONCLUSION
# INTERVIEW EXPECTED:
# PRIME CHECK METHOD
# BEST OPTIMIZED SOLUTION:
# SIEVE OF ERATOSTHENES
# BEST TIME COMPLEXITY:
# O(N log log N)
# BEST SPACE COMPLEXITY:
# O(N)
# MOST RECOMMENDED:
# SIEVE OF ERATOSTHENES

#USING OPTIMIZED METHOD
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
n=int(input("ENTER A NUMBER"))
for i in range(2,n//2+1):
    if is_prime(i) and is_prime(n-i):
        print(i,n-i)


#STORE ALL PAIRS
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
n=int(input("ENTER A NUMBER"))
pairs=[]
for i in range(2,n//2+1):
    if is_prime(i) and is_prime(n-i):
        pairs.append((i,n-i))
print(pairs)

#USING SIEVE OF ERATOSTHENES
n=int(input("ENTER A UMBER"))
prime=[True]*(n+1)
prime[0]=prime[1]=False
for i in range(2,int(n**0.5)+1):
    if prime[i]:
        for j in range(i*i,n+1,i):
            prime[j]=False
for i in range(2,n//2+1):
    if prime[i] and prime[n-i]:
        print(i,n-i)