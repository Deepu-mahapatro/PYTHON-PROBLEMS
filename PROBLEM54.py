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