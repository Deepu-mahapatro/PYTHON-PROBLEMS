# FIND MISSING NUMBER FROM 1 TO N
# CORE IDEA:
      # NUMBERS SHOULD EXIST FROM 1 TO N
      # ONE NUMBER IS MISSING
      # FIND THE NUMBER NOT PRESENT
# EDGE CASES:
      # EMPTY ARRAY
      # N = 1
      # MISSING FIRST NUMBER
      # MISSING LAST NUMBER
      # ARRAY NOT SORTED
      # ONLY ONE NUMBER MISSING
# KEY OBSERVATION:
      # EXPECTED NUMBERS = 1 TO N
      # ACTUAL NUMBERS = ARRAY ELEMENTS
      # ANSWER = EXPECTED - ACTUAL
      # RANGE(1,N+1) REPRESENTS ALL EXPECTED NUMBERS
      # NUMS REPRESENTS ONLY PRESENT NUMBERS
# EXAMPLE:
      # NUMS = [1,2,3,5]
      # N = 5
      # EXPECTED = [1,2,3,4,5]
      # ACTUAL = [1,2,3,5]
      # MISSING = 4
# APPROACH 1 (BRUTE FORCE):
      # CHECK EVERY NUMBER
      # FROM 1 TO N
      # IF NUMBER NOT IN ARRAY
      # RETURN NUMBER
# APPROACH 2 (SORTING):
      # SORT ARRAY
      # COMPARE VALUE WITH INDEX+1
      # FIRST MISMATCH
      # IS THE ANSWER
# APPROACH 3 (HASH SET):
      # STORE ELEMENTS IN SET
      # CHECK NUMBERS FROM 1 TO N
      # FIRST NUMBER NOT IN SET
      # IS THE ANSWER
# APPROACH 4 (SUM FORMULA):
      # EXPECTED SUM
      # N*(N+1)//2
      # ACTUAL SUM
      # SUM(NUMS)
      # MISSING
      # EXPECTED SUM - ACTUAL SUM
# APPROACH 5 (XOR METHOD):
      # XOR ALL NUMBERS
      # FROM 1 TO N
      # XOR ALL ARRAY ELEMENTS
      # SAME NUMBERS CANCEL
      # MISSING NUMBER REMAINS
# TIME COMPLEXITY:
      # BRUTE FORCE      -> O(N²)
      # SORTING          -> O(N LOG N)
      # HASH SET         -> O(N)
      # SUM FORMULA      -> O(N)
      # XOR METHOD       -> O(N)
# SPACE COMPLEXITY:
      # BRUTE FORCE      -> O(1)
      # SORTING          -> O(1)
      # HASH SET         -> O(N)
      # SUM FORMULA      -> O(1)
      # XOR METHOD       -> O(1)
# CONCLUSION:
      # BETTER SOLUTION
            # HASH SET
      # OPTIMAL SOLUTION
            # SUM FORMULA
      # ADVANCED OPTIMAL
            # XOR METHOD
      # MOST INTERVIEWERS EXPECT
            # SUM FORMULA OR XOR

#BRUTE FORCE APPROACH
nums=[1,2,3,5]
n=5
for num in range(1,n+1):
    if num not in nums:
        print("MISSING NUMBER :",num)
        break
    
#USING SORTING METHOD
nums=[1,2,3,5]
n=5
nums.sort()
for i in range(len(nums)):
    if nums[i]!=i+1:
        print("MISSING NUMBER :",i+1)
        break
else:
    print("MISSING NUMBER :",n)
    
#USING HASH SET METHOD
nums=[1,2,3,5]
n=5
seen=set(nums)
for num in range(1,n+1):
    if num not in seen:
        print("MISSING NUMBER :",num)
        break
    
#USING FORMULA METHOD
nums=[1,2,3,5]
n=5
expected_sum=n*(n+1)//2
actual_sum=sum(nums)
missing=expected_sum-actual_sum
print("MISSING NUMBER :",missing)

#USING XOR FORMULA METHOD
nums=[1,2,3,5]
n=5
xor1=0
xor2=0
for i in range(1,n+1):
    xor1^=i
for j in nums:
    xor2^=j
missing=xor1^xor2
print("MISSING NUMBER :",missing)
