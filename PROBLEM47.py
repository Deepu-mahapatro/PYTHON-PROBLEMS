
#TO CONVERT A SNAKE CASE STRING INTO CAMEL CASE
#CORE IDEA:
      #TRAVERSE THE STRING CHARACTER BY CHARACTER
      #NORMAL CHARACTERS ARE ADDED AS THEY ARE
      #"_" INDICATES THE START OF A NEW WORD
      #REMOVE "_"
      #CONVERT THE NEXT CHARACTER TO UPPERCASE
#EDGE CASES:
      #EMPTY STRING -> RETURN EMPTY STRING
      #SINGLE WORD -> NO CHANGE
      #ALREADY CAMEL CASE -> NO CHANGE
      #LEADING "_" -> IGNORE IT
      #TRAILING "_" -> IGNORE IT
      #MULTIPLE "_" TOGETHER -> TREAT AS A SINGLE SEPARATOR
      #NUMBERS REMAIN UNCHANGED
#KEY OBSERVATION:
      #EVERY "_" REPRESENTS
      #A WORD BOUNDARY
#CONCLUSION:
#REMOVE EACH "_"
#AND CAPITALIZE THE CHARACTER IMMEDIATELY AFTER IT
#TO OBTAIN THE CAMEL CASE STRING.

#BRUTE FORCE METHOD
def snake_to_camel(s):
    #EDGE CASE:
    if not s:
        return ""
    result=[]
    i=0
    while i<len(s):
        if s[i]=="_":
            if i+1<len(s):
                result.append(s[i+1].upper())
            i+=2
        else:
            result.append(s[i])
            i+=1
    return ''.join(result)
s="Student_name"
print(snake_to_camel(s))

#USING SPLIT METHOD
def snake_to_camel(s):
    #EDGE CASE:
    if not s:
        return ""
    words=s.split("_")
    result=words[0]
    for word in words[1:]:
        if word:
            result+=word.capitalize()
    return result
s="Student_name"
print(snake_to_camel(s))

#USING LIST + JOIN METHOD
def snake_to_camel(s):
    if not s:
        return ""
    words = s.split("_")
    result = [words[0]]
    for word in words[1:]:
        if word:
            result.append(word.capitalize())
    return "".join(result)
s="Student_name"
print(snake_to_camel(s))

#USING PASCAL VERSION
def snake_to_camel(s):
    #EDGE CASE:
    if not s:
        return ""
    words=s.split("_")
    result=[]
    for word in words:
        result.append(word.capitalize())
    return ''.join(result)
s="Student_name"
print(snake_to_camel(s))