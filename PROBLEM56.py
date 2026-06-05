#RIGHT ANGLED STAR TRIANGLE
#RIGHT-ANGLED STAR TRIANGLE
#CORE IDEA:
      #PRINT ROW BY ROW
      #ROW NUMBER = NUMBER OF STARS
      #OUTER LOOP CONTROLS ROWS
      #INNER LOOP PRINTS STARS
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT ONE STAR
      #NEGATIVE NUMBER -> INVALID INPUT
#KEY OBSERVATION:
      #ROW 1 -> *
      #ROW 2 -> **
      #ROW 3 -> ***
      #STARS = ROW NUMBER
#APPROACH:
      #LOOP FROM 1 TO N
      #PRINT STARS EQUAL TO ROW NUMBER
      #MOVE TO NEXT LINE
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
#PRINT STARS EQUAL TO
#THE CURRENT ROW NUMBER.

#USING FUNCTION METHOD
def right_triangle(n):
    if n<=0:
        return 0
    for row in range(1,n+1):
        for col in range(row):
            print("*",end="")
        print()
n=int(input("enter a number"))
right_triangle(n)

#USING NESTED LOOPS
n=int(input("enter a number"))
#EDGE CASE
if n<=0:
    print("invalid number")
else:
    #PRINT EACH ROW
    for row in range(1,n+1):
        #PRINT STAR FOR CURRENT ROW
        for col in range(row):
            print("*",end="")
        #MOVE NEXT LINE
        print()


#USING STRING MULTIPLICATION
def right_triangle(n):
    if n<=0:
        print("INVALID NUMBER")
        return
    for row in range(1,n+1):
        print("*" * row)
n=int(input("enter a number"))
right_triangle(n)

#USING RECURSION METHOD
def right_triangle(n):
    #EDGE CASE
    if n<=0:
        return
    #FIRST PRINT SMALLER TRIANGLE
    right_triangle(n-1)
    #PRINT CURRENT ROW
    print("*" * n)
n=int(input("enter a number"))
if n<=0:
    print("INVALID NUMBER")
else:
    right_triangle(n)