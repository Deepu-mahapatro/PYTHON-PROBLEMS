#RUN LENGTH ENCODING (RLE)
#LOSSLESS DATA COMPRESSION METHOD
#INSTEAD OF STORING EVERY REPEATED CHARACTER
#WE STORE THE CHARACTER AND ITS FREQUENCY
#FOR EVERY GROUP OF CONSECUTIVE CHARACTERS
#COUNT HOW MANY TIMES IT APPEARS
#STORE THE CHARACTER FOLLOWED BY ITS COUNT
#CONDITION:
#ENCODED = CHARACTER + COUNT
#FOR "AAABBC" -> WE STORE AS -> A3B2C1
#ONLY CONSECUTIVE CHARACTERS ARE COUNTED
#CHARACTERS ARE STORED IN THE SAME ORDER
#EDGE CASE:
          #FOR EMPTY STRING "" -> OUTPUT ""
          #FOR SINGLE CHARACTER "A" -> OUTPUT "A1"
          #FOR NON REPEATING CHARACTERS
          #"ABC" -> OUTPUT "A1B1C1"
          #FOR ALL SAME CHARACTERS
          #"AAAAAA" -> OUTPUT "A6"
          #FOR MULTIPLE GROUPS
          #"AAABBA" -> OUTPUT "A3B2A1"
          #FOR SPACES
          #"AAA  B" -> OUTPUT "A3 2B1"
          #FOR SPECIAL SYMBOLS
          #"@@@@##" -> OUTPUT "@4#2"
          #FOR NUMBERS
          #"11122" -> OUTPUT "1422"
          #FOR NON-CONSECUTIVE CHARACTERS
          #"ABABA" -> OUTPUT "A1B1A1B1A1"
          #NOT A3B2 BECAUSE THE A'S ARE SEPARATED
#TAKE THE FIRST CHARACTER
#COUNT ITS CONSECUTIVE OCCURRENCES
#IF THE NEXT CHARACTER IS THE SAME
#INCREASE THE COUNT
#IF THE NEXT CHARACTER IS DIFFERENT
#STORE THE CURRENT CHARACTER AND ITS COUNT
#RESET THE COUNT TO 1
#START COUNTING THE NEW CHARACTER
#REPEAT UNTIL THE END OF THE STRING
#STORE THE LAST CHARACTER AND ITS COUNT
#RETURN THE ENCODED STRING
#FORMULA:
        #ENCODED = CHARACTER + COUNT
          
# BRUTE FORCE APPROACH
def run_length_encode(text):
    # EDGE CASE: EMPTY STRING
    if text == "":
        return ""
    result = ""
    #FIRST CHARACTER IS ALREADY COUNTED ONCE
    count = 1
    #START FROM TEH SECOND CHARACTER
    for i in range(1, len(text)):
        #SAME CHARACTER -> INCREASE FREQUENCY
        if text[i] == text[i - 1]:
            count += 1
        # DIFFERENT CHARACTERS FOUND
        else:
            result += text[i - 1] + str(count)
            # START COUNTING NEW GROUP
            count = 1
    # LAST GROUP IS STILL NOT STORED
    result += text[-1] + str(count)
    return result
print(run_length_encode("AAAABBBCCDAA"))

# BEST INTERVIEW METHOD
def run_length_encode(text):
    # EDGE CASE
    if not text:
        return ""
    # STORE ENCODED PARTS
    result = []
    count = 1
    for i in range(1, len(text)):
        # SAME CHARACTER
        if text[i] == text[i - 1]:
            count += 1
        # CHARACTER CHANGED
        else:
            # STORE PREVIOUS CHARACTER AND FREQUENCY
            result.append(text[i - 1] + str(count))
            # RESET COUNTER
            count = 1
    # HANDLE LAST CHARACTER GROUP
    result.append(text[-1] + str(count))
    # CONVERT LIST TO STRING
    return "".join(result)
print(run_length_encode("AAAABBBCCDAA"))

# PYTHONIC METHOD
from itertools import groupby
def run_length_encode(text):
    result = []
    # GROUP CONSECUTIVE CHARACTERS
    for char, group in groupby(text):
        # COUNT ELEMENTS IN CURRENT GROUP
        count = len(list(group))
        result.append(char + str(count))
    return "".join(result)
print(run_length_encode("AAAABBBCCDAA"))