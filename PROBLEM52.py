#CHECK IF ONE STRING IS A SUBSEQUENCE OF ANOTHER
#TO DETERMINE WHETHER ALL CHARACTERS OF
#THE FIRST STRING APPEAR IN THE SECOND STRING
#IN THE SAME ORDER
#CORE IDEA:
      #USE TWO POINTERS
      #ONE POINTER FOR THE SUBSEQUENCE STRING
      #ONE POINTER FOR THE MAIN STRING
      #TRAVERSE THE MAIN STRING
      #WHEN CHARACTERS MATCH
      #MOVE BOTH POINTERS
      #WHEN CHARACTERS DO NOT MATCH
      #MOVE ONLY THE MAIN STRING POINTER
      #IF ALL CHARACTERS OF THE FIRST STRING
      #ARE MATCHED
      #IT IS A VALID SUBSEQUENCE
#EDGE CASES:
      #EMPTY SUBSEQUENCE STRING -> RETURN TRUE
      #BOTH STRINGS EMPTY -> RETURN TRUE
      #SUBSEQUENCE STRING LONGER THAN MAIN STRING
      #-> RETURN FALSE
      #EXACT MATCH -> RETURN TRUE
      #MISSING CHARACTER -> RETURN FALSE
      #WRONG ORDER OF CHARACTERS -> RETURN FALSE
      #REPEATED CHARACTERS SHOULD BE MATCHED
      #IN THE CORRECT ORDER
#KEY OBSERVATION:
      #CHARACTERS DO NOT NEED TO BE ADJACENT
      #ONLY THE ORDER MUST BE PRESERVED
#CONCLUSION:
#SCAN THE MAIN STRING FROM LEFT TO RIGHT.
#MATCH CHARACTERS OF THE SUBSEQUENCE
#ONE BY ONE.
#IF ALL CHARACTERS ARE MATCHED,
#RETURN TRUE.
#OTHERWISE,
#RETURN FALSE.

#USING TEO POINTERS METHOD
def is_subsequence(s1,s2):
    #EDGE CASE
    if not s1:
        return True
    i=0 #POINTER FOR S1
    j=0 #POINTER FOR S2
    while i<len(s1) and j<len(s2):
        #CHARACTER MATCH
        if s1[i]==s2[j]:
            i+=1
        #ALWAYS MOVE IN S2
        j+=1
    #IF ALL CHARACTERS OF S1 MATCHED
    return i==len(s1)
print(is_subsequence("abc","ahbgdc"))

#USING FOR LOOP METHOD
def is_subsequence(s1,s2):
    #EDGE CASE
    if not s1:
        return True
    index=0
    for char in s2:
        #MATCH FOUND
        if index<len(s1) and char==s1[index]:
            index+=1
    #IF ALL CHARACTERS OF S1 MATCHES
    return index==len(s1)
print(is_subsequence("abc","abhgdc"))

#USING RECURSIVE METHOD
def is_subsequence(s1,s2,i=0,j=0):
    #ALL CHARACTERS MATCHED
    if i==len(s1):
        return True
    #MAIN STRING FINISHED
    if j==len(s2):
        return False
    #CHARACTER MATCH
    if s1[i]==s2[j]:
        return is_subsequence(s1,s2,i+1,j+1)
    #NO MATCH 
    return is_subsequence(s1,s2,i,j-1)
print(is_subsequence("abc","abhgdc"))

#USING RECURSIVE FUNCTION SIMPLE METHOD
def is_subsequence(s1,s2):
    #EDGE CASE
    if not s1:
        return True
    #MAIN STRING FINISHED
    if not s2:
        return False
    #CHARACTER MATCH
    if s1[0]==s2[0]:
        return is_subsequence(s1[1:],s2[1:])
    return is_subsequence(s1,s2[1:])
print(is_subsequence("abc","abhgdc"))