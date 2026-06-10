# ROTATE ARRAY BY K POSITIONS
# CORE IDEA:
      # SHIFT ELEMENTS LEFT OR RIGHT
      # BY K POSITIONS
      # ARRAY BEHAVES CIRCULARLY
      # ELEMENTS MOVING OUT OF ONE SIDE
      # REAPPEAR ON THE OTHER SIDE
# EDGE CASES:
      # EMPTY ARRAY -> RETURN EMPTY ARRAY
      # SINGLE ELEMENT -> NO CHANGE
      # K = 0 -> NO ROTATION
      # K > N -> USE K % N
      # K = N -> SAME ARRAY
      # NEGATIVE VALUES -> HANDLE NORMALLY
# KEY OBSERVATION:
      # AFTER N ROTATIONS
      # ARRAY RETURNS TO ORIGINAL FORM
      # THEREFORE
      # K = K % N
      # REDUCES UNNECESSARY WORK
# EXAMPLE:
      # ARRAY = [1,2,3,4,5]
      # K = 2
      # RIGHT ROTATION
      # [4,5,1,2,3]
      # LEFT ROTATION
      # [3,4,5,1,2]
# APPROACH 1 (BRUTE FORCE):
      # RIGHT ROTATION
            # TAKE LAST ELEMENT
            # INSERT AT FRONT
            # REPEAT K TIMES
      # LEFT ROTATION
            # TAKE FIRST ELEMENT
            # APPEND AT END
            # REPEAT K TIMES
# APPROACH 2 (SLICING METHOD):
      # RIGHT ROTATION
            # ARR[-K:] + ARR[:-K]
      # LEFT ROTATION
            # ARR[K:] + ARR[:K]
      # PYTHONIC SOLUTION
      # EASY TO REMEMBER
# APPROACH 3 (REVERSAL ALGORITHM):
      # RIGHT ROTATION
            # REVERSE WHOLE ARRAY
            # REVERSE FIRST K ELEMENTS
            # REVERSE REMAINING ELEMENTS
      # LEFT ROTATION
            # REVERSE FIRST K ELEMENTS
            # REVERSE REMAINING ELEMENTS
            # REVERSE WHOLE ARRAY
      # IN-PLACE SOLUTION
# APPROACH 4 (EXTRA ARRAY METHOD):
      # CREATE TEMP ARRAY
      # RIGHT ROTATION
            # NEW INDEX = (I + K) % N
      # LEFT ROTATION
            # NEW INDEX = (I - K) % N
      # PLACE ELEMENTS
      # IN THEIR FINAL POSITION
# TIME COMPLEXITY:
      # BRUTE FORCE         -> O(N × K)
      # SLICING METHOD      -> O(N)
      # REVERSAL ALGORITHM  -> O(N)
      # EXTRA ARRAY METHOD  -> O(N)
# SPACE COMPLEXITY:
      # BRUTE FORCE         -> O(1)
      # SLICING METHOD      -> O(N)
      # REVERSAL ALGORITHM  -> O(1)
      # EXTRA ARRAY METHOD  -> O(N)
# CONCLUSION:
      # EASIEST METHOD
            # SLICING
      # BEST INTERVIEW METHOD
            # REVERSAL ALGORITHM
      # BEST FOR UNDERSTANDING
            # EXTRA ARRAY METHOD
      # BRUTE FORCE
            # GOOD STARTING POINT
            # BUT NOT OPTIMAL

#BRUTE FORCE (RIGHT ROTATION)
nums=[1,2,3,4,5]
k=2
n=len(nums)
k=k%n
for _ in range(k):
    last=nums.pop()
    nums.insert(0,last)
print(nums)

#BRUTE FORCE (LEFT ROTATION)
nums=[1,2,3,4,5]
n=len(nums)
k=2
k=k%n
for _ in range(k):
    first=nums.pop()
    nums.append(first)
print(nums)



#USING SLICING METHOD(RIGHT ROTATION)
nums=[1,2,3,4,5]
k=2
n=len(nums)
k=k%n
nums=nums[-k:]+nums[:-k]
print(nums)

#USING SLICING METHOD(LEFT ROTATION)
nums=[1,2,3,4,5]
k=2
n=len(nums)
k=k%n
nums=nums[k:]+nums[:k]
print(nums)

#REVERSAL ALGORITHM (RIGHT ROTATION)
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
arr=[1,2,3,4,5]
k=2
n=len(arr)
k=k%n
reverse(arr,0,n-1)
reverse(arr,0,k-1)
reverse(arr,k,n-1)
print(arr)

#REVERSAL ALGORITHM (LEFT ROTATION)
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
arr=[1,2,3,4,5]
k=2
n=len(arr)
k=k%n
reverse(arr,0,k-1)
reverse(arr,k,n-1)
reverse(arr,0,n-1)
print(arr)

#USING EXTRA ARRAY METHOD (RIGHT ROTATION)
nums=[1,2,3,4,5]
n=len(nums)
k=2
k=k%n
temp=[0]*n
for i in range(n):
    temp[(i+k)%n]=nums[i]
print(temp)

#USING EXTRA ARRAY METHOD (LEFT ROTATION)
nums=[1,2,3,4,5]
k=2
n=len(nums)
k=k%n
temp=[0]*n
for i in range(n):
    temp[(i-k)%n]=nums[i]
print(temp)