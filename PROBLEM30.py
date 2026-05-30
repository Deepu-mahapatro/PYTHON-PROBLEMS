#TOGGLE CASE OF A STRING
#TOGGLE MEANS CONVERT ONE INTO ANOTHER
#FOR UPPERCASE-> CONVERT TO LOWERCASE
#FOR LOWERCASE-> CONVERT INTO UPPERCASE
#OTHER WISE KEEP CHARACTER SAME UNCHANGED

#USING BUILT IN SWAPCASE() METHOD
text="PYthon123"
result=text.swapcase()
print(result)

#USING ISUPPER AND ISLOWER METHODS
text="PYThon123"
result=""
for ch in text:
    if ch.isupper():
        result+=ch.lower()
    elif ch.islower():
        result+=ch.upper()
    else:
        result+=ch
print(result)
    
#USING ASCII VALUES METHOD
text="PYThon123"
result=""
for ch in text:
    ascii_value=ord(ch)
    #FOR UPPERCASE
    if 65<=ascii_value<=90:
        result+=chr(ascii_value+32)
    #FOR LOWERCASE
    elif 97<=ascii_value<=122:
        result+=chr(ascii_value-32)
    else:
        result+=ch
print(result)

#USING LIST + JOIN METHOD
text="PYThon123"
result=[]
for ch in text:
    if ch.isupper():
        result.append(ch.lower())
    elif ch.islower():
        result.append(ch.upper())
    else:
        result.append(ch)
final_result="".join(result)
print(final_result)

#USING BIT MANIPULATION METHOD
text = "PyThon123`"
result = ""
for ch in text:
    if ch.isalpha():
        result += chr(ord(ch) ^ 32)
    else:
        result += ch
print(result)