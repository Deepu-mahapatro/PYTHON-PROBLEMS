#PYRAMID STAR PATTERN
#CORE IDEA:
      #PRINT SPACES FIRST
      #THEN PRINT STARS
      #SPACES DECREASE BY 1
      #STARS INCREASE BY 2
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT ONE STAR
      #NEGATIVE NUMBER -> INVALID INPUT
#KEY OBSERVATION:
      #SPACES = N - ROW
      #STARS = 2*ROW - 1
#APPROACH:
      #LOOP FROM 1 TO N
      #PRINT SPACES
      #PRINT STARS
      #MOVE TO NEXT LINE
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
#SPACES DECREASE
#STARS INCREASE
#TO FORM A PYRAMID.

#USING NESTED LOOP METHOD
n=int(input("enter number"))
#EDGE CASE
if n<=0:
    print("INVALID NUMBER")
else:
    #PRINT EACH ROW
    for row in range(1,n+1):
        #PRINT SPACES
        for space in range(n-row):
            print(" ",end="")
        #PRINT STARS
        for star in range(2*row-1):
            print("*",end="")
        #MOVE TO NEXT LINE
        print()

#USING STRING MULTIPLICATION METHOD
def pyramid(n):
    #EDGE CASE:
    if n<=0:
        print("INVALID NUMBER")
        return
    for row in range(1,n+1):
        spaces=" "* (n-row)
        stars="*" * (2*row-1)
        print(spaces+stars)
n=int(input("enter a number"))
pyramid(n)


#USING RECURSION METHOD
def pyramid(row,n):
    #BASE CASE
    if row>n:
        return
    #PRINT CURRENT ROW
    spaces=" " * (n-row)
    stars="*" * (2*row-1)
    print(spaces+stars)
    #RECURSIVE CALL
    pyramid(row+1,n)
n=int(input("enter a number"))
if n<=0:
    print("INVALID NUMBER")
else:
    pyramid(1,n)