# ARMSTRONG NUMBER

#USING WHILE LOOP METHOD
def armstrong(n):
    # Negative edge case
    if n < 0:
        return "Negative numbers are not Armstrong Numbers"
    original = n
    # Count digits
    digits = len(str(n))
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** digits
        n = n // 10
    if total == original:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"
print(armstrong(153))

#USING STRING TRAVERSAL
def armstrong(n):
    if n < 0:
        return "Invalid Number"
    digits = len(str(n))
    total = 0
    for digit in str(n):
        total += int(digit) ** digits
    if total == n:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"
print(armstrong(153))

#USING LIST COMPREHENSION METHOD
def armstrong(n):
    if n < 0:
        return "Invalid"
    digits = len(str(n))
    total = sum([int(digit) ** digits for digit in str(n)])
    if total == n:
        return "Armstrong Number"
    return "Not Armstrong Number"
print(armstrong(153))

#USING RECURSION METHOD
def power_sum(n, digits):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** digits) + power_sum(n // 10, digits)
def armstrong(n):
    if n < 0:
        return "Invalid"
    digits = len(str(n))
    total = power_sum(n, digits)
    if total == n:
        return "Armstrong Number"
    return "Not Armstrong Number"
print(armstrong(153))