# FIND ALL PAIRS WHERE XOR EQUALS K
# PROBLEM
# GIVEN AN ARRAY AND A VALUE K
# FIND ALL PAIRS (a, b) SUCH THAT:
# a XOR b = k
# EXAMPLE
# arr = [1, 2, 3, 4, 5]
# k = 7
# OUTPUT:
# [(3,4), (2,5)]
# XOR PROPERTY
# a XOR b = k
# b = a XOR k
# a = b XOR k
# APPROACH 1 (BRUTE FORCE METHOD)
# CHECK EVERY POSSIBLE PAIR
# IF nums[i] XOR nums[j] == k
# STORE THE PAIR
# TIME COMPLEXITY: O(n²)
# SPACE COMPLEXITY: O(1) [EXCLUDING OUTPUT]
# INTERVIEW VALUE: BASIC APPROACH
# APPROACH 2 (HASH SET + XOR METHOD)
# FOR EVERY NUMBER:
# target = num XOR k
# CHECK WHETHER target EXISTS IN SEEN SET
# IF YES, STORE THE PAIR
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
# INTERVIEW VALUE: MOST RECOMMENDED
# APPROACH 3 (DICTIONARY METHOD)
# USE HASHMAP INSTEAD OF SET
# STORE PREVIOUSLY SEEN NUMBERS
# CHECK target = num XOR k
# IF target EXISTS, STORE THE PAIR
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
# INTERVIEW VALUE: GOOD HASHING PRACTICE
# APPROACH 4 (XOR FREQUENCY METHOD)
# USE FREQUENCY MAP
# COUNT NUMBER OF VALID PAIRS
# HANDLE DUPLICATES PROPERLY
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
# INTERVIEW VALUE: BEST FOR COUNTING PAIRS
# FORMULA
# target = num XOR k
# IF target EXISTS:
# num XOR target = k
# EXAMPLE
# num = 4
# k = 7
# target = 4 XOR 7 = 3
# 4 XOR 3 = 7
# EDGE CASES
# [] , k=5
# OUTPUT: []
# [5], k=5
# OUTPUT: []
# [1,1,1,1], k=0
# OUTPUT: 6 PAIR
# [2,5], k=7
# OUTPUT: [(2,5)]
# [1,2,3,4,5], k=7
# OUTPUT: [(3,4), (2,5)]
# IMPORTANT POINTS
# XOR OF SAME NUMBERS IS 0
# x XOR x = 0
# XOR WITH 0 RETURNS SAME NUMBER
# x XOR 0 = x
# XOR IS COMMUTATIVE
# a XOR b = b XOR 
# XOR IS ASSOCIATIVE
# (a XOR b) XOR c = a XOR (b XOR c)
# CONCLUSION
# BEST APPROACH FOR FINDING PAIRS:
# HASH SET + XOR METHOD
# BEST APPROACH FOR COUNTING PAIRS:
# XOR FREQUENCY METHOD
# BEST TIME COMPLEXITY:
# O(n)
# BEST SPACE COMPLEXITY:
# O(n)

#BRUTE FORCE METHOD
def find_pairs(nums,k):
    pairs=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]^nums[j])==k:
                pairs.append((nums[i],nums[j]))
    return pairs
nums=[1,2,3,4,5]
k=7
print(find_pairs(nums,k))

#USING HASH SET + XOR METHOD
def find_pairs(nums,k):
    seen=set()
    pairs=[]
    for num in nums:
        target=num^k 
        if target in seen:
            pairs.append((target,num))
        seen.add(num)
    return pairs
nums=[1,2,3,4,5]
k=7
print(find_pairs(nums,k))

#XOR FREQUENCY METHOD
def find_pairs(nums,k):
    freq={}
    count=0
    for num in nums:
        target=num^k
        count+=freq.get(target,0)
        freq[num]=freq.get(num,0)+1
    return count
nums=[1,2,3,4,5]
target=7
print(find_pairs(nums,k))

#USING DICTIONARY METHOD
def find_pairs(nums,k):
    mp={}
    pairs=[]
    for num in nums:
        target=num^k
        if target in mp:
            pairs.append((target,num))
        mp[num]=1
    return pairs
nums=[1,2,3,4,5]
k=7
print(find_pairs(nums,k))