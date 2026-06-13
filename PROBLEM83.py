# FIND PAIR WITH GIVEN SUM
# CORE IDEA:
      # FIND TWO NUMBERS
      # WHOSE SUM EQUALS TARGET
# EDGE CASES:
      # EMPTY ARRAY
      # SINGLE ELEMENT
      # NO PAIR EXISTS
      # DUPLICATE VALUES
      # NEGATIVE NUMBERS
      # MULTIPLE PAIRS
# KEY OBSERVATION:
      # FOR EVERY NUMBER
      # COMPLEMENT = TARGET - NUMBER
      # IF COMPLEMENT EXISTS
      # PAIR IS FOUND
# EXAMPLE:
      # NUMS = [1,2,3,4,5]
      # TARGET = 9
      # PAIR = (4,5)
# APPROACH 1 (BRUTE FORCE):
      # USE NESTED LOOPS
      # CHECK EVERY POSSIBLE PAIR
      # RETURN FIRST MATCH
# APPROACH 2 (HASH SET):
      # STORE VISITED NUMBERS
      # FIND COMPLEMENT
      # IF COMPLEMENT EXISTS
      # RETURN PAIR
# APPROACH 3 (TWO POINTER):
      # WORKS FOR SORTED ARRAY
      # LEFT + RIGHT
      # MOVE POINTERS ACCORDINGLY
      # RETURN PAIR
# APPROACH 4 (RETURN ALL PAIRS):
      # STORE ALL VALID PAIRS
      # RETURN LIST OF PAIRS
# TIME COMPLEXITY:
      # BRUTE FORCE      -> O(N²)
      # HASH SET         -> O(N)
      # TWO POINTER      -> O(N)
# SPACE COMPLEXITY:
      # BRUTE FORCE      -> O(1)
      # HASH SET         -> O(N)
      # TWO POINTER      -> O(1)
# CONCLUSION:
      # BETTER SOLUTION
            # HASH SET
      # OPTIMAL FOR SORTED ARRAY
            # TWO POINTER
      # MOST INTERVIEWERS EXPECT
            # HASH SET

#BRUTE FORCE NESTED LOOP METHOD
def find_pair(nums,target):
    #EDGE CASE
    if not nums:
        return []
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            #CHECK IF CURRENT PAIR FORM TARGET
            if nums[i]+nums[j]==target:
                return (nums[i],nums[j])
    return None
nums=[1,2,3,4,5]
target=9
print(find_pair(nums,target))

#USING HASH SET METHOD
def find_pair(nums,target):
    #EDGE CASE
    if not nums:
        return []
    n=len(nums)
    seen=set()
    for num in nums:
        complement=target-num
        #PAIR FOUND
        if complement in seen:
            return (complement,num)
        seen.add(num)
    return None
nums=[1,2,3,4,5]
target=9
print(find_pair(nums,target))

#USING TWO POINTER METHOD
def find_pair(nums,target):
    #EDGE CASE
    if not nums:
        return []
    left=0
    right=len(nums)-1
    while left<right:
        current_sum=nums[left]+nums[right]
        if current_sum==target:
            return (nums[left],nums[right])
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return None
nums=[1,2,3,4,5]
target=9
print(find_pair(nums,target))

#RETURN ALL PAIRS
def find_pair(nums,target):
    #EDGE CASE
    if not nums:
        return []
    n=len(nums)
    seen=set()
    pairs=[]
    for num in nums:
        complement=target-num
        if complement in seen:
            pairs.append((complement,num))
        seen.add(num)
    return pairs
nums=[1,2,3,4,5,5,4,5,4]
target=9
print(find_pair(nums,target))