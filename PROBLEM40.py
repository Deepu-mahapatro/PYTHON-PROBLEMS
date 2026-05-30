#RUN LENGTH DECODING (RLD)
#LOSSLESS DATA DECOMPRESSION METHOD
#CONVERTS THE COMPRESSED STRING BACK TO ITS ORIGINAL FORM
#INSTEAD OF STORING CHARACTER AND COUNT
#WE REPEAT THE CHARACTER COUNT NUMBER OF TIMES
#FOR "A3B2C1" -> WE RESTORE AS -> AAABBC
#TAKE A CHARACTER AND ITS FREQUENCY
#REPEAT THE CHARACTER FREQUENCY NUMBER OF TIMES
#APPEND IT TO THE RESULT STRING
#CONTINUE UNTIL THE ENTIRE ENCODED STRING IS PROCESSED
#CHARACTERS ARE RECONSTRUCTED EXACTLY AS THEY APPEARED
#EXAMPLE:
#A3B2A1 -> AAABBA
#THE ORDER IS PRESERVED
#EDGE CASE:
    #EMPTY STRING "" -> ""
    #SINGLE CHARACTER COUNT "A1" -> A
    #NON REPEATING CHARACTERS
    #"A1B1C1" -> ABC
    #LARGE COUNTS
    #"A12" -> AAAAAAAAAAAA
    #NUMBERS MAY BECOME AMBIGUOUS
    #"1322" CAN BE HARD TO DISTINGUISH
    #WITHOUT A SEPARATOR FORMAT
    #SPACES
    #"A3 2B1" -> AAA  B
    #SPECIAL SYMBOLS
    #"@4#2" -> @@@@##
#ALGORITHM:
#TAKE A CHARACTER
#READ ITS COUNT
#REPEAT THE CHARACTER COUNT TIMES
#ADD IT TO THE RESULT
#MOVE TO THE NEXT CHARACTER-COUNT PAIR
#REPEAT UNTIL END OF STRING
#FORMULA:
    #DECODED = CHARACTER * COUNT
    
# BRUTE FORCE APPROACH
def run_length_decode(text):
    # EDGE CASE: EMPTY STRING
    if text == "":
        return ""
    result = ""
    # PROCESS CHARACTER-COUNT PAIRS
    for i in range(0, len(text), 2):
        # EXTRACT CHARACTER
        char = text[i]
        # EXTRACT COUNT
        count = int(text[i + 1])
        # REPEAT CHARACTER COUNT TIMES
        result += char * count
    return result
print(run_length_decode("A4B3C2D1A2"))

# BEST INTERVIEW METHOD
def run_length_decode(text):
    # EDGE CASE
    if not text:
        return ""
    # STORE DECODED PARTS
    result = []
    # PROCESS CHARACTER-COUNT PAIRS
    for i in range(0, len(text), 2):
        # EXTRACT CHARACTER
        char = text[i]
        # EXTRACT COUNT
        count = int(text[i + 1])
        # STORE REPEATED CHARACTER
        result.append(char * count)
    # CONVERT LIST TO STRING
    return "".join(result)
print(run_length_decode("A4B3C2D1A2"))

# PYTHONIC METHOD
def run_length_decode(text):
    # STORE DECODED PARTS
    result = []
    # CREATE CHARACTER-COUNT PAIRS
    pairs = zip(text[::2], text[1::2])
    # PROCESS EACH PAIR
    for char, count in pairs:
        # REPEAT CHARACTER COUNT TIMES
        result.append(char * int(count))
    return "".join(result)
print(run_length_decode("A4B3C2D1A2"))