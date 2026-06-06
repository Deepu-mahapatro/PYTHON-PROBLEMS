#SAND GLASS PATTERN

#CORE IDEA:
      #PRINT STARS AND LEADING SPACES
      #UPPER HALF SHRINKS
      #LOWER HALF EXPANDS
      #FORM AN HOURGLASS SHAPE

#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT SINGLE STAR
      #NEGATIVE NUMBER -> INVALID INPUT

#KEY OBSERVATION:
      #SPACES INCREASE BY 1
      #STARS DECREASE BY 2
      #UPPER HALF:
            #SPACES INCREASE
            #STARS DECREASE
      #LOWER HALF:
            #SPACES DECREASE
            #STARS INCREASE

#APPROACH:
      #PRINT UPPER HALF
      #PRINT SPACES FIRST
      #PRINT STARS NEXT
      #PRINT LOWER HALF
      #REVERSE THE SAME LOGIC

#TIME COMPLEXITY:
      #O(N²)

#SPACE COMPLEXITY:
      #O(1)

#CONCLUSION:
      #BUILD THE UPPER HALF BY
      #INCREASING SPACES AND
      #DECREASING STARS
      #THEN MIRROR IT TO FORM
      #A COMPLETE SAND GLASS
      
#USING NESTED LOOP METHOD
n=int(input("enter a number"))
if n<=0:
    print("invalid number")
else:
    #UPPER HALF
    for i in range(1,n+1):
        #PRINT LEADING SPACES
        for j in range(i-1):
            print(" ",end="")
        #PRINT STARTS
        for j in range(2*(n-i)+1):
            print("*",end="")
        print()
    #LOWER HALF
    for i in range(n-1,0,-1):
        #PRINT LEADING SPACES
        for j in range(i-1):
            print(" ",end="")
        #PRINT STARS
        for j in range(2*(n-i)+1):
            print("*",end="")
        print()
        
#USING STRING MULTIPLICATION METHOD
n=int(input("enter a number"))
if n<=0:
    print("invalid number")
else:
    #UPPER HALF
    for i in range(1,n+1):
        spaces=" " * (i-1)
        stars="*" * (2*(n-i)+1)
        print(spaces+stars)
    #LOWER HALF
    for i in range(n-1,0,-1):
        spaces=" " * (i-1)
        stars="*" * (2*(n-i)+1)
        print(spaces+stars)
        
#USING RECURSION METHOD
def upper_half(row,n):
    if row>n:
        return
    print(" " * (row-1) + "*" * (2*(n-row)+1))
    upper_half(row+1,n)
def lower_half(row,n):
    if row==0:
        return
    print(" " * (row-1) + "*" * (2*(n-row)+1))
    lower_half(row-1,n)
n=int(input("enter a number"))
if n<=0:
    print("invalid number")
else:
    upper_half(1,n)
    lower_half(n-1,n)