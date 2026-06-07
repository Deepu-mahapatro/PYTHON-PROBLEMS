#ALPHABET TRIANGLE PATTERN
#PATTERN:
      #A
      #AB
      #ABC
      #ABCD
      #ABCDE
#CORE IDEA:
      #EACH ROW STARTS FROM 'A'
      #PRINT ALPHABETS IN SEQUENCE
      #NUMBER OF CHARACTERS IN A ROW
      #IS EQUAL TO THE ROW NUMBER
#EDGE CASES:
      #N <= 0 -> NO OUTPUT
      #N = 1 -> PRINT ONLY 'A'
      #NEGATIVE NUMBER -> INVALID INPUT
#KEY OBSERVATION:
      #ROW 1 -> A
      #ROW 2 -> AB
      #ROW 3 -> ABC
      #ROW 4 -> ABCD
      #EVERY NEW ROW ADDS
      #ONE MORE ALPHABET
#LOGIC BEHIND IT:
      #OUTER LOOP CONTROLS ROWS
      #INNER LOOP CONTROLS CHARACTERS
      #FOR EACH ROW:
      #START FROM 'A'
      #PRINT CHARACTERS UP TO
      #CURRENT ROW NUMBER
#ASCII CONCEPT:
      #'A' = 65
      #'B' = 66
      #'C' = 67
      #'D' = 68
      #chr(65) -> A
      #chr(66) -> B
      #chr(67) -> C
#APPROACH:
      #TAKE N AS INPUT
      #RUN OUTER LOOP FROM 1 TO N
      #FOR EACH ROW
      #RUN INNER LOOP FROM 0 TO ROW-1
      #CONVERT NUMBER TO ALPHABET
      #USING chr(65 + j)
      #PRINT THE ROW
#MAIN LOGIC:
      #chr(65 + j)
      #j=0 -> A
      #j=1 -> B
      #j=2 -> C
      #j=3 -> D
#TIME COMPLEXITY:
      #O(N²)
#SPACE COMPLEXITY:
      #O(1)
#CONCLUSION:
      #EACH ROW BEGINS WITH 'A'
      #AND PRINTS CONSECUTIVE
      #ALPHABETS UP TO THE
      #CURRENT ROW NUMBER
      #OUTER LOOP CREATES ROWS
      #INNER LOOP CREATES LETTERS

#USING NESTED LOOP METHOD
def alphabet_tri(n):
    #EDGE CASE:
    if n<=0:
        return
    for i in range(1,n+1):
        for j in range(i):
            print(chr(65+j),end="")
        print()
n=int(input("enter a number"))
alphabet_tri(n)

#USING STRING BUILDING METHOD
def alphabet_tri(n):
    #EDGE CASE:
    if n<=0:
        return
    for i in range(1,n+1):
        row=""
        for j in range(i):
            row+=chr(65+j)
        print(row)
n=int(input("enter a number"))
alphabet_tri(n)

#USING STRING SLICING METHOD
def alphabet_triangle(n):
    if n <= 0:
        return
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1, n + 1):
        print(alphabets[:i])
n = int(input("Enter a number: "))
alphabet_triangle(n)

#USING RECURSION METHOD
def alphabet_tri(n):
    #BASE CASE
    if n==0:
        return
    #SMALLER PROBLEMS
    alphabet_tri(n-1)
    #CURRENT ROW
    for j in range(n):
        print(chr(65+j),end="")
    print()
n=int(input("enter a number"))
if n>0:
    alphabet_tri(n)
    
# LIST COMPREHENSION METHOD
def alphabet_triangle(n):
    if n <= 0:
        return
    for i in range(1, n + 1):
        print("".join(chr(65 + j) for j in range(i)))
n = int(input("Enter a number: "))
alphabet_triangle(n)