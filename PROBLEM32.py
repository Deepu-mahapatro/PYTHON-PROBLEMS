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