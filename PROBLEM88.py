#COUNT OCCURRENCES OF AN ELEMENT(RECURSION)
#CORE IDEA:
#COUNT HOW MANY TIMES TARGET APPEARS
#USE RECURSION TO TRAVERSE ARRAY
#EDGE CASES:
#EMPTY ARRAY
#SINGLE ELEMENT ARRAY
#TARGET NOT PRESENT
#TARGET PRESENT ONCE
#TARGET PRESENT MULTIPLE TIMES
#ALL ELEMENTS SAME
#DUPLICATE VALUES
#LARGE ARRAY
#KEY OBSERVATION:
#CHECK CURRENT ELEMENT
#IF MATCH COUNT 1
#OTHERWISE COUNT 0
#ADD RESULT FROM REMAINING ARRAY
#EXAMPLE:
#ARR=[1,2,3,2,4,2]
#TARGET=2
#OUTPUT=3
#APPROACH 1(INDEX RECURSION):
#START FROM INDEX 0
#CHECK EACH ELEMENT
#MOVE TO NEXT INDEX
#COUNT MATCHES
#BASE CASE:
#INDEX==LEN(ARR)
#RETURN 0
#RECURSIVE CASE:
#IF MATCH RETURN 1+RECURSIVE CALL
#ELSE RETURN RECURSIVE CALL
#APPROACH 2(SLICING RECURSION):
#CHECK FIRST ELEMENT
#RECURSE ON REMAINING ARRAY
#BASE CASE:
#LEN(ARR)==0
#RETURN 0
#RECURSIVE CASE:
#IF MATCH RETURN 1+RECURSIVE CALL
#ELSE RETURN RECURSIVE CALL
#APPROACH 3(REVERSE RECURSION):
#START FROM LAST INDEX
#MOVE TOWARDS FIRST INDEX
#COUNT MATCHES
#BASE CASE:
#INDEX<0
#RETURN 0
#RECURSIVE CASE:
#IF MATCH RETURN 1+RECURSIVE CALL
#ELSE RETURN RECURSIVE CALL
#APPROACH 4(DIVIDE AND CONQUER):
#DIVIDE ARRAY INTO TWO HALVES
#COUNT IN LEFT HALF
#COUNT IN RIGHT HALF
#ADD BOTH RESULTS
#BASE CASE:
#LEFT>RIGHT RETURN 0
#LEFT==RIGHT RETURN 1 OR 0
#RECURSIVE CASE:
#COUNT LEFT+COUNT RIGHT
#TIME COMPLEXITY:
#INDEX RECURSION->O(N)
#SLICING RECURSION->O(N²)
#REVERSE RECURSION->O(N)
#DIVIDE AND CONQUER->O(N)
#SPACE COMPLEXITY:
#INDEX RECURSION->O(N)
#SLICING RECURSION->O(N)
#REVERSE RECURSION->O(N)
#DIVIDE AND CONQUER->O(LOGN)
#CONCLUSION:
#BETTER SOLUTION
#INDEX RECURSION
#OPTIMAL SOLUTION
#INDEX RECURSION
#ADVANCED SOLUTION
#DIVIDE AND CONQUER
#MOST INTERVIEWERS EXPECT
#INDEX RECURSION

#USING INDEX RECURSION METHOD
def count_occurrences(arr, target, index=0):
    # BASE CASE
    if index == len(arr):
        return 0
    # RECURSIVE CASE
    if arr[index] == target:
        return 1 + count_occurrences(arr, target, index + 1)
    return count_occurrences(arr, target, index + 1)
arr = [1, 2, 3, 2, 4, 2]
target = 2
print(count_occurrences(arr, target))

# USING SLICING
def count_occurrences(arr, target):
    # BASE CASE
    if len(arr) == 0:
        return 0
    # RECURSIVE CASE
    if arr[0] == target:
        return 1 + count_occurrences(arr[1:], target)
    return count_occurrences(arr[1:], target)
arr = [1, 2, 3, 2, 4, 2]
print(count_occurrences(arr, 2))

# REVERSE TRAVERSAL RECURSION
def count_occurrences(arr, target, index):
    # BASE CASE
    if index < 0:
        return 0
    # RECURSIVE CASE
    if arr[index] == target:
        return 1 + count_occurrences(arr, target, index - 1)
    return count_occurrences(arr, target, index - 1)
arr = [1, 2, 3, 2, 4, 2]
print(count_occurrences(arr, 2, len(arr)-1))

# DIVIDE AND CONQUER
def count_occurrences(arr, target, left, right):
    # BASE CASE
    if left > right:
        return 0
    if left == right:
        return 1 if arr[left] == target else 0
    mid = (left + right) // 2
    return (count_occurrences(arr, target, left, mid) +
            count_occurrences(arr, target, mid + 1, right))
arr = [1, 2, 3, 2, 4, 2]
print(count_occurrences(arr, 2, 0, len(arr)-1))
