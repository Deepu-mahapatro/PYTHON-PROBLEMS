# ZIP TWO LISTS INTO A DICTIONARY
# CORE IDEA:
      # FIRST LIST CONTAINS KEYS
      # SECOND LIST CONTAINS VALUES
      # COMBINE BOTH LISTS
      # CREATE DICTIONARY
# EDGE CASES:
      # BOTH LISTS EMPTY
      # SINGLE ELEMENT
      # DIFFERENT LENGTH LISTS
      # DUPLICATE KEYS
      # MORE KEYS THAN VALUES
      # MORE VALUES THAN KEYS
# KEY OBSERVATION:
      # ELEMENTS AT SAME INDEX
      # BELONG TOGETHER
      # KEYS[i] BECOMES KEY
      # VALUES[i] BECOMES VALUE
      # STORE AS KEY-VALUE PAIR
# EXAMPLE:
      # KEYS = ["a","b","c"]
      # VALUES = [1,2,3]
      # OUTPUT
      # {"a":1,"b":2,"c":3}
# APPROACH 1 (ZIP + DICT):
      # PAIR KEYS AND VALUES
      # CREATE TUPLES
      # CONVERT TUPLES
      # INTO DICTIONARY
# APPROACH 2 (FOR LOOP):
      # TRAVERSE BOTH LISTS
      # TOGETHER
      # INSERT EACH PAIR
      # INTO DICTIONARY
# APPROACH 3 (UNEQUAL LENGTH CHECK):
      # VALIDATE INPUT
      # CHECK SAME LENGTH
      # CREATE DICTIONARY
      # OTHERWISE RAISE ERROR
# APPROACH 4 (INDEX TRAVERSAL):
      # TRAVERSE USING INDEX
      # ACCESS KEY
      # ACCESS VALUE
      # STORE IN DICTIONARY
# TIME COMPLEXITY:
      # ZIP + DICT       -> O(N)
      # FOR LOOP         -> O(N)
      # UNEQUAL LENGTH   -> O(N)
      # INDEX TRAVERSAL  -> O(N)
# SPACE COMPLEXITY:
      # ZIP + DICT       -> O(N)
      # FOR LOOP         -> O(N)
      # UNEQUAL LENGTH   -> O(N)
      # INDEX TRAVERSAL  -> O(N)
# CONCLUSION:
      # BETTER SOLUTION
            # FOR LOOP
      # OPTIMAL SOLUTION
            # ZIP + DICT
      # SAFE SOLUTION
            # UNEQUAL LENGTH CHECK
      # MOST INTERVIEWERS EXPECT
            # ZIP + DICT
            # OR INDEX TRAVERSAL

#USING ZIP() AND DICT() METHOD
def create_dictionary(keys,values):
    #PAIR KEYS AND VALUES
    #CONVERTS PAIRS INTO DICTIONARIES
    return dict(zip(keys,values))
keys=["a","b","c"]
values=[1,2,3]
print(create_dictionary(keys,values))

#USING FOR LOOP METHOD
def create_dictionary(keys,values):
    result={}
    #TRAVERSE BOTH LISTS TOGETHER
    for key,value in zip(keys,values):
        result[key]=value
    return result
keys=["a","b","c"]
values=[1,2,3]
print(create_dictionary(keys,values))

#HANDLE UNEQUAL LENGTH
def create_dictionary(keys,values):
    if len(keys)!=len(values):
        raise ValueError(
            "BOTH LISTS MUST HAVE SAME LENGTH"
        )
    return dict(zip(keys,values))
keys=["a","b","c"]
values=[1,2,3]
print(create_dictionary(keys,values))

#USING INDEX TRAVERSAL METHOD
def create_dictionary(keys,values):
    result={}
    #TRAVERSE USING INDEX
    for i in range(len(keys)):
        result[keys[i]]=values[i]
    return result
keys=["a","b","c"]
values=[1,2,3]
print(create_dictionary(keys,values))