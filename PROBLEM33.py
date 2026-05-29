#FIND MOST FREQUENT CHARACTER
#COUNT HOW MANY TIMES A CHARACTER APPEARS 
#NOW FIND TEH CHARACTER WITH HIGHEST COUNT 
#THT CHARACTER HAS TEH HIGHEST FREQUENCY COUNT
#START READING CHARACTERS ONE BY ONE 
#COUNT OCCURRENCES FOR EACH CHARACTER
#NOW FIND MAXIMUM COUNT AMONG THEM 
#EDGE CASE:  
          #EMPTY STRING -> NO MAX COUNT
          #FOR SINGLE CHARACTER "A"-> "A"
          #FOR SAME CHARACTERS "AAA"-> "A"
          #IT ALSO INCLUDED SPACES AND SYMBOLS AND OTHERS
          #FOR INPUT "AABB"-> MAX_COUNT="A" OR "B"

#BRUTE FORCE METHOD
def most_frequent(s):
    #EDGE CASE:
    if len(s)==0:
        return None
    max_count=0
    result=s[0]
    for i in range(len(s)):
        count=0
        for j in range(len(s)):
            if s[i]==s[j]:
                count+=1
            if count>max_count:
                max_count=count
                result=s[i]
    return result
s="aaabbc"
print(most_frequent(s))

#USING HASH MAP AND DICTIONARY METHOD
def most_frequent(s):
    #EDGE CASE:
    if len(s)==0:
        return None
    freq={}
    #COUNT FREQUENCIES
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    max_count=0
    result=None
    #FOR HIGHEST FREQUENCIES
    for ch,count in freq.items():
        if count>max_count:
            max_count=count
            result=ch
    return result
s="aabbc"
print(most_frequent(s))

#DICTIONARY + MAX() METHOD
def most_frequent(s):
    #EDGE CASE:
    if len(s)==0:
        return None
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    return max(freq,key=freq.get)
s="aaabbc"
print(most_frequent(s))   

#USING SORTING APPROACH
def most_frequent(s):
    #EGE CASE:
    if len(s)==0:
        return None
    chars=sorted(s)
    max_count=1
    current_count=1
    result=chars[0]
    for i in range(1,len(chars)):
        if chars[i]==chars[i-1]:
            current_count+=1
        else:
            current_count=1
        if current_count>max_count:
            max_count=current_count
            result=chars[i]
    return result
s="aaabbc"
print(most_frequent(s))