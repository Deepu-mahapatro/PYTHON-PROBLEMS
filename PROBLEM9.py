#FIBONACCI SERIES OF NUMBER N

#WITHOUT USING LIST LOOP METHOD
def fibonacci(n):
    if n<=0:
        return "invalid input"
    a=0
    b=1
    for i in range(n):
        print(a,end="")
        c=a+b
        a=b
        b=c
fibonacci(7)

#USING USING LIST LOOP METHOD
def fibonacci(n):
    if n<=0:
        return "enter a positive number"
    if n==1:
        return [0]
    #starting values
    a=0
    b=1
    #always teh first two values are in result
    result=[0,1]
    #for remaining elements
    for i in range(2,n):
        c=a+b
        result.append(c)
        a=b
        b=c
    return result
print(fibonacci(7))

#USING RECURSION METHOD
def fibonacci(n):
    if n<=0:
        return "invalid"
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))