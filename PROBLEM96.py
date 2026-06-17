# FIND ALL PYTHAGOREAN TRIPLETS UP TO N
# APPROACH 1 (BRUTE FORCE METHOD)
# CHECK EVERY POSSIBLE a,b,c
# CONDITION: a²+b²=c²
# TIME COMPLEXITY: O(N³)
# SPACE COMPLEXITY: O(1)
# INTERVIEW VALUE: EASY TO UNDERSTAND
# APPROACH 2 (NESTED LOOP + SQRT METHOD)
# CALCULATE c USING SQUARE ROOT
# CHECK IF c IS AN INTEGER
# CONDITION: a²+b²=c²
# TIME COMPLEXITY: O(N²)
# SPACE COMPLEXITY: O(1)
# INTERVIEW VALUE: MOST RECOMMENDED
# APPROACH 3 (EUCLID'S FORMULA)
# a=m²-k²
# b=2mk
# c=m²+k²
# GENERATES PYTHAGOREAN TRIPLETS DIRECTLY
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(1)
# INTERVIEW VALUE: ADVANCED MATHEMATICAL APPROACH
# EDGE CASES
# N=0 → []
# N=1 → []
# N=4 → []
# N=5 → (3,4,5)
# N=10 → (3,4,5)
# N=20 → (3,4,5),(5,12,13),(8,15,17)
# NEGATIVE N → []
# LARGE N → USE EUCLID'S FORMULA
# KEY OBSERVATION
# PYTHAGOREAN TRIPLET:
# a²+b²=c²
# EXAMPLE:
# 3²+4²=5²
# 9+16=25
# INTERVIEW COMPARISON
# BRUTE FORCE → SIMPLE BUT SLOW
# SQRT METHOD → BEST PRACTICAL SOLUTION
# EUCLID'S FORMULA → BEST OPTIMIZED SOLUTION
# CONCLUSION
# INTERVIEW EXPECTED:
# SQRT METHOD
# BEST TIME COMPLEXITY:
# O(N)
# USING:
# EUCLID'S FORMULA
# BEST PRACTICAL APPROACH:
# O(N²)
# USING:
# NESTED LOOP + SQRT

#BRUTE FORCE METHOD
n=int(input("enter a number"))
for a in range(1,n+1):
    for b in range(a+1,n+1):
        for c in range(b+1,n+1):
            if a*a+b*b==c*c:
                print((a,b,c))


#USING NESTED LOOP METHOD
import math
n=int(input("ENTER N:"))
for a in range(1,n+1):
    for b in range(a+1,n+1):
        c=math.sqrt(a*a+b*b)
        if c==int(c) and c<=n:
            print((a,b,int(c)))
            

#USING EUCLID'S FORMULA
n=int(input("ENTER N:"))
for m in range(2,n):
    for k in range(1,m):
        a=m*m-k*k
        b=2*m*k
        c=m*m+k*k
        if c<=n:
            print((a,b,c))


#COMPLETE VERSION OF EUCLID'S METHOD
n=int(input("ENTER N:"))
for m in range(2,n):
    for k in range(1,m):
        a=m*m-k*k
        b=2*m*k
        c=m*m+k*k
        factor=1
        while factor*c<=n:
            print(
                (
                    factor*a,
                    factor*b,
                    factor*c
                )
            )
            factor+=1