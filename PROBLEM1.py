# CHECK PRIME NUMBER

nums=int(input("enter a number"))
if nums<=1:
    print("not a prime number")
else:
    for i in range(2,nums):
        if nums%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")
        
#FOR A GIVEN RANGE START TO END
start=int(input("enter a number"))
end=int(input("enter b number"))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
            
#BASIC LOOP METHOD
def prime(n):
    # Edge cases
    if n <= 1:
        return "Not Prime"
    # Check divisibility
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print(prime(7))

#USING COUNT METHOD
def prime(n):
    if n <= 1:
        return "Not Prime"
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "Prime"
    else:
        return "Not Prime"
print(prime(13))

#USING RECURSION METHOD
def check_prime(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return check_prime(n, i + 1)
print(check_prime(7))