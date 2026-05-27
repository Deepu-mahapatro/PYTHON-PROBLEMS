#REVERSE A STRING
#MEANS:
      #LAST CHARACTER BECOMES FIRST 
      #FIRST CHARACTER BECOMES LAST
#EX: HELLO -> OLLEH 
#EDGE CASES:
    # FOR EMPTY STRING "" -> OUTPUT : ""
    #FOR SINGLE CHARACTER "A" -> OUTPUT : "A"
    #HERE WE CAN ALSO CHECK PALINDROME

#USING SLICING METHOD
def reverse_string(s):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return ""
    return s[::-1]
print(reverse_string("hello"))

#USING REVERSE LOOP
def reverse_string(s):
    #EDGE CASE : EMPTY STRING
    if s=="":
        return ""
    #EMPTY RESULT STRING
    reverse_str=""
    #TRAVERSE FROM END TO START
    for i in range(len(s)-1,-1,-1):
        reverse_str+=s[i]
    return reverse_str
print(reverse_string("hello"))

#USING TWO POINTERS METHOD
def reverse_string(s):
    if s=="":
        return ""
    #CONVERT STRING INTO LIST
    chars=list(s)
    #LEFT POINTER
    left=0
    #RIGHT POINTER
    right=len(chars)-1
    #SWAP UNTIL POINTERS MEET
    while left<right:
        #SWAP
        chars[left],chars[right]=chars[right],chars[left]
        #MOVE POINTERS
        left+=1
        right-=1
    #CONVERT BACK TO STRING
    return ''.join(chars)
print(reverse_string("hello"))

#USING RECURSION METHOD
def reverse_string(s):
    #EDGE CASE: EMPTY STRING
    if s=="":
        return ""
    #BASE CASE
    if len(s)<=1:
        return s
    return reverse_string(s[1:])+s[0]
print(reverse_string("hello"))
   