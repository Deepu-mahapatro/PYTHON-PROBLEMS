# CHUNK LIST INTO GROUPS OF SIZE N
# CORE IDEA:
      # SPLIT LIST INTO SMALLER GROUPS
      # EACH GROUP SHOULD CONTAIN N ELEMENTS
      # LAST GROUP MAY CONTAIN FEWER ELEMENTS
# EDGE CASES:
      # EMPTY LIST
      # N = 1
      # N = LENGTH OF LIST
      # N > LENGTH OF LIST
      # SINGLE ELEMENT LIST
      # LAST CHUNK INCOMPLETE
      # DUPLICATE VALUES
      # NEGATIVE NUMBERS
      # N <= 0 (INVALID INPUT)
# KEY OBSERVATION:
      # CHUNKS START AT EVERY NTH INDEX
      # SLICING CAN DIRECTLY EXTRACT CHUNKS
      # EVERY ELEMENT BELONGS TO EXACTLY ONE CHUNK
      # O(N) IS THE BEST POSSIBLE TIME COMPLEXITY
# EXAMPLE:
      # NUMS = [1,2,3,4,5,6,7,8]
      # N = 3
      # RESULT = [[1,2,3],[4,5,6],[7,8]]
# APPROACH 1 (BRUTE FORCE LOOP):
      # ITERATE IN STEPS OF N
      # EXTRACT CHUNK USING SLICING
      # APPEND TO RESULT
# APPROACH 2 (MANUAL TWO INDEX WINDOW):
      # USE START AND END POINTERS
      # CREATE WINDOW OF SIZE N
      # MOVE WINDOW FORWARD
# APPROACH 3 (BUILT-IN BATCHED):
      # USE ITERTOOLS.BATCHED
      # AUTOMATICALLY CREATE GROUPS
      # RETURN CHUNKS AS TUPLES
# APPROACH 4 (WHILE LOOP):
      # START FROM INDEX 0
      # CREATE CHUNK USING SLICING
      # MOVE INDEX BY N
# TIME COMPLEXITY:
      # BRUTE FORCE LOOP      -> O(N)
      # TWO INDEX WINDOW      -> O(N)
      # BATCHED               -> O(N)
      # WHILE LOOP            -> O(N)
# SPACE COMPLEXITY:
      # BRUTE FORCE LOOP      -> O(N)
      # TWO INDEX WINDOW      -> O(N)
      # BATCHED               -> O(N)
      # WHILE LOOP            -> O(N)
# CONCLUSION:
      # SIMPLEST SOLUTION
            # BRUTE FORCE LOOP
      # CLEANEST SOLUTION
            # WHILE LOOP
      # BUILT-IN PYTHON SOLUTION
            # ITERTOOLS.BATCHED
      # INTERVIEW FRIENDLY
            # BRUTE FORCE LOOP
      # MOST INTERVIEWERS EXPECT
            # FOR LOOP + SLICING
      # OPTIMAL SOLUTION
            # O(N) TIME

#BRUTE FORCE LOOP METHOD
nums=[1,2,3,4,5,6,7,8]
n=3
result=[]
for i in range(0,len(nums),n):
    result.append(nums[i:i+n])
print(result)

#MANUAL TEO INDEX WINDOW
nums=[1,2,3,4,5,6,7,8]
n=3
result=[]
start=0
while start<len(nums):
    end=start+n
    result.append(nums[start:end])
    start=end
print(result)

#USING BUILT IN METHOD BATCHED
from itertools import batched
nums=[1,2,3,4,5,6,7,8]
result=list(batched(nums,3))
print(result)

#USING WHILE LOOP METHOD
nums=[1,2,3,4,5,6,7,8]
n=3
result=[]
i=0
while i<len(nums):
    result.append(nums[i:i+n])
    i+=n
print(result)