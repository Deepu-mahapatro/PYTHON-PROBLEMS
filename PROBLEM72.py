#SECOND SMALLEST ELEMENT
#CORE IDEA:
      #FIND THE SECOND SMALLEST DISTINCT ELEMENT
      #NOT THE SECOND OCCURRENCE
      #TRACK OR IDENTIFY THE ELEMENT
      #JUST GREATER THAN THE SMALLEST
#EDGE CASES:
      #EMPTY ARRAY -> SECOND SMALLEST DOES NOT EXIST
      #ONE ELEMENT -> SECOND SMALLEST DOES NOT EXIST
      #ALL ELEMENTS SAME -> SECOND SMALLEST DOES NOT EXIST
      #DUPLICATES OF SMALLEST -> IGNORE DUPLICATES
      #NEGATIVE NUMBERS -> HANDLE NORMALLY
#KEY OBSERVATION:
      #SECOND SMALLEST MUST BE DISTINCT
      #IT MUST BE GREATER THAN THE SMALLEST
      #AND SMALLER THAN ALL REMAINING ELEMENTS
#EXAMPLE:
      #ARRAY = [10, 40, 30, 20]
      #SMALLEST = 10
      #SECOND SMALLEST = 20
#APPROACH 1 (SORTING):
      #SORT THE ARRAY
      #SMALLEST WILL BE AT FIRST INDEX
      #TRAVERSE FORWARD
      #FIND FIRST ELEMENT DIFFERENT
      #FROM SMALLEST
      #THAT ELEMENT IS SECOND SMALLEST
#APPROACH 2 (TWO VARIABLE METHOD):
      #INITIALIZE SMALLEST = INF
      #INITIALIZE SECOND = INF
      #TRAVERSE ARRAY
      #IF CURRENT < SMALLEST
            #SECOND = SMALLEST
            #SMALLEST = CURRENT
      #ELSE IF CURRENT IS BETWEEN
      #SMALLEST AND SECOND
            #SECOND = CURRENT
#APPROACH 3 (SET METHOD):
      #REMOVE DUPLICATES USING SET
      #SORT UNIQUE ELEMENTS
      #SECOND ELEMENT
      #IS SECOND SMALLEST
#APPROACH 4 (MIN METHOD):
      #FIND SMALLEST USING MIN()
      #IGNORE ALL OCCURRENCES OF SMALLEST
      #FIND MIN OF REMAINING ELEMENTS
#APPROACH 5 (TWO PASS METHOD):
      #FIRST PASS -> FIND SMALLEST
      #SECOND PASS -> FIND SMALLEST ELEMENT
      #GREATER THAN THE SMALLEST
#TIME COMPLEXITY:
      #SORTING METHOD      -> O(N LOG N)
      #TWO VARIABLE METHOD -> O(N)
      #SET METHOD          -> O(N LOG N)
      #MIN METHOD          -> O(N)
      #TWO PASS METHOD     -> O(N)
#SPACE COMPLEXITY:
      #SORTING METHOD      -> O(1)
      #TWO VARIABLE METHOD -> O(1)
      #SET METHOD          -> O(N)
      #MIN METHOD          -> O(N)
      #TWO PASS METHOD     -> O(1)
#CONCLUSION:
      #THE OPTIMAL SOLUTION
      #IS THE TWO VARIABLE METHOD
      #IT FINDS THE SECOND SMALLEST
      #IN A SINGLE TRAVERSAL
      #WITH O(N) TIME
      #AND O(1) SPACE
      
#SORTING METHOD
nums = [40,20,10,30,60]
#EDGE CASE
if len(nums) < 2:
    print("SECOND SMALLEST ELEMENT DOES NOT EXIST")
else:
    nums.sort()
    smallest = nums[0]
    second_smallest = None
    for i in range(1, len(nums)):
        #FIRST DISTINCT ELEMENT
        if nums[i] != smallest:
            second_smallest = nums[i]
            break
    if second_smallest is None:
        print("SECOND SMALLEST DOES NOT EXIST")
    else:
        print(second_smallest)
        
#TWO VARIABLE METHOD
nums = [10,30,60,20,4]
#EDGE CASE
if len(nums) < 2:
    print("SECOND SMALLEST ELEMENT DOES NOT EXIST")
else:
    smallest = float('inf')
    second = float('inf')
    for num in nums:
        #NEW SMALLEST FOUND
        if num < smallest:
            second = smallest
            smallest = num
        #UPDATE SECOND SMALLEST
        elif smallest < num < second:
            second = num
    if second == float('inf'):
        print("SECOND SMALLEST DOES NOT EXIST")
    else:
        print(second)
        
#USING SET METHOD
nums = [10,40,30,20]
unique = list(set(nums))
if len(unique) < 2:
    print("SECOND SMALLEST ELEMENT DOES NOT EXIST")
else:
    unique.sort()
    print(unique[1])
    
#USING BUILT IN MIN() METHOD
nums = [10,40,30,20]
if len(nums) < 2:
    print("SECOND SMALLEST ELEMENT DOES NOT EXIST")
else:
    smallest = min(nums)
    second = []
    for num in nums:
        if num != smallest:
            second.append(num)
    if not second:
        print("SECOND SMALLEST ELEMENT DOES NOT EXIST")
    else:
        print(min(second))
        
#USING TWO PASS METHOD
nums = [10,40,30,20]
if len(nums) < 2:
    print("SECOND SMALLEST ELEMENT DOES NOT EXIST")
else:
    smallest = min(nums)
    second = float('inf')
    for num in nums:
        if num != smallest and num < second:
            second = num
    if second == float('inf'):
        print("SECOND SMALLEST ELEMENT DOES NOT EXIST")
    else:
        print(second)
        