#RUN LENGTH ENCODING (RLE) 
#LOSS LESS DATA COMPRESSION METHOD
#INSTEAD OF EVERY CHARACTER REPEATS WE STORE IT
#AS THE CHARACTER (HOW MANY TIMES IT REPEATED)
#TO REDUCE THE SIZE OF THE STRING CONTAINING MANY CHARACTERS
#FOR "AAABBC"-> WE STORE AS ->A3B2C1
#CHARACTERS ARE NOT CONSECUTIVE
#MEANS: "ABABA"->A1B1A1B1A1
#NOR A3B2 BECAUSE TEH A'S ARE SEPARATED
#EDGE CASE:
          #EMPTY STRING ""->""
          #SINGLE CHARACTER "A"->A1
          #FOR NON REPEATING CHARACTERS "ABC"->A1B1C1
          #IT ALSO PERFORMS FOR NUMBERS AS 11122->1322
          #IT ALSO PERFORM FOR SPACES AAA  B->A3 2B1
          #SAME FOR SPECIAL SYMBOLS ALSO
          
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