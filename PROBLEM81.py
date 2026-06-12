# MOVE ALL ZEROS TO THE END
# CORE IDEA:
      # MOVE ALL ZEROS TO THE END
      # MAINTAIN RELATIVE ORDER OF NON-ZERO ELEMENTS
      # RETURN MODIFIED ARRAY
# EDGE CASES:
      # EMPTY ARRAY
      # SINGLE ELEMENT ARRAY
      # ALL ZEROS
      # NO ZEROS PRESENT
      # ZEROS AT START
      # ZEROS AT END
      # ZEROS IN MIDDLE
      # NEGATIVE NUMBERS
      # DUPLICATE VALUES
# KEY OBSERVATION:
      # NON-ZERO ELEMENTS MUST KEEP THEIR ORDER
      # ZEROS SHOULD BE MOVED TO THE BACK
      # EXTRA ARRAY CAN BE USED
      # TWO POINTERS CAN SOLVE IN-PLACE
      # COUNT METHOD REDUCES SWAPS
# EXAMPLE:
      # NUMS = [0,1,0,3,12]
      # NON-ZEROS = [1,3,12]
      # ZEROS = [0,0]
      # RESULT = [1,3,12,0,0]
# APPROACH 1 (BRUTE FORCE METHOD):
      # STORE NON-ZERO ELEMENTS
      # STORE ZERO ELEMENTS
      # COMBINE BOTH ARRAYS
# APPROACH 2 (TWO POINTER METHOD):
      # USE LEFT POINTER
      # SCAN ARRAY USING RIGHT POINTER
      # MOVE NON-ZERO ELEMENTS FORWARD
      # ZEROS AUTOMATICALLY MOVE TO END
# APPROACH 3 (SORT METHOD):
      # SORT ARRAY USING CUSTOM KEY
      # TREAT ZEROS AS LARGER VALUES
      # MOVE ZEROS TO END
# APPROACH 4 (COUNT METHOD):
      # PLACE NON-ZERO ELEMENTS AT FRONT
      # TRACK FILLED POSITIONS
      # FILL REMAINING POSITIONS WITH ZEROS
# TIME COMPLEXITY:
      # BRUTE FORCE METHOD    -> O(N)
      # TWO POINTER METHOD    -> O(N)
      # SORT METHOD           -> O(N LOG N)
      # COUNT METHOD          -> O(N)
# SPACE COMPLEXITY:
      # BRUTE FORCE METHOD    -> O(N)
      # TWO POINTER METHOD    -> O(1)
      # SORT METHOD           -> O(1)
      # COUNT METHOD          -> O(1)
# CONCLUSION:
      # SIMPLEST SOLUTION
            # BRUTE FORCE METHOD
      # BRUTE FORCE SOLUTION
            # EXTRA ARRAY APPROACH
      # NOT RECOMMENDED
            # SORT METHOD
      # OPTIMAL SOLUTION
            # COUNT METHOD
      # MOST INTERVIEWERS EXPECT
            # TWO POINTER METHOD O(N), O(1
      # ANOTHER OPTIMAL SOLUTION
            # COUNT METHOD O(N), O(1)

#BRUTE FORCE METHOD
nums=[0,1,0,3,12]
non_zero=[]
zero=[]
for num in nums:
    if num==0:
        zero.append(num)
    else:
        non_zero.append(num)
result=non_zero+zero
print(result)

#USING TWO POINTER METHOD
nums=[0,1,0,3,12]
left=0
for right in range(len(nums)):
    if nums[right]!=0:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
print(nums)

#USING SORT METHOD
nums=[0,1,0,3,12]
nums.sort(key=lambda x : x==0)
print(nums)

#COUNT METHOD
nums=[0,1,0,3,12]
count=0
for num in nums:
    if num!=0:
        nums[count]=num
        count+=1
while count<len(nums):
    nums[count]=0
    count+=1
print(nums)