#CHECK IF A STRING HAS ALL UNIQUE CHARACTERS
#TO DETERMINE WHETHER EVERY CHARACTER IN A STRING APPEARS ONLY ONCE
#A STRING HAS ALL UNIQUE CHARACTERS IF:
      #NO CHARACTER REPEATS
      #EACH CHARACTER OCCURS EXACTLY ONCE
      #THE MOMENT A CHARACTER REAPPEARS, THE STRING IS NOT UNIQUE
#CORE IDEA:
      #TRAVERSE THE STRING CHARACTER BY CHARACTER
      #KEEP TRACK OF CHARACTERS ALREADY ENCOUNTERED
      #IF A CHARACTER IS FOUND AGAIN
      #DUPLICATE EXISTS -> FALSE
      #IF THE ENTIRE STRING IS PROCESSED WITHOUT DUPLICATES
      #ALL CHARACTERS ARE UNIQUE -> TRUE
#EDGE CASES:
      #EMPTY STRING -> TRUE
      #SINGLE CHARACTER -> TRUE
      #ALL CHARACTERS SAME -> FALSE
      #CASE-SENSITIVE CHARACTERS ('A' ≠ 'a')
      #SPACES, SYMBOLS, AND DIGITS ARE ALSO CHARACTERS
      #ANY REPEATED CHARACTER MAKES THE RESULT FALSE
#KEY OBSERVATION:
      #A STRING IS UNIQUE ONLY WHEN EVERY CHARACTER
      #APPEARS EXACTLY ONE TIME
#CONCLUSION:
#IF NO CHARACTER REPEATS, RETURN TRUE.
#IF ANY CHARACTER IS ENCOUNTERED MORE THAN ONCE, RETURN FALSE.

#BRUTE FORCE APPROACH
def has_unique(s):
    n=len(s)
    for i in range(n):
        for j in range(i+1,n):
            if s[i]==s[j]:
                return False
    return True
s="HELLO WORD"
print(has_unique(s))

#USING FREQUENCY DICTIONARY METHOD
def has_unique(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
        if freq[ch]>1:
            return False
    return True
s="HELO"
print(has_unique(s))

#USING SET METHOD
def has_unique(s):
    seen=set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True
s="HELO"
print(has_unique(s))

#USING LENGTH OPERATION
def has_unique(s):
    return len(s)==len(set(s))
s="HELO"
print(has_unique(s))

#USING SORTING METHOD
def has_unique(s):
    chars=sorted(s)
    for i in range(1,len(chars)):
        if chars[i]==chars[i-1]:
            return False
    return True
print(has_unique("HELO"))