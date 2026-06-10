# REMOVE DUPLICATES FROM ARRAY/LIST
# CORE IDEA:
      # KEEP ONLY UNIQUE ELEMENTS
      # REMOVE REPEATED VALUES
      # PRESERVE ORDER IF REQUIRED
      # EACH ELEMENT SHOULD APPEAR ONLY ONCE
# EDGE CASES:
      # EMPTY ARRAY -> RETURN EMPTY ARRAY
      # SINGLE ELEMENT -> RETURN SAME ARRAY
      # ALL ELEMENTS SAME -> RETURN ONE ELEMENT
      # NO DUPLICATES -> RETURN ORIGINAL ARRAY
      # NEGATIVE NUMBERS -> HANDLE NORMALLY
      # MIXED VALUES -> HANDLE NORMALLY
# KEY OBSERVATION:
      # DUPLICATES ARE REPEATED VALUES
      # UNIQUE ELEMENTS SHOULD APPEAR ONLY ONCE
      # HASH SET PROVIDES FAST LOOKUP
      # SORTED ARRAYS CAN USE TWO POINTERS
# EXAMPLE:
      # ARRAY = [1, 2, 2, 3, 4, 4, 5]
      # OUTPUT = [1, 2, 3, 4, 5]
# APPROACH 1 (SET METHOD):
      # CONVERT ARRAY TO SET
      # CONVERT BACK TO LIST
      # DUPLICATES REMOVED AUTOMATICALLY
# APPROACH 2 (HASH SET + LOOP):
      # CREATE EMPTY SET
      # CREATE RESULT LIST
      # TRAVERSE ARRAY
      # IF ELEMENT NOT IN SET
            # ADD TO SET
            # ADD TO RESULT
      # PRESERVES ORDER
# APPROACH 3 (DICT.FROMKEYS):
      # CREATE DICTIONARY USING ARRAY
      # DICTIONARY KEYS ARE UNIQUE
      # CONVERT KEYS TO LIST
      # PRESERVES ORDER
# APPROACH 4 (NESTED LOOP):
      # CREATE EMPTY RESULT
      # FOR EACH ELEMENT
      # CHECK IF ALREADY EXISTS
      # IF NOT EXISTS ADD TO RESULT
      # NO EXTRA DATA STRUCTURE
# APPROACH 5 (SORTING):
      # SORT ARRAY
      # TRAVERSE ARRAY
      # KEEP ONLY DISTINCT VALUES
      # ORDER MAY CHANGE
# APPROACH 6 (TWO POINTERS - SORTED ARRAY):
      # ARRAY MUST BE SORTED
      # USE READ POINTER
      # USE WRITE POINTER
      # COPY UNIQUE ELEMENTS FORWARD
      # IN-PLACE SOLUTION
# TIME COMPLEXITY:
      # SET METHOD           -> O(N)
      # HASH SET + LOOP      -> O(N)
      # DICT.FROMKEYS        -> O(N)
      # NESTED LOOP          -> O(N²)
      # SORTING METHOD       -> O(N LOG N)
      # TWO POINTERS         -> O(N)
# SPACE COMPLEXITY:
      # SET METHOD           -> O(N)
      # HASH SET + LOOP      -> O(N)
      # DICT.FROMKEYS        -> O(N)
      # NESTED LOOP          -> O(1)
      # SORTING METHOD       -> O(1)
      # TWO POINTERS         -> O(1)
# CONCLUSION:
      # FOR UNSORTED ARRAY
      # HASH SET + LOOP IS BEST
      # TIME = O(N)
      # SPACE = O(N)
      # FOR SORTED ARRAY
      # TWO POINTER METHOD IS OPTIMAL
      # TIME = O(N)
      # SPACE = O(1)

#USING STE METHOD
nums=[1,2,3,4,5,5]
result=list(set(nums))
print(result)

#USING NESTED LOOP
nums=[1,2,3,4,5,5]
result=[]
for i in nums:
    if i not in result:
        result.append(i)
print(result)

#USING SORTING METHOD
nums=[1,2,3,4,5,5]
nums.sort()
result=[nums[0]]
for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]:
        result.append(nums[i])
print(result)

#USING TWO POINTER METHOD(WHEN ARRAY IS SORTED)
nums=[1,2,3,4,5,5]
left=1
for right in range(1,len(nums)):
    if nums[right]!=nums[right-1]:
        nums[left]=nums[right]
        left+=1
print(nums[:left])

#UNSORTED ARRAY USING HASH SET APPROACH
nums=[1,2,3,4,5,5]
seen=set()
result=[]
for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(num)
print(result)

#USING DICTFROMKEYS METHOD
nums=[1,2,3,4,5,5]
result=list(dict.fromkeys(nums))
print(result)