#PIG LATIN CONVERTER
#TO CONVERT ENGLISH WORDS OR SENTENCES
#INTO THEIR PIG LATIN REPRESENTATION
#CORE IDEA:
      #PROCESS EACH WORD INDIVIDUALLY
      #CHECK WHETHER THE WORD STARTS
      #WITH A VOWEL OR CONSONANT
      #IF THE WORD STARTS WITH A VOWEL
      #ADD "way" TO THE END
      #IF THE WORD STARTS WITH A CONSONANT
      #FIND THE FIRST VOWEL
      #MOVE ALL LEADING CONSONANTS
      #TO THE END OF THE WORD
      #ADD "ay" TO THE END
      #STORE THE CONVERTED WORD
      #JOIN ALL CONVERTED WORDS
      #BACK INTO A SENTENCE
#EDGE CASES:
      #EMPTY STRING -> RETURN EMPTY STRING
      #ONLY SPACES -> RETURN EMPTY STRING
      #SINGLE VOWEL WORD -> ADD "way"
      #SINGLE CONSONANT WORD -> ADD "ay"
      #ALL VOWELS -> ADD "way"
      #NO VOWELS -> RETURN WORD + "ay"
      #LOWERCASE WORDS -> HANDLE CORRECTLY
      #UPPERCASE WORDS -> HANDLE CORRECTLY
      #MIXED CASE WORDS -> HANDLE CORRECTLY
      #MULTIPLE WORDS -> CONVERT EACH WORD
      #EXTRA SPACES -> SHOULD NOT AFFECT RESULT
      #PUNCTUATION -> HANDLE BASED ON REQUIREMENTS
#KEY OBSERVATION:
      #THE FIRST VOWEL DETERMINES
      #HOW THE WORD IS TRANSFORMED
      #WORDS STARTING WITH VOWELS
      #ONLY REQUIRE APPENDING "way"
      #WORDS STARTING WITH CONSONANTS
      #REQUIRE MOVING THE LEADING
      #CONSONANT CLUSTER
      #STRING SLICING IS THE MAIN OPERATION
#CONCLUSION:
#PROCESS EACH WORD SEPARATELY.
#IF IT STARTS WITH A VOWEL,
#APPEND "way".
#OTHERWISE,
#FIND THE FIRST VOWEL,
#MOVE THE LEADING CONSONANTS
#TO THE END,
#APPEND "ay",
#AND RETURN THE FINAL
#PIG LATIN SENTENCE.

#BRUTE FORCE APPROACH
def pig_latin(s):
    #VOWELS
    vowels="aeiouAEIOU"
    #EDGE CASE
    if not s:
        return ""
    #WORD STARTS WITH A VOWEL
    if s[0] in vowels:
        return s+"way"
    #FIND FIRST VOWEL
    for i in range(len(s)):
        if s[i] in vowels:
            #MOVE LEADING CONSONANTS
            return s[i:]+s[:i]+"ay"
    #NO VOWEL FOUND
    return s+"ay"
s="hello"
print(pig_latin(s))

#CONVERT AN ENTIRE SENTENCE
def pig_latin(s):
    if not s:
        return ""
    #VOWELS
    vowels="aeiouAEIOU"
    result=[]
    #PROCESS EACH WORD
    for word in s.split():
        #START WITH VOWEL
        if word[0] in vowels:
            result.append(word+"way")
        else:
            #FIND FIRST VOWEL
            for i in range(len(word)):
                if word[i] in vowels:
                    result.append(
                        word[i:]+word[:i]+"ay"
                    )
                    break
            else:
                #NO VOWEL
                result.append(word+"ay")
    return " ".join(result)
s="hello world"
print(pig_latin(s))

#PRESERVE UPPER CASE
def pig_latin(word):
    vowels = "aeiouAEIOU"
    is_upper = word.isupper()
    if word[0] in vowels:
        result = word + "way"
    else:
        for i, ch in enumerate(word):
            if ch in vowels:
                result = (
                    word[i:]
                    + word[:i]
                    + "ay"
                )
                break
        else:
            result = word + "ay"
    if is_upper:
        return result.upper()
    return result
print(pig_latin("HELLO"))