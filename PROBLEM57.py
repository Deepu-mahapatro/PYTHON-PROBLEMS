#INVERTED STAR TRIANGLE 
#ALSO CALLED AS REVERSE RIGHT ANGLED TRIANGLE
#INVERTED RIGHT-ANGLED STAR TRIANGLE
#CORE IDEA:
      #PRINT ROW BY ROW
      #START WITH N STARS
      #DECREASE ONE STAR
      #IN EACH ROW
      #OUTER LOOP CONTROLS ROWS
      #INNER LOOP PRINTS STARS
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT ONE STAR
      #NEGATIVE NUMBER -> INVALID INPUT
#KEY OBSERVATION:
      #ROW 1 -> N STARS
      #ROW 2 -> N-1 STARS
      #ROW 3 -> N-2 STARS
      #LAST ROW -> 1 STAR
      #STARS DECREASE BY 1
      #IN EVERY ROW
#APPROACH:
      #LOOP FROM N TO 1
      #PRINT STARS EQUAL
      #TO CURRENT ROW VALUE
      #MOVE TO NEXT LINE
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
#START WITH N STARS
#AND DECREASE BY 1
#UNTIL ONE STAR REMAINS.

#USING NESTED LOOP METHOD
n=int(input("enter a number"))
#EDGE CASE
if n<=0:
    print("INVALID NUMBER")
else:
    #PRINT EACH ROW
    for row in range(n,0,-1):
        #PRINT STARS FOR EACH ROW
        for col in range(row):
            print("*",end="")
        #MOVE TO NEXT LINE
        print()

#USING STRING MULTIPLICATION METHOD
def invert_triangle(n):
    #EDGE CASE
    if n<=0:
        print("INVALID TRIANGLE")
        return
    for row in range(n,0,-1):
        print("*" * row)
n=int(input("enter a number"))
invert_triangle(n)

#USING RECURSION METHOD
def invert_triangle(n):
    #EDGE CASE
    if n<=0:
        return
    #PRINT CURRENT ROW
    print("*" * n)
    #PRINT SMALLER TRIANGLE
    invert_triangle(n-1)
n=int(input("enter a number"))
if n<=0:
    print("INVALID NUMBER")
else:
    invert_triangle(n)