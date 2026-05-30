#ANAGRAM CHECK PROBLEM
#BOTH THE CHARACTER CONTAIN SAME CHARACTER WITH SAME FREQUENCIES
#THIS TYPE OF WORDS CALLED AS ANAGRAM
#EX: SILENT->LISTEN (SAME CHARACTER AND SAME FREQUENCY)

#USING SORTING METHOD
s1="listen"
s2="silent"
    #CHECK STRING LENGTH FIRST
if len(s1)!=len(s2):
    print(False)
else:
    #SORT THE STRINGS
    sorted_s1=sorted(s1)
    sorted_s2=sorted(s2)
    #COMPARE THE TWO STRINGS
    print(sorted_s1==sorted_s2)

#USING HASH MAP AND DICTIONARY
s1="listen"
s2="silent"
#CHECK STRING LENGTHS
if len(s1)!=len(s2):
    print(False)
else:
    #STORE CHARACTER FREQUENCIES
    freq1={}
    freq2={}
    #COUNT FOR FIRST STRING
    for ch in s1:
        if ch in freq1:
            freq1[ch]+=1
        else:
            freq1[ch]=1
    #COUNT FOR SECOND STRING 
    for ch in s2:
        if ch in freq2:
            freq2[ch]+=1
        else:
            freq2[ch]=1
#COMPARE DICTIONARIES
print(freq1==freq2)

#USING COUNTER METHOD
from collections import Counter
s1="listen"
s2="silent"
print(Counter(s1)==Counter(s2)) 

#USING RECURSION METHOD
def count_chars(text, index, freq):
    # BASE CASE
    # IF ALL CHARACTERS PROCESSED
    if index == len(text):
        return
    # CURRENT CHARACTER
    ch = text[index]
    # UPDATE FREQUENCY
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
    # RECURSIVE CALL
    count_chars(text, index + 1, freq)
# INPUT STRINGS
s1 = "listen"
s2 = "silent"
# CHECK LENGTH FIRST
if len(s1) != len(s2):
    print(False)
else:
    # STORE FREQUENCIES
    freq1 = {}
    freq2 = {}
    # BUILD FREQUENCY MAPS
    count_chars(s1, 0, freq1)
    count_chars(s2, 0, freq2)
    # COMPARE MAPS
    print(freq1 == freq2)