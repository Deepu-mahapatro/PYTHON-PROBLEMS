#FIND THE LONGEST WORD IN A SENTENCE
#TO DETERMINE THE WORD WITH THE MAXIMUM NUMBER OF CHARACTERS
#PRESENT IN A GIVEN SENTENCE
#CORE IDEA:
      #SPLIT THE SENTENCE INTO INDIVIDUAL WORDS
      #TRAVERSE EACH WORD ONE BY ONE
      #COMPARE THE LENGTH OF THE CURRENT WORD
      #WITH THE LONGEST WORD FOUND SO FAR
      #IF CURRENT WORD IS LONGER
      #UPDATE THE LONGEST WORD
#EDGE CASES:
      #EMPTY STRING -> RETURN EMPTY RESULT
      #ONLY ONE WORD -> RETURN THAT WORD
      #ALL WORDS SAME LENGTH -> RETURN FIRST LONGEST WORD
      #MULTIPLE LONGEST WORDS -> DEPENDS ON REQUIREMENTS
      #LEADING OR TRAILING SPACES SHOULD NOT AFFECT RESULT
      #MULTIPLE SPACES BETWEEN WORDS SHOULD BE HANDLED
      #PUNCTUATION HANDLING DEPENDS ON REQUIREMENTS
#KEY OBSERVATION:
      #THE LONGEST WORD IS THE WORD
      #WITH THE MAXIMUM LENGTH
#CONCLUSION:
#SCAN ALL WORDS IN THE SENTENCE.
#KEEP TRACK OF THE LONGEST WORD FOUND SO FAR.
#WHEN A LONGER WORD IS ENCOUNTERED,
#UPDATE THE RESULT.
#AFTER PROCESSING ALL WORDS,
#RETURN THE LONGEST WORD.

#USING BRUTE FORCE APPROACH
def longest_word(s):
    #EDGE CASE
    if not s.strip():
        return ""
    words=s.split()
    words.sort(key=len)
    return words[-1]
s="I LOVE PYTHON PROGRAMMING"
print(longest_word(s))

#MANUAL TRAVERSING METHOD
def longest_word(s):
    #EDGE CASE
    if not s.strip():
        return ""
    words=s.split()
    longest=words[0]
    for word in words:
        #LONGER WORD FOUND 
        if len(word)>len(longest):
            longest=word
    return longest
s="I LOVE PYTHON PROGRAMMING"
print(longest_word(s))

#USING MAX METHOD
def longest_word(s):
    #EDGE CASE
    if not s.strip():
        return ""
    return max(s.split(),key=len)
s="I LOVE PYTHON PROGRAMMING"
print(longest_word(s))

#FIND THE WORD AND ITS LENGTH
def longest_word(s):
    #EDGE CASE
    if not s.strip():
        return "",0
    longest=""
    for word in s.split():
        if len(word)>len(longest):
            longest=word
    return longest,len(longest)
s="I LOVE PYTHON PROGRAMMING"
word,length=longest_word(s)
print(word)
print(length)

#BEST METHOD TO SOLVE 
def longest_word(s):
    longest=""
    for word in s.split():
        if len(word)>len(longest):
            longest=word
    return longest
s="I LOVE PYTHON PROGRAMMING"
print(longest_word(s))

#USING REDUCE METHOD
from functools import reduce
def longest_word(s):
    words=s.split()
    if not words:
        return ""
    return reduce(
        lambda x,y:x if len(x)>len(y) else y,words
    )
s="I LOVE PYTHON PROGRAMMING"
print(longest_word(s))