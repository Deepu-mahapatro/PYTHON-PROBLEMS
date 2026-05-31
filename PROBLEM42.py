#COMPRESSION OF STRINGS (AAABBC->A3B2C1)
#THE GOAL IS TO COMPRESS A STRING BY REPLACING CONSECUTIVE
#REPEATED CHARACTERS WITH : CHARACTER+COUNT
#WE READ THE STRING FROM LEFT TO RIGHT
#FOR EACH CHARACTER: 
       #STORE PREVIOUS CHARACTER
       #STORE ITS COUNT
#CONTINUE WITH NEXT CHARACTER
# 1. START FROM FIRST CHARACTER.
# 2. COUNT CONSECUTIVE OCCURRENCES.
# 3. WHEN CHARACTER CHANGES:
#       STORE CHARACTER + COUNT.
# 4. RESET COUNT FOR NEW CHARACTER.
# 5. CONTINUE UNTIL END.
# 6. DON'T FORGET THE FINAL GROUP.
# FINAL IDEA:STRING COMPRESSION WORKS BY GROUPING CONSECUTIVE 
# IDENTICAL CHARACTERS AND REPLACING EACH GROUP WITH 
# "CHARACTER + COUNT", WHERE THE COUNT REPRESENTS CONSECUTIVE OCCURRENCES,
# NOT TOTAL FREQUENCY IN THE ENTIRE STRING.

#ITERATIVE APPROACH(BEST METHOD)
def compress_string(s):
    #EDGE CASE:EMPTY STRING
    if not s:
        return ""
    result=""
    #FIRST CHARACTER
    current_char=s[0]
    count=1
    #START FORM SECOND CHARACTER
    for i in range(1,len(s)):
        #SAME CHARACTER 
        if s[i]==current_char:
            count+=1
        #NEW CHARACTER FOUND
        else:
            result+=current_char+str(count)
            current_char=s[i]
            count=1
    #DON'T FORGET LAST GROUP 
    result+=current_char+str(count)
    return result
print(compress_string("AAABBC"))

#TWO POINTER APPROACH
def compress_string(s):
    #EDGE CASE:EMPTY STRING
    if not s:
        return ""
    result=""
    n=len(s)
    left=0
    while left<n:
        right=left
        #COUNT SAME CHARACTERS
        while right<n and s[right]==s[left]:
            right+=1
        count=right-left
        result+=s[left]+str(count)
        left=right
    return result
print(compress_string("AAABBC"))

#USING LIST METHOD
def compress_string(s):
    #EDGE CASE: EMPTY STRING
    if not s:
        return ""
    result=[]
    current_char=s[0]
    count=1
    for i in range(1,len(s)):
        if s[i]==current_char:
            count+=1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char=s[i]
            count=1
    #LAST GROUP
    result.append(current_char)
    result.append(str(count))
    return ''.join(result)
print(compress_string("AAABBC"))

#USING WHILE LOOP METHOD
def compress_string(s):
    if not s:
        return ""
    result=""
    i=0
    while i < len(s):
        count=1
        while i+1<len(s) and s[i]==s[i+1]:
            count+=1
            i+=1
        result+=s[i]+str(count)
        i+=1
    return result
print(compress_string("AAABBC"))