#REMOVE DUPLICATES IN A STRING
#KEEP ONLY FIRST OCCURRENCE OF THE ELEMENTS
#NO REPEATED ELEMENTS ARE ALLOWED
#EDGE CASE:
          #FOR EMPTY STRING ""-> ""
          #FOR SINGLE CHARACTER "A"-> "A"
          #CASE SENSITIVE "Aa"->"Aa"

#USING BRUTE FORCE METHOD
text="programming"
result=""
for ch in text:
    if ch not in result:
        result+=ch
print(result)

#USING CASE INSENSITIVE METHOD
text="programming"
seen=set()
result=""
for ch in text:
    #COVERT INTO LOWER CASE
    lower_char=ch.lower()
    if lower_char not in seen:
        result+=ch
        seen.add(lower_char)
print(result)

#USING SET METHOD
text="programming"
seen=set()
result=""
for ch in text:
    if ch not in seen:
        result+=ch
        seen.add(ch)
print(result)
#USING ORDERED DICTIONARY
from collections import OrderedDict
text="programming"
result="".join(OrderedDict.fromkeys(text))
print(result)

#USING RECURSION METHOD
def remove_duplicate(text,seen=set(),index=0):
    #BASE CASE:
    if index==len(text):
        return ""
    #CURRENT CHARACTER
    ch=text[index]
    if ch not in seen:
        seen.add(ch)
        return ch+remove_duplicate(text,seen,index+1)
    else:
        #SKIP DUPLICATE
        return remove_duplicate(text,seen,index+1)
text="programming"
print(remove_duplicate(text))