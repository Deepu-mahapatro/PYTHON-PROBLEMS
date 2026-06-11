# FLATTEN A NESTED LIST
# CORE IDEA:
      # LIST MAY CONTAIN
      # OTHER LISTS INSIDE IT
      # REMOVE ALL NESTING
      # RETURN SINGLE FLAT LIST
# EDGE CASES:
      # EMPTY LIST
      # ALREADY FLAT LIST
      # SINGLE ELEMENT
      # DEEPLY NESTED LIST
      # ONLY EMPTY LISTS
      # MIXED DATA TYPES
# KEY OBSERVATION:
      # NORMAL ELEMENTS
      # GO DIRECTLY TO RESULT
      # NESTED LISTS
      # MUST BE EXPLORED
      # PROCESS UNTIL
      # NO LISTS REMAIN
# EXAMPLE:
      # NUMS = [1,[2,3],[4,[5,6]]]
      # FLAT RESULT
      # [1,2,3,4,5,6]
# APPROACH 1 (RECURSIVE BACKTRACKING):
      # TRAVERSE EACH ELEMENT
      # IF ELEMENT IS A LIST
      # GO INSIDE IT
      # IF NORMAL ELEMENT
      # ADD TO RESULT
      # RETURN BACK
      # CONTINUE TRAVERSAL
# APPROACH 2 (RECURSIVE RETURN STYLE):
      # EACH RECURSIVE CALL
      # RETURNS FLATTENED RESULT
      # COMBINE RESULTS
      # FROM ALL SUB LISTS
      # RETURN FINAL LIST
# TIME COMPLEXITY:
      # RECURSIVE BACKTRACKING  -> O(N)
      # RECURSIVE RETURN STYLE  -> O(N)
# SPACE COMPLEXITY:
      # RECURSIVE BACKTRACKING  -> O(D)
      # RECURSIVE RETURN STYLE  -> O(D)
# CONCLUSION:
      # BETTER SOLUTION
            # RECURSIVE BACKTRACKING
      # OPTIMAL SOLUTION
            # RECURSIVE RETURN STYLE
      # MOST INTERVIEWERS EXPECT
            # RECURSIVE SOLUTION

#RECURSION BACKTRACKING METHOD
def flatten(nums):
    result=[]
    def backtrack(current):
        for item in current:
            #NESTED LIST
            if isinstance(item,list):
                backtrack(item)
            #NORMAL ELEMENT
            else:
                result.append(item)
    backtrack(nums)
    return result
nums=[1,[2,3],[4,[5,6]]]
print(flatten(nums))

#USING RECURSION STYLE 
def flatten(nums):
    result=[]
    for item in nums:
        #NESTED LIST
        if isinstance(item,list):
            result.extend(flatten(item))
        #NORMAL ELEMENT
        else:
            result.append(item)
    return result
nums=[1,[2,3],[4,[5,6]]]
print(flatten(nums))