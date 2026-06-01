#CONVERT CAMEL CASE TO SNAKE CASE OR PASCAL CASE
#TO CONVERT A CAMEL CASE OR PASCAL CASE STRING INTO SNAKE CASE
#CORE IDEA:
      #TRAVERSE THE STRING CHARACTER BY CHARACTER
      #LOWERCASE LETTERS ARE ADDED AS THEY ARE
      #UPPERCASE LETTERS INDICATE A NEW WORD
      #ADD "_" BEFORE THEM
      #CONVERT THEM TO LOWERCASE
#EDGE CASES:
      #EMPTY STRING -> RETURN EMPTY STRING
      #SINGLE CHARACTER -> RETURN LOWERCASE
      #ALREADY SNAKE CASE -> NO CHANGE
      #PASCAL CASE -> NO LEADING "_"
      #NUMBERS REMAIN UNCHANGED
      #CONSECUTIVE CAPITAL LETTERS DEPEND ON REQUIREMENTS
#KEY OBSERVATION:
      #EVERY UPPERCASE LETTER REPRESENTS
      #THE START OF A NEW WORD
#CONCLUSION:
#INSERT "_" BEFORE EACH NEW WORD
#AND CONVERT ALL CHARACTERS TO LOWERCASE
#TO OBTAIN THE SNAKE CASE STRING.

#BRUTE FORCE APPROACH
def camel_to_snake(s):
    #EDGE CASE:
    if not s:
        return ""
    result=""
    for ch in s:
        #IF UPPERCASE LETTER FOUND
        if ch.isupper():
            #AVOID LEADING "_"
            if result:
                result+="_"
            #CONVERT TO LOWERCASE
            result+=ch.lower()
        else:
            result+=ch
    return result
s="studentName"
print(camel_to_snake(s))

#USING LIST METHOD
def camel_to_snake(s):
    #EDGE CASE:
    if not s:
        return ""
    result=[]
    for ch in s:
        if ch.isupper():
            if result:
                result.append("_")
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)
s="studentName"
print(camel_to_snake(s))

#USING ENUMERATE METHOD
def camel_to_snake(s):
    result=[]
    for i,ch in enumerate(s):
        if ch.isupper():
            if i!=0:
                result.append("_")
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)
s="StudentName"
print(camel_to_snake(s))