#DIAMOND STAR PATTERN
#CORE IDEA:
      #COMBINE TWO PYRAMIDS
      #TOP PYRAMID
      #BOTTOM PYRAMID
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT SINGLE STAR
#KEY OBSERVATION:
      #TOP:
            #SPACES = N-ROW
            #STARS = 2*ROW-1
      #BOTTOM:
            #SPACES = N-ROW
            #STARS = 2*ROW-1
#APPROACH:
      #PRINT TOP PYRAMID
      #PRINT BOTTOM PYRAMID
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
#A DIAMOND IS
#AN UPPER PYRAMID
#PLUS A LOWER PYRAMID.

#USING NESTED LOOP METHOD
n=int(input("enter a number"))
if n<=0:
    print("INVALID NUMBER")
else:
    #TOP HALF
    for row in range(1,n+1):
        for space in range(n-row):
            print(" ",end="")
        for stars in range(2*row-1):
            print("*",end="")
        print()
    #BOTTOM HALF
    for row in range(n-1,0,-1):
        for space in range(n-row):
            print(" ",end="")
        for stars in range(2*row-1):
            print("*",end="")
        print()

#USING STRING MULTIPLICATION METHOD
n=int(input("enter a number"))
if n<=0:
    print("INVALID NUMBER")
else:
    #TOP HALF
    for row in range(1,n+1):
        spaces=" " * (n-row)
        stars="*" * (2*row-1)
        print(spaces+stars)
    #BOTTOM HALF
    for row in range(n-1,0,-1):
        spaces=" " * (n-row)
        stars="*" * (2*row-1)
        print(spaces+stars)

#USING RECURSION METHOD
def top(row,n):
    if row>n:
        return
    print(" " * (n-row) + "*" * (2*row-1))
    top(row+1,n)
def bottom(row):
    if row==0:
        return
    print(" " * (n-row) + "*" * (2*row-1))
    bottom(row-1)
n=int(input("enter a number"))
if n<=0:
    print("INVALID NUMBER")
else:
    top(1,n)
    bottom(n-1)