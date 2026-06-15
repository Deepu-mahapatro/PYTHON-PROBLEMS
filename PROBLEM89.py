#REVERSE A STRING USING RECURSION
#CORE IDEA:
#REVERSE STRING USING RECURSIVE CALLS
#EDGE CASES:
#EMPTY STRING
#SINGLE CHARACTER
#PALINDROME STRING
#SPECIAL CHARACTERS
#EXAMPLE:
#INPUT="HELLO"
#OUTPUT="OLLEH"
#APPROACH 1(SIMPLE RECURSION):
#BASE CASE:
#LEN(S)==0
#RETURN ""
#RECURSIVE CASE:
#REVERSE(S[1:])+S[0]
#APPROACH 2(TWO POINTER RECURSION):
#SWAP LEFT AND RIGHT
#MOVE POINTERS INWARDS
#BASE CASE:
#LEFT>=RIGHT
#RETURN
#TIME COMPLEXITY:
#SIMPLE RECURSION->O(N²)
#TWO POINTER RECURSION->O(N)
#SPACE COMPLEXITY:
#BOTH->O(N)
#BEST SOLUTION:
#TWO POINTER RECURSION

#MOST INTERVIEWERS EXPECT:
#TWO POINTER RECURSION

#NORMAL METHOD
def reverse_string(s):
    #BASE CASE
    if len(s)==0:
        return ""
    #REVERSE REMAINING STRING AND ADD FIRST CHARACTER AT ALST
    return reverse_string(s[1:])+s[0]
print(reverse_string("HELLO"))

#RECURSION USING START AND END POINTERS (TWO POINTERS)
def reverse_string(s):
    chars=list(s)
    def method(left,right):
        #BASE CASE
        if left>=right:
            return 
        #SWAP CASE
        chars[left],chars[right]=chars[right],chars[left]
        #RECURSIVE CALL
        method(left+1,right-1)
    method(0,len(chars)-1)
    return "".join(chars)
print(reverse_string("HELLO"))

