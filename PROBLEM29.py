#COUNT WORDS IN A SENTENCE
#NOW WE NEED TO DIVIDE THE SENTENCE INTO WORDS
#EX : "I LOVE PYTHON" IN THIS THE WORDS ARE
#I-> WORD1,LOVE->WORD2,PYTHON->WORD3
#EDGE CASES FOR EMPTY ""-> WORDCOUNT=0
#EDGE CASE FOR EMPTY SPACE "    "-> WORDCOUNT=0
#HENCE THIS WORD ARE DIVIDED BY USING WHITE SPACES
#WHITESPACES: \N,\T,"" BY USING THIS THEY DIVIDE

#USING SPLIT METHOD
sentence="I LOVE PYTHON"
word=sentence.split()
count=len(word)
print(count)

#USING MANUAL PROCESS METHOD
sentence="I LOVE PYTHON"
count=0
for i in range(len(sentence)):
    #CURRENT CHARACTER IS NOT SPACE
    if not sentence[i].isspace():
        #FIRST CHARACTER OR PREVIOUS IS SPACE
        if i==0 or sentence[i-1].isspace():
            count+=1
print(count)

#USING COUNT METHOD
sentence="I LOVE PYTHON"
count=sentence.count(" ")+1
print(count)

#USING REGEX METHOD
import re
sentence="I LOVE PYTHON"
words=re.findall(r'\S+',sentence)
print(len(words))

#UsiNG TWO POINTER METHOD
sentence="I LOVE PYTHON"
count=0
i=0
n=len(sentence)
while i<n:
    #SKIP SPACES
    while i<n and sentence[i].isspace():
        i+=1
    #FOUND WORD
    if i<n:
        count+=1
    #SKIP WORD
    while i<n and not sentence[i].isspace():
        i+=1
print(count)
