
#STATEMENT 1
#Multiples of 3 form an arithmetic progression.
#STATEMENT 2
#Multiples of 5 form another arithmetic progression.
#STATEMENT 3
#Common multiples belong to multiples of 15.
#STATEMENT 4
#Adding sums separately counts common multiples twice.
#STATEMENT 5
#Subtracting sum of multiples of 15 removes duplicate counting.
#FINAL PROVEN FORMULA
#Total=Sum(3)+Sum(5)−Sum(15)​
#MOST IMPORTANT INTUITION
#The entire problem depends on:
#1. Divisibility
#Check whether number divides completely.
#2. Arithmetic Progression
#Multiples form regular increasing patterns.
#3. Inclusion-Exclusion Principle
#Add groups separately.
#Subtract overlap once.

#BRUTE FORCE METHOD
#METHOD 1 : BRUTE FORCE
def sum_multiples(n):
    #EDGE CASE
    if n < 1:
        return 0
    #SUM VARIABLE
    total = 0
    #CHECK EVERY NUMBER
    for i in range(1, n + 1):
        #DIVISIBLE BY 3 OR 5
        if i % 3 == 0 or i % 5 == 0:
            #ADD TO SUM
            total += i
    return total
#EXAMPLE
print(sum_multiples(10))

#USING MATHEMATICAL FORMULA METHOD
#METHOD 3 : OPTIMAL FORMULA METHOD
def multiple_sum(k, n):
    #COUNT OF MULTIPLES
    m = n // k
    #SUM FORMULA
    return k * m * (m + 1) // 2
def sum_multiples_formula(n):
    #EDGE CASE
    if n < 1:
        return 0
    return (
        multiple_sum(3, n)
        + multiple_sum(5, n)
        - multiple_sum(15, n)
    )
#EXAMPLE
print(sum_multiples_formula(10))

#USING RECURSIVE METHOD
#METHOD 4 : RECURSIVE METHOD
def sum_recursive(n):
    #EDGE CASE
    if n <= 0:
        return 0
    #DIVISIBLE BY 3 OR 5
    if n % 3 == 0 or n % 5 == 0:
        return n + sum_recursive(n - 1)
    #SKIP NUMBER
    return sum_recursive(n - 1)
#EXAMPLE
print(sum_recursive(10))