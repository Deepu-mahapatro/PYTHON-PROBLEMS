#SECOND LARGEST ELEMENT
#CORE IDEA:
      #FIND THE SECOND BIGGEST DISTINCT ELEMENT
      #NOT THE SECOND OCCURRENCE
      #TRACK OR IDENTIFY THE ELEMENT
      #JUST SMALLER THAN THE LARGEST
#EDGE CASES:
      #EMPTY ARRAY -> SECOND LARGEST DOES NOT EXIST
      #ONE ELEMENT -> SECOND LARGEST DOES NOT EXIST
      #ALL ELEMENTS SAME -> SECOND LARGEST DOES NOT EXIST
      #DUPLICATES OF LARGEST -> IGNORE DUPLICATES
      #NEGATIVE NUMBERS -> HANDLE NORMALLY
#KEY OBSERVATION:
      #SECOND LARGEST MUST BE DISTINCT
      #IT MUST BE SMALLER THAN THE LARGEST
      #AND GREATER THAN ALL REMAINING ELEMENTS
#EXAMPLE:
      #ARRAY = [10, 40, 30, 20]
      #LARGEST = 40
      #SECOND LARGEST = 30
#APPROACH 1 (SORTING):
      #SORT THE ARRAY
      #LARGEST WILL BE AT LAST INDEX
      #TRAVERSE BACKWARDS
      #FIND FIRST ELEMENT DIFFERENT
      #FROM LARGEST
      #THAT ELEMENT IS SECOND LARGEST
#APPROACH 2 (TWO VARIABLE METHOD):
      #INITIALIZE LARGEST = -INF
      #INITIALIZE SECOND = -INF
      #TRAVERSE ARRAY
      #IF CURRENT > LARGEST
            #SECOND = LARGEST
            #LARGEST = CURRENT
      #ELSE IF CURRENT IS BETWEEN
      #LARGEST AND SECOND
            #SECOND = CURRENT
#APPROACH 3 (SET METHOD):
      #REMOVE DUPLICATES USING SET
      #SORT UNIQUE ELEMENTS
      #SECOND LAST ELEMENT
      #IS SECOND LARGEST
#APPROACH 4 (MAX METHOD):
      #FIND LARGEST USING MAX()
      #IGNORE ALL OCCURRENCES OF LARGEST
      #FIND MAX OF REMAINING ELEMENTS
#APPROACH 5 (TWO PASS METHOD):
      #FIRST PASS -> FIND LARGEST
      #SECOND PASS -> FIND LARGEST ELEMENT
      #SMALLER THAN THE LARGEST
#TIME COMPLEXITY:
      #SORTING METHOD      -> O(N LOG N)
      #TWO VARIABLE METHOD -> O(N)
      #SET METHOD          -> O(N LOG N)
      #MAX METHOD          -> O(N)
      #TWO PASS METHOD     -> O(N)
#SPACE COMPLEXITY:
      #SORTING METHOD      -> O(1)
      #TWO VARIABLE METHOD -> O(1)
      #SET METHOD          -> O(N)
      #MAX METHOD          -> O(N)
      #TWO PASS METHOD     -> O(1)
#CONCLUSION:
      #THE OPTIMAL SOLUTION
      #IS THE TWO VARIABLE METHOD
      #IT FINDS THE SECOND LARGEST
      #IN A SINGLE TRAVERSAL
      #WITH O(N) TIME
      #AND O(1) SPACE


#A SORTING METHOD
nums=[40,20,10,30,60]
#EDGE CASE
if len(nums)<2:
    print("SECOND LARGEST ELEMENT IS NOT EXISTS")
else:
    nums.sort()
    largest=nums[-1]
    second_largest=None
    for i in range(len(nums)-2,-1,-1):
        #FIRST DISTINCT ELEMENT
        if nums[i]!=largest:
            second_largest=nums[i]
            break
    if second_largest is None:
        print("SECOND LARGEST IS NOT EXISTS")
    else:
        print(second_largest)
        
#TWO VARIABLE METHOD
nums=[10,30,60,20,40]
#EDGE CASE
if len(nums)<2:
    print("SECOND LARGEST ELEMENT IS NOT EXISTS")
else:
    largest=float('-inf')
    second=float('-inf')
    for num in nums:
        #NEW LARGEST FOUND
        if num>largest:
            second=largest
            largest=num
        #UPDATE SECOND LARGEST
        elif largest>num>second:
            second=num
    if second==float('-inf'):
        print("SECOND LARGEST IS NOT EXISTS")
    else:
        print(second)
        
#USING SET METHOD
nums=[10,40,30,20]
unique=list(set(nums))
if len(unique)<2:
    print("SECOND LARGEST ELEMENT IS NOT EXISTS")
else:
    unique.sort()
    print(unique[-2])
    
#USING BUILT IN MAX() METHOD
nums=[10,40,30,20]
if len(nums)<2:
    print("SECOND LARGEST ELEMENT IS NOT EXISTS")
else:
    largest=max(nums)
    second=[]
    for num in nums:
        if num!=largest:
            second.append(num)
    if not second:
        print("SECOND LARGEST ELEMENT IS NOT EXISTS")
    else:
        print(max(second))

#USING TWO PASS METHOD
nums=[10,40,30,20]
if len(nums)<2:
    print("SECOND LARGEST ELEMENT IS NOT EXISTS")
else:
    largest=max(nums)
    second=float('-inf')
    for num in nums:
        if num!=largest and num>second:
            second=num
    if second==float('-inf'):
        print("SECOND LARGEST ELEMENT IS NOT EXISTS")
    else: print(second)