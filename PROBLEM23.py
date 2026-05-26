#COLLATZ SEQUENCE OF N
#IT IS ALSO CALLED AS 3N+1,HAILSTONE SEQUENCE
#IT IS A REPEATED PROCESS BASED ON PRIORITY:
         #IF EVEN -> DIVIDE BY 2
         #IF ODD -> MULTIPLY BY 3 THEN ADD 1(3N+1)
#CONTINUE UNTIL IT REACHES 1
# SO IT KEEPS REPEATING INCREASING AND DECREASING
#UNTIL IT REACHES 1

#BASIC ITERATIVE METHOD
def coll_sequence(n):
    #EDGE CASE : INVALID INPUT
    if n<=0:
        return "ENTER A POSITIVE NUMBER"
    #STORE SEQUENCE
    sequence=[n]
    #CONTINUE UNTIL 1
    while n!=1:
        #FOR EVEN NUMBER
        if n%2==0:
            n=n//2
        #FOR ODD NUMBER
        else:
            n=3*n +1
        #STORE VALUE
        sequence.append(n)
    return sequence
print(coll_sequence(6))
print("\n")

#PRINT DIRECTLY WITHOUT SORTING
#PRINT DIRECTLY METHOD
def coll_print(n):
    #EDGE CASE
    if n <= 0:
        print("ENTER A POSITIVE INTEGER")
        return
    #PRINT START
    print(n, end=" ")
    #PROCESS
    while n != 1:
        #EVEN
        if n % 2 == 0:
            n = n // 2   
        #ODD
        else:
            n = 3 * n + 1
        #PRINT VALUE
        print(n, end=" ")
#EXAMPLE
coll_print(6)
print("\n")

#USING RECURSIVE METHOD
#RECURSIVE METHOD
def coll_recursive(n):
    #EDGE CASE
    if n <= 0:
        print("ENTER A POSITIVE INTEGER")
        return
    #PRINT CURRENT VALUE
    print(n, end=" ")
    #BASE CONDITION
    if n == 1:
        return
    #EVEN CASE
    if n % 2 == 0:
        coll_recursive(n // 2)
    #ODD CASE
    else:
        coll_recursive(3 * n + 1)
#EXAMPLE
coll_recursive(6)