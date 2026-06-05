#NUMBER TRIANGLE PATTERN
#CORE IDEA:
      #EACH ROW STARTS FROM 1
      #NUMBERS INCREASE BY 1
      #EACH NEW ROW PRINTS ONE EXTRA NUMBER
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT 1
      #NEGATIVE NUMBER -> INVALID INPUT
#KEY OBSERVATION:
      #ROW 1 -> 1
      #ROW 2 -> 12
      #ROW 3 -> 123
      #ROW N -> 123...N
      #NUMBERS PRINT FROM 1 TO ROW
#APPROACH:
      #LOOP THROUGH ROWS
      #FOR EACH ROW PRINT 1 TO ROW
      #MOVE TO NEXT LINE
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
      #PRINT NUMBERS FROM 1 TO CURRENT ROW
      #TO FORM A NUMBER TRIANGLE
      
      
#USING NESTED LOOP METHOD
n=int(input("enter a number"))
for row in range(1,n+1):
    for num in range(1,row+1):
        print(num,end="")
    print()


#USING STRING MULTIPLICATION METHOD
n=int(input("enter a number"))
if n<=0:
    print("invalid number")
else:
    for row in range(1,n+1):
        current_row=""
        for num in range(1,row+1):
            current_row+=str(num)
        print(current_row)

#BETTER STRING METHOD
n=int(input("enter a number"))
for row in range(1,n+1):
    print("".join(str(num) for num in range(1,row+1)))
    
#USING RECURSION METHOD
def num_triangle(n,row):
    if n<=0:
        print("invalid number")
    if row>n:
        return
    for num in range(1,row+1):
        print(num,end="")
    print()
    num_triangle(n,row+1)
n=int(input("enter a number"))
num_triangle(n,row=0)