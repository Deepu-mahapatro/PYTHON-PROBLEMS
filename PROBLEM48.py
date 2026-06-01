#COUNT OCCURRENCES OF EACH WORD
#TO DETERMINE HOW MANY TIMES EACH WORD APPEARS IN A STRING
#CORE IDEA:
      #TRAVERSE EACH WORD IN THE INPUT
      #KEEP TRACK OF WORD FREQUENCIES
      #IF A WORD IS SEEN FOR THE FIRST TIME
      #STORE IT WITH COUNT 1
      #IF THE WORD ALREADY EXISTS
      #INCREMENT ITS COUNT
#EDGE CASES:
      #EMPTY STRING -> RETURN EMPTY RESULT
      #SINGLE WORD -> COUNT IS 1
      #ALL WORDS UNIQUE -> EVERY COUNT IS 1
      #ALL WORDS SAME -> COUNT EQUALS TOTAL WORDS
      #CASE-SENSITIVE COMPARISON DEPENDS ON REQUIREMENTS
      #MULTIPLE SPACES SHOULD NOT AFFECT COUNTING
      #PUNCTUATION HANDLING DEPENDS ON REQUIREMENTS
#KEY OBSERVATION:
      #EACH WORD ACTS AS A KEY
      #ITS FREQUENCY ACTS AS THE VALUE
#CONCLUSION:
#SCAN ALL WORDS ONE BY ONE.
#FOR EACH WORD, STORE OR UPDATE ITS COUNT.
#THE FINAL RESULT CONTAINS EVERY WORD
#AND THE NUMBER OF TIMES IT APPEARS.

#USING BRUTE FORCE METHOD
def count_word(s):
    #EDGE CASE:
    if not s.strip():
        return {}
    freq={}
    words=s.split()
    for ch in words:
        if ch not in freq:
            count=0
            for w in words:
                if w==ch:
                    count+=1
            freq[ch]=count
    return freq
s="apple apple apple mango mango orange"
print(count_word(s))

#USING DICTIONARY METHOD
def count_word(text):
    #EDGE CASE:
    if not text.strip():
        return {}
    freq={}
    #SPLIT STRING INTO WORDS
    words=text.split()
    #COUNT FREQUENCIES
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq
text="apple mango apple mango apple orange"
print(count_word(text))

#USING DICT.GET() METHOD
def count_word(s):
    #EDGE CASE:
    if not s.strip():
        return {}
    freq={}
    words=s.split()
    for ch in words:
            freq[ch]=freq.get(ch,0)+1
    return freq
s="apple mango apple apple mango orange"
print(count_word(s))

#CASE INSENSITIVE METHOD
def count_word(s):
    freq={}
    for word in s.lower().split():
        freq[word]=freq.get(word,0)+1
    return freq
s="apple apple apple orange mango mango"
print(count_word(s))