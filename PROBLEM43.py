#REMOVAL OF VOWELS IN A STRING
#PROCESS EACH CHARACTER ONE BY ONE
#CHECK WHETHER IT IS VOWEL OR NOT 
#IF IT IS VOWEL REMOVE IT OR ELSE KEEP IT 
#CONTINUE UNTIL THE ENTIRE STRING IS PROCESSED
#EDGE CASE:
          #EMPTY STRING ""->""
          #SINGLE VOWEL "A"->""
          #SINGLE CONSONANT "B"->"B"
          #SPACES KEEP IT AS IT IS 
#COMPLETE PROCESS:
#REMOVE VOWELS
#PURPOSE
# REMOVE ALL VOWELS FROM THE STRING.
# #VOWELS
# A, E, I, O, U
# a, e, i, o, u
#PROCESS
# 1. VISIT EACH CHARACTER.
# 2. CHECK WHETHER IT IS A VOWEL.
# 3. IF IT IS A VOWEL:
#       SKIP IT.
# 4. OTHERWISE:
#       KEEP IT.
# 5. CONTINUE UNTIL THE STRING ENDS.
# 6. JOIN ALL KEPT CHARACTERS.
# 7. RETURN THE RESULT.
# #KEY IDEA
# REMOVE ONLY VOWELS.
# KEEP EVERYTHING ELSE.
# MAINTAIN THE ORIGINAL ORDER.

#SIMPLE FOR LOOP
def remove_vowels(s):
    #ALL VOWELS
    vowels="aeiouAEIOU"
    result=""
    #CHECK EACH CHARACTER
    for char in s:
        #KEEP ONLY NON-VOWELS
        if char not in vowels:
            result+=char
    return result
print(remove_vowels("HELLO"))

#USING LIST + JOIN METHOD
def remove_vowels(s):
    vowels="aeiouAEIOU"
    result=[]
    for char in s:
        if char not in vowels:
            result.append(char)
    return ''.join(result)
print(remove_vowels("HELLO"))

#USING RECURSION METHOD
def remove_vowels(s):
    vowels="aeiouAEIOU"
    #BASE CASE
    if not s:
        return ""
    #SKIP VOWEL
    if s[0] in vowels:
        return remove_vowels(s[1:])
    #KEEP NON-VOWELS
    return s[0]+remove_vowels(s[1:])
print(remove_vowels("HELLO"))

#USING WHILE LOOP METHOD
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    i = 0
    while i < len(s):
        if s[i] not in vowels:
            result += s[i]
        i += 1
    return result
print(remove_vowels("HELLO"))