# PERFECT NUMBER TO CHECK

# USING FOR LOOP METHOD
n = int(input("Enter a number: "))
if n <= 1:
    print("Invalid Input")
else:
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        print("PERFECT NUMBER")
    else:
        print("NOT A PERFECT NUMBER")

# USING LIST COMPREHENSION METHOD
num = int(input("Enter a number: "))
result = sum([i for i in range(1, num) if num % i == 0])
if result == num:
    print("PERFECT NUMBER")
else:
    print("NOT A PERFECT NUMBER")

# BASIC LOOP METHOD
def perfect_number(n):
    if n <= 0:
        return "Not Perfect Number"
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    if total == n:
        return "Perfect Number"
    else:
        return "Not Perfect Number"
print(perfect_number(12))

# USING RECURSION METHOD
def divisor_sum(n, i=1):
    if i == n:
        return 0
    if n % i == 0:
        return i + divisor_sum(n, i + 1)
    return divisor_sum(n, i + 1)
def perfect_number(n):
    if n <= 0:
        return "Not Perfect Number"
    if divisor_sum(n) == n:
        return "Perfect Number"
    return "Not Perfect Number"
print(perfect_number(28))

# BEST METHOD
import math
def perfect_number(n):
    if n <= 1:
        return False
    total = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n
print(perfect_number(28))