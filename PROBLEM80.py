# FIND UNIQUE ELEMENTS FROM TWO LISTS
# CORE IDEA:
      # TWO LISTS ARE GIVEN
      # FIND ELEMENTS THAT APPEAR IN ONLY ONE LIST
      # EXCLUDE COMMON ELEMENTS
      # RETURN UNIQUE ELEMENTS
# EDGE CASES:
      # BOTH LISTS EMPTY
      # ONE LIST EMPTY
      # ALL ELEMENTS COMMON
      # NO COMMON ELEMENTS
      # DUPLICATE VALUES
      # NEGATIVE NUMBERS
      # UNSORTED LISTS
      # STRING VALUES
# KEY OBSERVATION:
      # UNIQUE ELEMENTS EXIST IN ONLY ONE LIST
      # COMMON ELEMENTS MUST BE REMOVED
      # SET OPERATIONS MAKE THIS EFFICIENT
      # SYMMETRIC DIFFERENCE DIRECTLY RETURNS UNIQUE ELEMENTS
# EXAMPLE:
      # LIST1 = [1,2,3,4]
      # LIST2 = [3,4,5,6]
      # UNIQUE = [1,2,5,6]
# APPROACH 1 (SET SYMMETRIC DIFFERENCE):
      # CONVERT BOTH LISTS TO SETS
      # FIND SYMMETRIC DIFFERENCE USING ^
      # RETURN UNIQUE ELEMENTS
# APPROACH 2 (BRUTE FORCE LOOP):
      # ITERATE THROUGH FIRST LIST
      # STORE ELEMENTS NOT PRESENT IN SECOND LIST
      # ITERATE THROUGH SECOND LIST
      # STORE ELEMENTS NOT PRESENT IN FIRST LIST
# APPROACH 3 (LOOP + HASH SET):
      # CONVERT BOTH LISTS TO SETS
      # CHECK ELEMENTS NOT PRESENT IN OTHER SET
      # STORE UNIQUE ELEMENTS
# APPROACH 4 (TWO POINTER APPROACH):
      # SORT BOTH LISTS
      # USE TWO POINTERS
      # COLLECT NON-MATCHING ELEMENTS
      # SKIP COMMON ELEMENTS
# APPROACH 5 (SYMMETRIC_DIFFERENCE_UPDATE):
      # CONVERT FIRST LIST TO SET
      # APPLY SYMMETRIC_DIFFERENCE_UPDATE()
      # KEEP ONLY UNIQUE ELEMENTS
# APPROACH 6 (FILTER METHOD):
      # FILTER ELEMENTS OF FIRST LIST
      # NOT PRESENT IN SECOND LIST
      # FILTER ELEMENTS OF SECOND LIST
      # NOT PRESENT IN FIRST LIST
      # COMBINE RESULTS
# TIME COMPLEXITY:
      # SET SYMMETRIC DIFFERENCE      -> O(N+M)
      # BRUTE FORCE LOOP             -> O(N*M)
      # LOOP + HASH SET              -> O(N+M)
      # TWO POINTERS                 -> O(N+M)
      # SYMMETRIC_DIFFERENCE_UPDATE  -> O(N+M)
      # FILTER + SET                 -> O(N+M)
# SPACE COMPLEXITY:
      # SET SYMMETRIC DIFFERENCE      -> O(N+M)
      # BRUTE FORCE LOOP             -> O(1)
      # LOOP + HASH SET              -> O(N+M)
      # TWO POINTERS                 -> O(1)
      # SYMMETRIC_DIFFERENCE_UPDATE  -> O(N)
      # FILTER + SET                 -> O(N+M)
# CONCLUSION:
      # SIMPLEST SOLUTION
            # SET SYMMETRIC DIFFERENCE
      # BRUTE FORCE SOLUTION
            # LOOP METHOD
      # BEST FOR SORTED ARRAYS
            # TWO POINTER APPROACH
      # FUNCTIONAL STYLE
            # FILTER METHOD
      # OPTIMAL SOLUTION
            # SET SYMMETRIC DIFFERENCE
      # MOST INTERVIEWERS EXPECT
            # HASH SET APPROACH O(N+M)

# USING SET SYMMETRIC DIFFERENCE
list1 = [1,2,3,4]
list2 = [3,4,5,6]
result = list(set(list1) ^ set(list2))
print(result)

# USING LOOP METHOD
list1 = [1,2,3,4]
list2 = [3,4,5,6]
result = []
for i in list1:
    if i not in list2:
        result.append(i)
for i in list2:
    if i not in list1:
        result.append(i)
print(result)

# USING TWO POINTERS
list1 = sorted([1,2,3,4])
list2 = sorted([3,4,5,6])
i = 0
j = 0
result = []
while i < len(list1) and j < len(list2):
    if list1[i] == list2[j]:
        i += 1
        j += 1
    elif list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1
while i < len(list1):
    result.append(list1[i])
    i += 1
while j < len(list2):
    result.append(list2[j])
    j += 1
print(result)

# USING SYMMETRIC_DIFFERENCE_UPDATE
list1 = [1,2,3,4]
list2 = [3,4,5,6]
s1 = set(list1)
s1.symmetric_difference_update(list2)
print(list(s1))

# USING FILTER METHOD
list1 = [1,2,3,4]
list2 = [3,4,5,6]
s1 = set(list1)
s2 = set(list2)
result1 = list(filter(lambda x: x not in s2, list1))
result2= list(filter(lambda x: x not in s1, list2))
result3=result1+result2
print(result3)