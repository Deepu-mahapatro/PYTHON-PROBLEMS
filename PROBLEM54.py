#MORSE CODE ENCODER
#TO CONVERT EACH CHARACTER OF A TEXT
#INTO ITS CORRESPONDING MORSE CODE REPRESENTATION
#CORE IDEA:
      #CREATE A DICTIONARY MAPPING
      #CHARACTERS TO MORSE CODE
      #TRAVERSE EACH CHARACTER IN THE INPUT STRING
      #CONVERT CHARACTER TO UPPERCASE
      #LOOK UP ITS MORSE CODE IN THE DICTIONARY
      #STORE THE MORSE CODE IN A RESULT LIST
      #JOIN ALL MORSE CODES WITH SPACES
      #RETURN OR PRINT THE ENCODED STRING
#EDGE CASES:
      #EMPTY STRING -> RETURN EMPTY STRING
      #ONLY SPACES -> RETURN EMPTY STRING
      #SINGLE CHARACTER -> RETURN ITS MORSE CODE
      #LOWERCASE LETTERS -> CONVERT TO UPPERCASE
      #MIXED CASE LETTERS -> HANDLE CORRECTLY
      #MULTIPLE WORDS -> USE "/" AS WORD SEPARATOR
      #NUMBERS -> REQUIRE NUMBER MORSE MAPPINGS
      #SPECIAL CHARACTERS -> SKIP OR HANDLE
      #BASED ON REQUIREMENTS
      #UNSUPPORTED CHARACTERS -> IGNORE OR
      #RAISE AN ERROR
#KEY OBSERVATION:
      #EACH CHARACTER IS PROCESSED INDEPENDENTLY
      #DICTIONARY LOOKUP PROVIDES FAST ACCESS
      #TO THE CORRESPONDING MORSE CODE
      #CHARACTERS ARE REPLACED
      #NOT REARRANGED OR SORTED
#CONCLUSION:
#SCAN THE INPUT STRING CHARACTER BY CHARACTER.
#LOOK UP EACH CHARACTER IN THE MORSE DICTIONARY.
#STORE THE CORRESPONDING MORSE CODE.
#JOIN ALL MORSE CODES TO FORM THE FINAL
#ENCODED MESSAGE.
#RETURN THE MORSE CODE STRING.

#USING BRUTE FORCE APPROACH
    #MORSE CODE MAPPING
MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
    }
def morse_code(s):
    #EDGE CASE:
    if not s:
        return ""
    result=[]
    #TRAVERSE EACH CHARACTER
    for char in s.upper():
        #CHECK IF STRING EXISTS OR NOT
        if char in MORSE:
            #ADD MORSE TO RESULT
            result.append(MORSE[char])
    #JOIN MORSE CODES
    return " ".join(result)
s="HELLO123"
print(morse_code(s))

#TO HANDLE SPACES BETWEEN WORDS
def morse_code(s):
    #EDGE CASE
    if not s:
        return ""
    result=[]
    for char in s.upper():
        #WORD SEPARATOR 
        if char==" ":
            result.append("/")
        elif char in MORSE:
            result.append(MORSE[char])
        else:
            continue
    return " ".join(result)
s="HELLO WORLD @@@"
print(morse_code(s))