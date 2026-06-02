#REMOVE DUPLICATE WORDS IN A SENTENCE
#TO REMOVE REPEATED WORDS AND KEEP ONLY
#THE FIRST OCCURRENCE OF EACH WORD
#CORE IDEA:
      #SPLIT THE SENTENCE INTO WORDS
      #TRAVERSE EACH WORD
      #IF WORD IS NOT SEEN BEFORE
      #KEEP IT
      #IF WORD IS ALREADY SEEN
      #SKIP IT
#EDGE CASES:
      #EMPTY STRING -> RETURN EMPTY RESULT
      #ONLY ONE WORD -> RETURN THAT WORD
      #NO DUPLICATES -> RETURN ORIGINAL SENTENCE
      #ALL WORDS SAME -> KEEP FIRST WORD ONLY
      #MULTIPLE SPACES SHOULD BE HANDLED
      #CASE SENSITIVITY DEPENDS ON REQUIREMENTS
      #PUNCTUATION HANDLING DEPENDS ON REQUIREMENTS
#KEY OBSERVATION:
      #KEEP THE FIRST OCCURRENCE
      #REMOVE ALL LATER OCCURRENCES
#CONCLUSION:
#SCAN ALL WORDS.
#KEEP TRACK OF SEEN WORDS.
#ADD ONLY NEW WORDS TO THE RESULT.
#RETURN THE SENTENCE WITH UNIQUE WORDS.

#USING SET METHOD 
def remove_duplicate(s):
    #EDGE CASE:
    if not s or s.strip()=="":
        return ""
    words=s.split()
    seen=set()
    result=[]
    for word in words:
        #KEEP ONLY FIRST OCCURRENCE
        if word not in seen:
            seen.add(word)
            result.append(word)
    return " ".join(result)
s="apple apple apple orange mango"
print(remove_duplicate(s))

#USING BRUTE FORCE APPROACH
def remove_duplicate(s):
    #EDGE CASE
    if not s or s.strip()=="":
        return ""
    words=s.split()
    result=[]
    for word in words:
        #LINEAR SEARCH
        if word not in result:
            result.append(word)
    return " ".join(result)
s="apple apple apple orange mango"
print(remove_duplicate(s))

#USING SORTING METHOD
def remove_duplicate(s):
    #EDGE CASE
    if not s or s.strip()=="":
        return ""
    words=s.split()
    unique_words=sorted(set(words))
    return " ".join(unique_words)
s="apple apple apple orange mango"
print(remove_duplicate(s))

#USING CASE SENSITIVE METHOD
def remove_duplicate(s):
    #EDGE CASE
    if not s or s.strip()=="":
        return ""
    words=s.split()
    seen=set()
    result=[]
    for word in words:
        #CASE SENSITIVE CHECK
        lower_word=word.lower()
        if lower_word not in seen:
            seen.add(lower_word)
            result.append(word)
    return " ".join(result)
s="apple apple apple orange mango"
print(remove_duplicate(s))
    