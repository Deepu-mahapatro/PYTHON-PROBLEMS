#REVERSE WORD IN A SENTENCE
#LETTERS INSIDE THE WORDS ARE NOT REVERSED 
#ONLY TEH POSITIONS OF WORDS ARE REVERSED
#REVERSE WORD AND CHARACTERS ARE DIFFERENT
#EX: "I LOVE->"LOVE I"
#IDENTIFY TEH WORDS AND FIND FIRST AND LAST WORD
#SWAP TEH POSITIONS AND CONTINUE TOWARD CENTER
#NOW JOIN THE WORDS BACK
#EDGE CASE:
          # FOR EMPTY STRING ""->""
          #FOR SINGLE WORD "PYTHON"->"PYTHON"
          #SPACES ARE REMOVED AUTOMATICALLY
          #FOR "    "-> ""
          #FOR NUMBERS BEHAVE LIKE NORMAL WORDS

#USING SPLIT()+REVERSE()+JOIN() METHOD
def reverse_word(s):
    #EDGE CASE:
    if s.strip()=="":
        return ""
    words=s.split()
    words.reverse()
    return " ".join(words)
s="I LOVE PYTHON"
print(reverse_word(s))

#USING SLICING METHOD
def reverse_word(s):
    #EDGE CASE:
    if s.strip()=="":
        return ""
    words=s.split()
    return " ".join(words[::-1])
s="I LOVE PYTHON"
print(reverse_word(s))

#WITHOUT USING REVERSE() METHOD
def reverse_word(s):
    #EDGE CASE:
    if s.strip()=="":
        return ""
    result=[]
    for word in s.split():
        result.insert(0,word)
    return " ". join(result)
s="I LOVE PYTHON"
print(reverse_word(s))

#TWO POINTER METHOD
def reverse_word(s):
    #EDGE CASE:
    if s.strip()=="":
        return ""
    word=s.split()
    left=0
    right=len(word)-1
    while left<right:
        word[left],word[right]=word[right],word[left]
        left+=1
        right-=1
    return " ".join(word)
s="I LOVE PYTHON"
print(reverse_word(s))