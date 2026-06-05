#HOLLOW SQUARE PATTERN 
#CORE IDEA:
      #PRINT STARS ON THE BORDER
      #PRINT SPACES INSIDE THE SQUARE
      #FIRST ROW -> ALL STARS
      #LAST ROW -> ALL STARS
      #FIRST COLUMN -> STAR
      #LAST COLUMN -> STAR
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT ONE STAR
      #N = 2 -> ALL BORDER CELLS ARE STARS
      #NEGATIVE NUMBER -> INVALID INPUT
#KEY OBSERVATION:
      #TOP BORDER -> ROW == 0
      #BOTTOM BORDER -> ROW == N-1
      #LEFT BORDER -> COL == 0
      #RIGHT BORDER -> COL == N-1
      #INSIDE CELLS -> SPACES
#APPROACH:
      #LOOP THROUGH ALL ROWS
      #LOOP THROUGH ALL COLUMNS
      #CHECK IF CURRENT CELL IS ON BORDER
      #PRINT STAR FOR BORDER
      #PRINT SPACE FOR INSIDE
      #MOVE TO NEXT LINE AFTER EACH ROW
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
      #PRINT STARS ON ALL FOUR BORDERS
      #PRINT SPACES INSIDE
      #TO FORM A HOLLOW SQUARE.

#USING NESTED LOOP METHOD
n=int(input("enter a number"))
if n==1:
    print ("*")
else:
    for row in range(n):
        for col in range(n):
            if row==0 or row==n-1 or col==0 or col==n-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
            
#USING STRING MULTIPLICATION METHOD
n=int(input("enter a number"))
if n==1:
    print ("*")
else:
    print("*" * n)
    for _ in range(n-2):
        print("*" + " " * (n-2) + "*" )
    print("*" * n)
    
    
    
#USING RECURSION METHOD
def hollow_square(n,row=0):
    if row==n:
        return
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()   
    hollow_square(n,row+1)
hollow_square(5)