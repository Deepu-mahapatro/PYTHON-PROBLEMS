#CHECK PANGRAM
#AS IN ENGLISH ALPHABETS CONSISTS OF 
#a b c d e f g h i j k l m
#n o p q r s t u v w x y z
#A SENTENCE IS SAID TO BE PANGRAM
#IF IT CONSISTS OF ALL CHARACTERS OF ALPHABETS AT ONCE MINIMUM
#ALL 26 CHARACTERS MUST APPEAR AT MINIMUM ONE TIME
#READ EACH CHARACTER AND RECORD UNIQUE CHARACTERS
#IGNORE NON-ALPHABETS CHARACTERS CONTINUE UNTIL END
#NOW CONTINUE UNIQUE CHARACTERS
#EDGE CASE:
          # FOR EMPTY STRING : ""-> FALSE
          #FOR ONLY SPACES -> FALSE
          #FOR SINGLE CHARACTER-> FALSE
          #FOR MIXED UPPER AND LOWER-> TRUE
          #FOR NUM OR SYMBOL BUT IT CONSISTS 26 MINIMUM ONE TIME -> TRUE

#USING SET METHOD
def is_pangram(s):
    letters=set()
    for ch in s.lower():
        if "a"<=ch<="z":
            letters.add(ch)
    return len(letters)==26
s="the quick brown fox jumps over the lazy dog"
print(is_pangram(s))

#USING ALPHABET SET COMPARISON
def is_pangram(s):
    alphabet=set("abcdefghijklmnopqrstuvwxyz")
    return alphabet<=set(s.lower())
s="the quick brown fox jumps over the lazy dog"
print(is_pangram(s))

#USING FREQUENCY ARRAY
def is_pangram(s):
    freq = [0] * 26
    for ch in s.lower():
        if 'a' <= ch <= 'z':
            index = ord(ch) - ord('a')
            freq[index] = 1
    return all(freq)
s="the quick brown fox jumps over the lazy dog"
print(is_pangram(s))

#BRUTE FORCE APPROACH
def is_pangram(s):
    s = s.lower()
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch not in s:
            return False
    return True
s="the quick brown fox jumps over the lazy dog"
print(is_pangram(s))

#USING DICTIONARY METHOD
def is_pangram(s):
    freq = {}
    for ch in s.lower():
        if 'a' <= ch <= 'z':
            freq[ch] = freq.get(ch, 0) + 1
    return len(freq) == 26
s="the quick brown fox jumps over the lazy dog !!!"
print(is_pangram(s))