#BUTTERFLY PATTERN
#CORE IDEA:
      #PRINT STARS ON LEFT SIDE
      #PRINT SPACES IN THE MIDDLE
      #PRINT STARS ON RIGHT SIDE
      #UPPER HALF EXPANDS
      #LOWER HALF CONTRACTS

#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT TWO STARS
      #NEGATIVE NUMBER -> INVALID INPUT

#KEY OBSERVATION:
      #LEFT STARS = ROW NUMBER
      #RIGHT STARS = ROW NUMBER
      #SPACES = 2 × (N-ROW)
      #UPPER HALF:
            #STARS INCREASE
            #SPACES DECREASE
      #LOWER HALF:
            #STARS DECREASE
            #SPACES INCREASE

#APPROACH:
      #PRINT UPPER HALF
      #PRINT LEFT STARS
      #PRINT MIDDLE SPACES
      #PRINT RIGHT STARS
      #PRINT LOWER HALF USING SAME LOGIC
      #IN REVERSE ORDER

#TIME COMPLEXITY:
      #O(N²)

#SPACE COMPLEXITY:
      #O(1)

#CONCLUSION:
      #BUILD THE PATTERN USING
      #LEFT STARS + SPACES + RIGHT STARS
      #AND MIRROR IT TO FORM
      #A BUTTERFLY SHAPE
      
#USING NESTED LOOP METHOD
n=int(input("enter a number"))
if n<0:
    print("invalid number")
else:
    #UPPER HALF
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        for j in range(2*(n-i)):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        print()
    #LOWER HALF
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="")
        for j in range(2*(n-i)):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        print()
        
#USING STRING MULTIPLICATION METHOD
n=int(input("enter a number"))
if n<0:
    print("invalid input")
else:
    #UPPER HALF
    for i in range(1,n+1):
        left="*" * i
        middle=" " * (2*(n-i))
        right="*" * i
        print(left+middle+right)
    #LOWER HALF
    for i in range(n,0,-1):
        left="*" * i
        middle=" " * (2*(n-i))
        right="*" * i
        print(left+middle+right)
        
#USING RECURSION METHOD
def butterfly_upper(row,n):
    if row>n:
        return
    print("*" * row + " " * (2*(n-row)) + "*" * row)
    butterfly_upper(row+1,n)
def butterfly_lower(row):
    if row==0:
        return
    print("*" * row + " " * (2*(n-row)) + "*" * row)
    butterfly_lower(row-1)
n=int(input("enter a number"))
if n<=0:
    print("invalid number")
else:
    butterfly_upper(1,n)
    butterfly_lower(n)