#PALINDROME CHECK CONCEPT
#A WORD OR A SEQUENCE THAT READS THE SAME BOTH FORWARD AND BACKWARD
#READ FROM LEFT TO RIGHT
#READ FORM RIGHT TO LEFT
#IF BOTH ARE SAME: PALINDROME
#OR ELSE: NOT A PALINDROME
#EDGE CASE: 
    #FOR EMPTY STRING "":RETURN ""
    #FOR SAME CHARACTERS "AA" -> RETURN "AA"
    #IF SPACES ARE INCLUDED NOT A PALINDROME

#REVERSE AND COMPARE METHOD
def reverse_string(s):
    #COVERT TO STRING
    s=str(s)
    result=""
    #REVERSE TEH STRING
    result=s[::-1]
    return s==result
print(reverse_string("oo"))

#USING TWO POINTER METHOD
def is_palindrome(s):
    #CONVERT INTO STRING
    s=str(s)
    if s=="":
        return ""
    #LEFT POINTER
    left=0
    #RIGHT POINTER
    right=len(s)-1
    #COMPARE BOTH SIDES
    while left<right:
        if s[left]!=s[right]:
            return False
        #MOVE POINTERS
        left+=1
        right-=1
    return True
print(is_palindrome("madam"))

#USING LOOP REVERSE STRING METHOD
def is_palindrome(s):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return ""
    #COVERT INTO STRING
    s=str(s)
    #STORE REVERSED STRING
    reverse_str=""
    #TRAVERSE THE LOOP BACKWARD
    for i in range(len(s)-1,-1,-1):
        reverse_str+=s[i]
    #COMPARE
    return s==reverse_str
print(is_palindrome("madam"))

#IGNORE SPACE AND CASE SENSITIVE
def is_palindrome(s):
    #REMOVE SPACES
    s=s.replace(" ","")
    #CONVERT TO LOWERCASE
    s=s.lower()
    #CHECK PALINDROME
    return s==s[::-1]
print(is_palindrome("mada m"))

#USING RECURSIVE METHOD
def is_palindrome(s):
    #CONVERT TO STRING
    s=str(s)
    #EDGE CASE:EMPTY STRING
    if s=="":
        return ""
    #BASE CASE:
    if len(s)<=1:
        return True
    #CHECK FIRST AND LAST
    if s[0]!=s[-1]:
        return False
    #RECURSIVE CHECK
    return is_palindrome(s[1:-1])     
print(is_palindrome("madam"))

#SIMPLE METHOD
#INPUT STRING
s = "madam"
#REVERSE STRING
reverse = s[::-1]
#COMPARE BOTH
if s == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")