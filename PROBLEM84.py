# REVERSE A LIST (WITHOUT USING BUILT IN)
# CORE IDEA:
      # REVERSE THE ORDER OF ELEMENTS
      # LAST ELEMENT BECOMES FIRST
      # FIRST ELEMENT BECOMES LAST
# EDGE CASES:
      # EMPTY LIST
      # SINGLE ELEMENT
      # DUPLICATE VALUES
      # NEGATIVE NUMBERS
      # MIXED DATA TYPES
      # LARGE LIST
# KEY OBSERVATION:
      # ELEMENTS CAN BE READ
      # FROM END TO START
      # OR SWAPPED FROM BOTH ENDS
      # UNTIL POINTERS MEET
# EXAMPLE:
      # NUMS = [1,2,3,4,5]
      # OUTPUT = [5,4,3,2,1]
# APPROACH 1 (BRUTE FORCE):
      # START FROM LAST INDEX
      # TRAVERSE TOWARDS FIRST INDEX
      # APPEND ELEMENTS TO NEW LIST
# APPROACH 2 (TWO POINTER):
      # PLACE POINTERS
      # AT START AND END
      # SWAP ELEMENTS
      # MOVE TOWARDS CENTER
# APPROACH 3 (RECURSION):
      # TAKE LAST ELEMENT
      # RECURSIVELY REVERSE REMAINING LIST
      # COMBINE RESULTS
# APPROACH 4 (INSERT AT BEGINNING):
      # TRAVERSE LIST
      # INSERT EACH ELEMENT
      # AT INDEX 0
# APPROACH 5 (MANUAL SWAPPING):
      # USE TEMP VARIABLE
      # SWAP LEFT AND RIGHT ELEMENTS
      # MOVE POINTERS TOWARDS CENTER
# TIME COMPLEXITY:
      # BRUTE FORCE         -> O(N)
      # TWO POINTER         -> O(N)
      # RECURSION           -> O(N)
      # INSERT AT BEGINNING -> O(N²)
      # MANUAL SWAPPING     -> O(N)
# SPACE COMPLEXITY:
      # BRUTE FORCE         -> O(N)
      # TWO POINTER         -> O(1)
      # RECURSION           -> O(N)
      # INSERT AT BEGINNING -> O(N)
      # MANUAL SWAPPING     -> O(1)
# CONCLUSION:
      # BETTER SOLUTION
            # TWO POINTER
      # OPTIMAL SOLUTION
            # TWO POINTER
      # ADVANCED SOLUTION
            # RECURSION
      # MOST INTERVIEWERS EXPECT
            # TWO POINTER

#BRUTE FORCE METHOD
def reverse_list(nums):
    #EDGE CASE
    if not nums:
        return []
    result=[]
    #START FROM LAST INDEX
    for i in range(len(nums)-1,-1,-1):
        result.append(nums[i])
    return result
nums=[1,2,3,4,5]
print(reverse_list(nums))

#USING TWO POINTER METHOD
def reverse_list(nums):
    #EDGE CASE
    if not nums:
        return []
    left=0
    right=len(nums)-1
    while left<right:
        #SWAP ELEMENTS
        nums[left],nums[right]=nums[right],nums[left]
        #MOVE POINTERS
        left+=1
        right-=1
    return nums
nums=[1,2,3,4,5]
print(reverse_list(nums))

#USING RECURSION METHOD
def reverse_list(nums):
    #BASE CASE
    if len(nums)<=1:
        return nums
    return [nums[-1]] + reverse_list(nums[:-1])
nums=[1,2,3,4,5]
print(reverse_list(nums))

#INSERT AT BEGINNING 
def reverse_list(nums):
    #EDGE CASE
    if not nums:
        return []
    result=[]
    for num in nums:
        result.insert(0,num)
    return result
nums=[1,2,3,4,5]
print(reverse_list(nums))

#MANUAL SWAPPING METHOD
def reverse_list(nums):
    #EDGE CASE
    if not nums:
        return []
    left=0
    right=len(nums)-1
    while left<right:
        temp=nums[left]
        nums[left]=nums[right]
        nums[right]=temp
        left+=1
        right-=1
    return nums
nums=[1,2,3,4,5]
print(reverse_list(nums))