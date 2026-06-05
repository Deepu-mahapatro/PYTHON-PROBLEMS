#HOLLOW TRIANGLE PATTERN
#CORE IDEA:
      #PRINT STARS ONLY ON BOUNDARIES
      #PRINT SPACES INSIDE THE TRIANGLE
      #LEFT SIDE IS STARS
      #RIGHT SIDE IS STARS
      #LAST ROW IS ALL STARS
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT ONE STAR
      #N = 2 -> NO HOLLOW AREA
      #NEGATIVE NUMBER -> INVALID INPUT
#KEY OBSERVATION:
      #LEFT BORDER -> COL == 0
      #RIGHT BORDER -> ROW == COL
      #BOTTOM BORDER -> ROW == N-1
      #INSIDE AREA -> SPACES
#APPROACH:
      #LOOP THROUGH ROWS
      #LOOP THROUGH COLUMNS UP TO ROW+1
      #CHECK BORDER CONDITIONS
      #PRINT STAR FOR BORDER
      #PRINT SPACE FOR INSIDE
      #MOVE TO NEXT LINE
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
      #PRINT STARS ON LEFT BORDER
      #PRINT STARS ON RIGHT BORDER
      #PRINT STARS ON LAST ROW
      #TO FORM A HOLLOW TRIANGLE
      
      
#USING NESTED LOOPS METHOD
n=int(input("enter a number"))
if n==1:
    print("*")
else:
    for row in range(n):
        for col in range(row+1):
            if col==0 or row==col or row==n-1:
                print("*",end="")
            
            else:
                print(" ",end="")
        print()


#USING STRING MULTIPLICATION METHOD
n=int(input("enter a number"))
if n<=0:
    print("invalid number")
elif n==1:
    print("*")
else:
    print("*")
    for row in range(1,n-1):
        print("*" + " "*(row-1) + "*")
    print("*" * n)
    
#USING RECURSION METHOD
def hollow_triangle(n,row=0):
    if row==n:
        return
    for col in range(row+1):
        if col==0 or row==col or row==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    hollow_triangle(n,row+1)
n=int(input("enter a number"))
hollow_triangle(n)