#FLOYD'S TRIANGLE PATTERN
#CORE IDEA:
      #NUMBERS START FROM 1
      #NUMBERS CONTINUE IN SEQUENCE
      #EACH ROW PRINTS AS MANY NUMBERS
      #AS ITS ROW NUMBER
#EDGE CASES:
      #N <= 0 -> INVALID INPUT
      #N = 1 -> PRINT 1
      #NEGATIVE NUMBER -> INVALID INPUT
#KEY OBSERVATION:
      #ROW 1 -> 1
      #ROW 2 -> 2 3
      #ROW 3 -> 4 5 6
      #ROW 4 -> 7 8 9 10
      #NUMBERS NEVER RESTART
      #THEY KEEP INCREASING ACROSS ROWS
#APPROACH:
      #INITIALIZE NUM = 1
      #LOOP THROUGH ROWS
      #PRINT CURRENT NUMBER
      #INCREMENT NUM AFTER EACH PRINT
      #MOVE TO NEXT LINE AFTER EACH ROW
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
      #PRINT CONTINUOUSLY INCREASING NUMBERS
      #WITH EACH ROW CONTAINING
      #A NUMBER OF ELEMENTS EQUAL
      #TO ITS ROW NUMBER

#NESTED LOOP METHOD(FROM STARTING 0)
n=int(input("enter number"))
if n<=0:
    print("invalid number")
elif n==1:
    print(1)
else:
    for i in range(1,n+1):
        for j in range(i):
            print(j,end="")
        print()
        

#NESTED LOOP METHOD(FROM STARTING 1)
n=int(input("enter a number"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
    
#USING RECURSION METHOD
def flo_triangle(n,row,col,num):
    if row>n:
        return
    if col<row:
        print(num,end=" ")
        flo_triangle(n,row,col+1,num+1)
    else:
        print()
        flo_triangle(n,row+1,0,num)
n=int(input("enter a number"))
flo_triangle(n,1,0,1)

#USING STRING MULTIPLICATION METHOD
n=int(input("enter a number"))
num=1
for i in range(1,n+1):
    row=""
    for j in range(i):
        row+=str(num) + " "
        num+=1
    print(row)