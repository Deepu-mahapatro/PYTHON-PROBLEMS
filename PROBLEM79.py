# FIND COMMON ELEMENTS OF TWO LISTS
# CORE IDEA:
      # TWO LISTS ARE GIVEN
      # FIND ELEMENTS PRESENT IN BOTH LISTS
      # RETURN COMMON ELEMENTS
# EDGE CASES:
      # BOTH LISTS EMPTY
      # ONE LIST EMPTY
      # NO COMMON ELEMENTS
      # ALL ELEMENTS COMMON
      # DUPLICATE VALUES
      # NEGATIVE NUMBERS
      # UNSORTED LISTS
# KEY OBSERVATION:
      # COMMON ELEMENTS MUST EXIST IN BOTH LISTS
      # HASHING PROVIDES FAST LOOKUP
      # SORTED ARRAYS CAN USE TWO POINTERS
# EXAMPLE:
      # LIST1 = [1,2,3,4,5]
      # LIST2 = [5,6,7,8,9]
      # RESULT = [5]
# APPROACH 1 (SET INTERSECTION):
      # CONVERT BOTH LISTS TO SETS
      # FIND INTERSECTION USING &
      # RETURN COMMON ELEMENTS
# APPROACH 2 (BRUTE FORCE LOOP):
      # ITERATE THROUGH FIRST LIST
      # CHECK PRESENCE IN SECOND LIST
      # STORE COMMON ELEMENTS
# APPROACH 3 (TWO POINTER APPROACH):
      # USE TWO POINTERS
      # COMPARE ELEMENTS
      # MOVE POINTERS ACCORDINGLY
      # STORE MATCHES
      # ARRAYS SHOULD BE SORTED
# APPROACH 4 (INTERSECTION_UPDATE):
      # CONVERT FIRST LIST TO SET
      # KEEP ONLY COMMON ELEMENTS
      # MODIFY ORIGINAL SET
# APPROACH 5 (FILTER METHOD):
      # CONVERT SECOND LIST TO SET
      # FILTER COMMON ELEMENTS
      # RETURN RESULT
# TIME COMPLEXITY:
      # SET INTERSECTION     -> O(N+M)
      # BRUTE FORCE LOOP     -> O(N*M)
      # TWO POINTERS         -> O(N+M)
      # INTERSECTION_UPDATE  -> O(N+M)
      # FILTER + SET         -> O(N+M)
# SPACE COMPLEXITY:
      # SET INTERSECTION     -> O(N+M)
      # BRUTE FORCE LOOP     -> O(1)
      # TWO POINTERS         -> O(1)
      # INTERSECTION_UPDATE  -> O(N)
      # FILTER + SET         -> O(M)
# CONCLUSION:
      # SIMPLEST SOLUTION
            # SET INTERSECTION
      # BRUTE FORCE SOLUTION
            # LOOP METHOD
      # BEST FOR SORTED ARRAYS
            # TWO POINTER APPROACH
      # FUNCTIONAL STYLE
            # FILTER METHOD
      # OPTIMAL SOLUTION
            # SET INTERSECTION
      # MOST INTERVIEWERS EXPECT
            # HASH SET APPROACH O(N+M)


#USING SET INTERSECTION
list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
result=list(set(list1)&set(list2))
print(result)

#USING LOOP METHOD
list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
result=[]
for i in list1:
    if i in list2:
        result.append(i)
print(result)

#SORTED TWO POINTER APPROACH
list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
i=0
j=0
result=[]
while i<len(list1) and j<len(list2):
    if list1[i]==list2[j]:
        result.append(list1[i])
        i+=1
        j+=1
    elif list1[i]<list2[j]:
        i+=1
    else:
        j+=1
print(result)

#USING INTERSECTION_UPDATE METHOD
list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
s1=set(list1)
s1.intersection_update(list2)
print(list(s1))

#USING FILTER METHOD
list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
s1=set(list2)
result=list(filter(lambda x:x in s1,list1))
print(result)