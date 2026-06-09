#SPIRAL MATRIX
#CORE IDEA:
      #FILL NUMBERS IN A CLOCKWISE SPIRAL
      #START FROM 1
      #MOVE RIGHT -> DOWN -> LEFT -> UP
      #REPEAT UNTIL ALL CELLS ARE FILLED
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT SINGLE CELL (1)
      #NEGATIVE NUMBER -> INVALID INPUT
      #N = 2 -> COMPLETE SPIRAL IN ONE LAYER
#KEY OBSERVATION:
      #USE FOUR BOUNDARIES
      #TOP -> FIRST ROW TO FILL
      #BOTTOM -> LAST ROW TO FILL
      #LEFT -> FIRST COLUMN TO FILL
      #RIGHT -> LAST COLUMN TO FILL
      #AFTER FILLING A SIDE
      #SHRINK ITS BOUNDARY
#BOUNDARIES:
      #TOP = 0
      #BOTTOM = N - 1
      #LEFT = 0
      #RIGHT = N - 1
#MOVEMENT ORDER:
      #LEFT -> RIGHT  (TOP ROW)
      #TOP -> BOTTOM  (RIGHT COLUMN)
      #RIGHT -> LEFT  (BOTTOM ROW)
      #BOTTOM -> TOP  (LEFT COLUMN)
      #REPEAT
#APPROACH:
      #CREATE N x N MATRIX FILLED WITH 0
      #INITIALIZE NUM = 1
      #INITIALIZE TOP, BOTTOM, LEFT, RIGHT
      #FILL TOP ROW
      #INCREMENT TOP
      #FILL RIGHT COLUMN
      #DECREMENT RIGHT
      #FILL BOTTOM ROW
      #DECREMENT BOTTOM
      #FILL LEFT COLUMN
      #INCREMENT LEFT
      #REPEAT UNTIL BOUNDARIES CROSS
#KEY PATTERN:
      #OUTER LAYER FILLED FIRST
      #THEN MOVE TO INNER LAYER
      #CONTINUE UNTIL CENTER IS REACHED
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(N²)
#CONCLUSION:
      #FILL THE MATRIX LAYER BY LAYER
      #IN CLOCKWISE DIRECTION
      #BY SHRINKING THE FOUR BOUNDARIES
      #UNTIL ALL CELLS ARE FILLED

#RIGHT ANGLED NUMBER TRIANGLE
#CORE IDEA:
      #EACH ROW STARTS FROM 1
      #NUMBERS INCREASE UP TO ROW NUMBER
      #ROW i PRINTS NUMBERS FROM 1 TO i
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT 1
      #NEGATIVE NUMBER -> INVALID INPUT
#KEY OBSERVATION:
      #ROW 1 -> 1
      #ROW 2 -> 1 2
      #ROW 3 -> 1 2 3
      #ROW 4 -> 1 2 3 4
      #NUMBERS RESTART FROM 1 IN EVERY ROW
#APPROACH:
      #LOOP THROUGH ROWS
      #FOR EACH ROW
      #PRINT NUMBERS FROM 1 TO CURRENT ROW NUMBER
      #MOVE TO NEXT LINE AFTER EACH ROW
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
      #PRINT NUMBERS STARTING FROM 1
      #IN EVERY ROW
      #UP TO THE CURRENT ROW NUMBER
      #FORMING A RIGHT ANGLED TRIANGLE

#USING NESTED LOOP METHOD
n=int(input("enter a number"))
if n<=0:
    print("invalid number")
elif n==1:
    print(1)
else:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
        
#USING RECURSION METHOD
def right_angle(n,row=1):
    #BASE CASE
    if n<=0:
        print("invalid input")
        return
    #STOP RECURSION
    if row>n:
        return
    #PRINT CURRENT ROW
    for num in range(1,row+1):
        print(num,end="")
    print()
    #RECURSIVE CALL
    right_angle(n,row+1)
n=int(input("enter a number"))
right_angle(n)

#STRING JOIN METHOD
n=int(input("enter a number"))
if n<=0:
    print("invalid input")
else:
    for i in range(1,n+1):
        temp=[]
        #GENERATE NUMBERS FOR CURRENT ROW
        for num in range(1,i+1):
            temp.append(str(num))
        #JOIN ALL ELEMENTS WITH SPACES
        row= "".join(temp)
        print(row)
    