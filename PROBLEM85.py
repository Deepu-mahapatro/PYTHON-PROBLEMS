# FIND MAJORITY ELEMENT (> N/2 TIMES)
# CORE IDEA:
      # FIND ELEMENT
      # APPEARING MORE THAN N/2 TIMES
      # RETURN THAT ELEMENT
# EDGE CASES:
      # EMPTY ARRAY
      # SINGLE ELEMENT
      # NO MAJORITY ELEMENT
      # ALL ELEMENTS SAME
      # NEGATIVE NUMBERS
      # DUPLICATE VALUES
      # LARGE ARRAY
# KEY OBSERVATION:
      # MAJORITY ELEMENT
      # OCCURS MORE THAN N/2 TIMES
      # ONLY ONE MAJORITY ELEMENT
      # CAN EXIST
# EXAMPLE:
      # NUMS = [1,1,2,2,2]
      # N = 5
      # N/2 = 2
      # COUNT(2) = 3
      # ANSWER = 2
# APPROACH 1 (BRUTE FORCE):
      # CHECK COUNT
      # OF EVERY ELEMENT
      # RETURN ELEMENT
      # IF COUNT > N/2
# APPROACH 2 (HASH MAP):
      # STORE FREQUENCY
      # OF EACH ELEMENT
      # RETURN ELEMENT
      # WHOSE COUNT > N/2
# APPROACH 3 (SORTING):
      # SORT ARRAY
      # MAJORITY ELEMENT
      # MUST BE AT MIDDLE INDEX
      # VERIFY FREQUENCY
# APPROACH 4 (BOYER MOORE):
      # FIND CANDIDATE
      # USING VOTING PROCESS
      # RETURN CANDIDATE
      # IF MAJORITY GUARANTEED
# APPROACH 5 (BOYER MOORE + VERIFICATION):
      # FIND CANDIDATE
      # COUNT FREQUENCY AGAIN
      # VERIFY MAJORITY EXISTS
# DRY RUN (BOYER MOORE):
      # NUMS = [1,1,2,2,2]
      # CANDIDATE = 1 COUNT = 1
      # CANDIDATE = 1 COUNT = 2
      # CANDIDATE = 1 COUNT = 1
      # CANDIDATE = 1 COUNT = 0
      # CANDIDATE = 2 COUNT = 1
      # ANSWER = 2
# TIME COMPLEXITY:
      # BRUTE FORCE            -> O(N²)
      # HASH MAP               -> O(N)
      # SORTING                -> O(N LOG N)
      # BOYER MOORE            -> O(N)
      # BOYER MOORE VERIFY     -> O(N)
# SPACE COMPLEXITY:
      # BRUTE FORCE            -> O(1)
      # HASH MAP               -> O(N)
      # SORTING                -> O(1)
      # BOYER MOORE            -> O(1)
      # BOYER MOORE VERIFY     -> O(1
# CONCLUSION:
      # BETTER SOLUTION
            # HASH MAP
      # OPTIMAL SOLUTION
            # BOYER MOORE
      # IF MAJORITY GUARANTEED
            # BOYER MOORE
      # IF MAJORITY NOT GUARANTEED
            # BOYER MOORE + VERIFICATION
      # MOST INTERVIEWERS EXPECT
            # BOYER MOORE VOTING ALGORITHM

#BRUTE FORCE APPROACH
def majority_element(nums):
    #EDGE CASE
    if not nums:
        return []
    n=len(nums)
    for num in nums:
        count=0
        #COUNT FREQUENCY 
        for value in nums:
            if value==num:
                count+=1
        #MAJORITY ELEMENT FOUND
        if count>n//2:
            return num
    return None
nums=[1,1,2,2,2]
print(majority_element(nums))

#USING HASH MAP METHOD
def majority_element(nums):
    #EDGE CASE
    if not nums:
        return []
    freq={}
    for num in nums:
        #INCREASE COUNT
        freq[num]=freq.get(num,0)+1
        #MAJORITY ELEMENT FOUND
        if freq[num]>len(nums)//2:
            return num
    return None
nums=[1,1,2,2,2]
print(majority_element(nums))   

#USING SORTING METHOD
def majority_element(nums):
    #EDGE CASE
    if not nums:
        return []
    nums.sort()
    #MIDDLE ELEMENT
    candidate=nums[len(nums)//2]
    count=0
    for num in nums:
        if num==candidate:
            count+=1
        if count>len(nums)//2:
            return candidate
    return None
nums=[1,1,2,2,2]
print(majority_element(nums))

#BOYER MOORE VOTING METHOD(IF MAJORITY EXISTS)
def majority_element(nums):
    #EDGE CASE
    if not nums:
        return []
    candidate=None
    count=0
    #FIND CANDIDATE
    for num in nums:
        if count==0:
            candidate=num
        if num==candidate:
            count+=1
        else:
            count-=1
    return candidate
nums=[1,1,2,2,2]
print(majority_element(nums))

#BOYER MOORE VOTING METHOD(IF MAJORITY NOT  EXISTS)
def majority_element(nums):
    #EDGE CASE
    if not nums:
        return []
    candidate=None
    count=0
    #FIND CANDIDATE
    for num in nums:
        if count==0:
            candidate=num
        if num==candidate:
            count+=1
        else:
            count-=1
    freq=0
    for num in nums:
        if num==candidate:
            freq+=1
    if freq>len(nums)//2:
        return candidate
    return None
nums=[1,2,3,4,5]
print(majority_element(nums))