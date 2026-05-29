#FIRST NON REPEATING CHARACTER
#TO FIND THE FIRST CHARACTER THAT APPEARS ONLY ONETIME
#READ EVERY CHARACTER AND COUNT TEH FREQUENCIES
#START SCANNING FORM BEGINNING AND RETURN CHARACTER
#EDGE CASE:
          #FOR EMPTY STRING ""->NONE
          #FOR SINGLE CHARACTER "A"->"A"
          #FOR UNIQUE CHARACTERS "ABC"->"A" ALREADY SATISFIED
          #IGNORE SPACES COVERT EITHER LOWER OR UPPER
          #SAME BEHAVE FOR NUMBERS

#USING HASHMAP AND DICTIONARY METHOD
def method(s):
    #EDGE CASE:
    if len(s)==0:
        return None
    freq={}
    #COUNT FREQUENCY
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    #FIND FIRST NON-REPEATING 
    for ch in s:
        if freq[ch]==1:
            return ch
    return None
s="aabbc"
print(method(s))

#BRUTE FORCE METHOD
def method(s):
    if len(s)==0:
        return None
    for i in range(len(s)):
        count=0
        for j in range(len(s)):
            if s[i]==s[j]:
                count+=1
        if count==1:
            return s[i]
    return None
s="aabbc"
print(method(s))

#USING STRING COUNT() METHOD
def method(s):
    if len(s)==0:
        return None
    for ch in s:
        if s.count(ch)==1:
            return ch
    return None
s="aabbc"
print(method(s))

#RETURN INDEX INSTEAD OF CHARACTER
def method(s):
    if len(s)==0:
        return 1
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for i in range(len(s)):
        if freq[s[i]]==1:
            return i
    return -1
s="aabbc"
print(method(s))

#USING COLLECTIONS COUNTER
from collections import Counter
def method(s):
    if len(s)==0:
        return None
    freq=Counter(s)
    for ch in s:
        if freq[ch]==1:
            return ch
    return None
s="aabbc"
print(method(s))