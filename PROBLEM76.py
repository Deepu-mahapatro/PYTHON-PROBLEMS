# COUNT FREQUENCY OF EACH ELEMENT
# CORE IDEA:
      # COUNT OCCURRENCES
      # OF EVERY ELEMENT
      # STORE COUNT
      # FOR EACH ELEMENT
# EDGE CASES:
      # EMPTY ARRAY
      # SINGLE ELEMENT
      # ALL ELEMENTS SAME
      # ALL ELEMENTS UNIQUE
      # NEGATIVE NUMBERS
      # STRING ELEMENTS
# KEY OBSERVATION:
      # SAME ELEMENT
      # MAY APPEAR MULTIPLE TIMES
      # NEED TO TRACK
      # OCCURRENCE COUNT
      # ELEMENT -> COUNT
# APPROACH 1 (BRUTE FORCE):
      # PICK EACH ELEMENT
      # SCAN ENTIRE ARRAY
      # COUNT OCCURRENCES
      # STORE RESULT
# APPROACH 2 (SORTING):
      # SORT ARRAY
      # SAME ELEMENTS
      # BECOME ADJACENT
      # COUNT CONSECUTIVE ELEMENTS
      # STORE FREQUENCY
# APPROACH 3 (HASH MAP):
      # CREATE DICTIONARY
      # TRAVERSE ARRAY
      # INCREMENT COUNT
      # FOR EACH ELEMENT
# APPROACH 4 (GET METHOD):
      # USE GET()
      # FETCH CURRENT COUNT
      # ADD 1
      # STORE UPDATED COUNT
# APPROACH 5 (DEFAULTDICT):
      # CREATE DEFAULTDICT(INT)
      # MISSING KEYS
      # GET DEFAULT 0
      # DIRECTLY INCREMENT COUNT
# APPROACH 6 (COUNTER):
      # USE COUNTER()
      # AUTOMATICALLY COUNT
      # ALL ELEMENT FREQUENCIES
# TIME COMPLEXITY:
      # BRUTE FORCE      -> O(N²)
      # SORTING          -> O(N LOG N)
      # HASH MAP         -> O(N)
      # GET METHOD       -> O(N)
      # DEFAULTDICT      -> O(N)
      # COUNTER          -> O(N)
# SPACE COMPLEXITY:
      # BRUTE FORCE      -> O(N)
      # SORTING          -> O(N)
      # HASH MAP         -> O(N)
      # GET METHOD       -> O(N)
      # DEFAULTDICT      -> O(N)
      # COUNTER          -> O(N)
# CONCLUSION:
      # BETTER SOLUTION
            # HASH MAP
      # OPTIMAL SOLUTION
            # HASH MAP
      # PYTHONIC SOLUTION
            # COUNTER
      # MOST INTERVIEWERS EXPECT
            # HASH MAP APPROACH

#USING BRUTE FORCE APPROACH
def count_frequency(arr):
    freq={}
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        freq[arr[i]]=count
    return freq
arr=[1,2,3,4,1,2,3,4]
print(count_frequency(arr))


#USING DICTIONARY METHOD
def count_frequency(arr):
    #EDGE CASE
    if not arr:
        return []
    freq={}
    for i in arr:
        #IF ELEMENT EXISTS,INCREMENT THE COUNT
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
arr=[1,2,3,4,1,2,3,4]
print(count_frequency(arr))


#USING GET+DICTIONARY METHOD
def count_frequency(arr):
    #EDGE CASE
    if not arr:
        return []
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1
    return freq
arr=[1,2,3,4,1,2,3,4]
print(count_frequency(arr))


#USING COUNTER METHOD
from collections import Counter
arr=[1,2,3,4,1,2,3,4]
freq=Counter(arr)
print(freq)

#USING DEFAULT DICT METHOD
from collections import defaultdict
def count_frequency(arr):
    freq=defaultdict(int)
    for i in arr:
        freq[i]+=1
    return dict(freq)
arr=[1,2,3,4,1,2,3,4]
print(count_frequency(arr))