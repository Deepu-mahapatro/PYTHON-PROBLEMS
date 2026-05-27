#COUNT VOWELS AND CONSONANTS
#VISIT EACH CHARACTER IN TEH STRING
#TURN INTO CASE SENSITIVE (UPPER OR LOWER)
#CHECK WHETHER THE CHARACTER IS ALPHABET
#IF VOWEL : INCREASE THE VOWEL COUNT
#ELSE : INCREASE THE CONSONANT COUNT
#IGNORE SPACES/DIGITS/SYMBOLS
#EDGE CASE:
     #FOR EMPTY STRING : VOWEL=O CONSONANT=0
     #FOR SINGLE CHARACTER "A"-> GOES TO VOWEL OR CONSONANT
     #FO UPPER AND LOWER CASE TURN INTO ONE CASE FIRST
     #NUM/SPACE/SYMBOLS ARE IGNORE REMAINING ARE COUNTED

#USING SIMPLE LOOP METHOD
def vo_con(s):
    #CONVERT INTO LOWERCASE
    s=s.lower()
    #INITIAL COUNTS
    vowels=0
    consonants=0
    #VOWELS SET
    vowel_set="aeiou"
    #TRAVERSE THE STRING
    for char in s:
        #CHECK IF ALPHABET OR NUM??
        if char.isalpha():
            #CHECK VOWEL
            if char in vowel_set:
                vowels+=1
            #OTHERWISE ITS CONSONANT
            else:
                consonants+=1
    #RETURN THE COUNTS
    return vowels,consonants
print(vo_con("HELLO"))

#USING ASCII METHOD
def vo_con(s):
    #COVERT INTO LOWER CASE
    s=s.lower()
    #INITIAL COUNTS
    vowels=0
    consonants=0
    #TRAVERSE 
    for char in s:
        #CHECK LOWER CASE ALPHABET RANGE
        if 'a'<=char <='z':
            #CHECK VOWELS
            if char in "aeiou":
                vowels+=1
            #CHECK CONSONANTS
            else:
                consonants+=1
    return vowels,consonants
print(vo_con("HELLO"))

#USING DICTIONARY METHOD
def count_vowels_consonants(s):
    #LOWERCASE
    s = s.lower()
    #DICTIONARY
    counts = {
        "vowels": 0,
        "consonants": 0
    }
    #TRAVERSE
    for char in s:
        #CHECK ALPHABET
        if char.isalpha():
            #VOWEL
            if char in "aeiou":
                counts["vowels"] += 1
            #CONSONANT
            else:
                counts["consonants"] += 1
    return counts
#TEST CASES
print(count_vowels_consonants("   "))

#USING RECURSION METHOD
def vo_con(s,vowels=0,consonants=0):
    #CONVERT TO LOWERCASE
    s=s.lower()
    #BASE CASE
    if len(s)==0:
        return vowels,consonants
    #FIRST CHARACTER
    char=s[0]
    #CHECK ALPHABET
    if char.isalpha():
        #VOWEL COUNT
        if char in "aeiou":
            vowels+=1
        #CONSONANT COUNT
        else:
            consonants+=1
    #RECURSIVE CALL 
    return vo_con(s[1:],vowels,consonants)
print(vo_con(""))