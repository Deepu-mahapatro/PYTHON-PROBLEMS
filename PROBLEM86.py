#SUM OF NATURAL NUMBERS(RECURSION)
#CORE IDEA:
#FIND SUM OF NUMBERS FROM 1 TO N
#USE RECURSION
#EDGE CASES:
#N<0
#N=0
#N=1
#LARGE N
#KEY OBSERVATION:
#SUM(N)=N+SUM(N-1)
#RECURSION CONTINUES UNTIL BASE CASE
#EXAMPLE:
#N=5
#OUTPUT=15
#APPROACH 1(STANDARD RECURSION):
#BASE CASE N==0
#RETURN N+SUM(N-1)
#APPROACH 2(BASE CASE N==1):
#FOR N>=1
#BASE CASE N==1
#RETURN N+SUM(N-1)
#APPROACH 3(TAIL RECURSION):
#USE ACCUMULATOR VARIABLE
#PASS RUNNING TOTAL
#APPROACH 4(START-END RECURSION):
#START FROM 1
#MOVE TOWARDS N
#ADD EACH VALUE
#APPROACH 5(DIVIDE AND CONQUER):
#SPLIT RANGE INTO HALVES
#ADD LEFT SUM AND RIGHT SUM
#TIME COMPLEXITY:
#STANDARD RECURSION->O(N)
#BASE CASE N==1->O(N)
#TAIL RECURSION->O(N)
#START-END RECURSION->O(N)
#DIVIDE AND CONQUER->O(N)
#SPACE COMPLEXITY:
#STANDARD RECURSION->O(N)
#BASE CASE N==1->O(N)
#TAIL RECURSION->O(N)
#START-END RECURSION->O(N)
#DIVIDE AND CONQUER->O(LOGN)
#CONCLUSION:
#BETTER SOLUTION
#STANDARD RECURSION
#OPTIMAL SOLUTION
#STANDARD RECURSION
#ADVANCED SOLUTION
#TAIL RECURSION
#DIVIDE AND CONQUER
#MOST INTERVIEWERS EXPECT
#STANDARD RECURSION

#SUM OF NATURAL NUMBERS(RECURSION)
def sum_natural(n):
    #EDGE CASE
    if n<0:
        return "NATURAL NUMBERS CANNOT BE NEGATIVE NUMBERS"
    #BASE CASE
    if n==0:
        return 0
    #RECURSIVE CASE
    return n+sum_natural(n-1)
n=int(input("enter a number"))
print(sum_natural(n))


#FOR CONDITION N>=1
def sum_natural(n):
    #BASE CASE
    if n==1:
        return 1
    #RECURSIVE CASE
    return n+sum_natural(n-1)
n=int(input("enter a number "))
print(sum_natural(n))

#USING TAIL RECURSION METHOD
def sum_natural(n,total=0):
    #BASE CASE
    if n==0:
        return total
    return sum_natural(n-1,total+n)
n=int(input("enter a number"))
print(sum_natural(n))

#USING DIVIDE AND CONQUER RECURSION
def sum_range(left,right):
    if left>right:
        return 0
    if left==right:
        return left
    mid=(left+right)//2
    return sum_range(left,mid)+sum_range(mid+1,right)
left=int(input("enter starting number"))
right=int(input("enter end number"))
print(sum_range(left,right))

#USING START AND END POINTERS
def sum_natural(start,end):
    #BASE CASE
    if start>end:
        return 0
    return start+sum_natural(start+1,end)
start=int(input("enter start number"))
end=int(input("enter end number"))
print(sum_natural(start,end))