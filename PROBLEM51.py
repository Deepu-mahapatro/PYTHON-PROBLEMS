#FIND ALL PALINDROME SUBSTRINGS
#TO FIND EVERY SUBSTRING THAT READS
#THE SAME FORWARD AND BACKWARD
#CORE IDEA:
      #A PALINDROME READS THE SAME
      #FROM LEFT TO RIGHT AND RIGHT TO LEFT
      #EVERY PALINDROME HAS A CENTER
      #PICK EACH POSITION AS A POSSIBLE CENTER
      #EXPAND OUTWARD FROM THE CENTER
      #IF LEFT AND RIGHT CHARACTERS MATCH
      #A PALINDROME EXISTS
      #CONTINUE EXPANDING UNTIL
      #CHARACTERS NO LONGER MATCH
      #CHECK BOTH ODD AND EVEN LENGTH PALINDROMES
#EDGE CASES:
      #EMPTY STRING -> RETURN EMPTY RESULT
      #SINGLE CHARACTER -> CHARACTER ITSELF IS A PALINDROME
      #NO LARGE PALINDROMES -> ONLY SINGLE CHARACTERS
      #ALL SAME CHARACTERS -> MANY PALINDROMES EXIST
      #ODD LENGTH PALINDROMES -> "ABA", "MADAM"
      #EVEN LENGTH PALINDROMES -> "AA", "ABBA"
      #CASE SENSITIVITY DEPENDS ON REQUIREMENTS
      #SPACES AND SPECIAL CHARACTERS
      #DEPEND ON REQUIREMENTS
#KEY OBSERVATION:
      #EVERY SINGLE CHARACTER
      #IS A PALINDROME
      #A PALINDROME GROWS SYMMETRICALLY
      #AROUND ITS CENTER
      #IF LEFT AND RIGHT CHARACTERS MATCH
      #KEEP EXPANDING
#CONCLUSION:
#VISIT EACH POSSIBLE CENTER.
#EXPAND LEFT AND RIGHT.
#WHEN CHARACTERS MATCH,
#A PALINDROME IS FOUND.
#STORE THE PALINDROME.
#CONTINUE UNTIL EXPANSION FAILS.
#REPEAT FOR ALL CENTERS.
#RETURN ALL PALINDROME SUBSTRINGS.

#BRUTE FORCE APPROACH
def is_palindrome(s):
    return s==s[::-1]
def find_all_palindromes(text):
    #EDGE CASE
    if not text:
        return []
    result=[]
    n=len(text)
    #GENERATE ALL SUBSTRINGS
    for start in range(n):
        for end in range(start,n):
            substring=text[start:end+1]
            #CHECK PALINDROME
            if is_palindrome(substring):
                result.append(substring)
    return result
text="ababa"
print(find_all_palindromes(text))

#GENERATE ALL SUBSTRING + REVERSE CHECK
def find_all_palindromes(s):
    #EDGE CASE
    if not s:
        return []
    result=[]
    n=len(s)
    for start in range(n):
        for end in range(start,n):
            substring=s[start:end+1]
            #CHECK PALINDROME
            if substring==substring[::-1]:
                result.append(substring)
    return result
s="ababa"
print(find_all_palindromes(s))

#EXPAND AROUND CENTER METHOD
def find_all_palindromes(s):
    #EDGE CASE
    if not s :
        return []
    result=[]
    n=len(s)
    #FUNCTION TO EXPAND FROM CENTER
    def expand(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            #PALINDROME FOUND
            result.append(s[left:right+1])
            #EXPAND FURTHER
            left-=1
            right+=1
    #CHECK EVERY POSSIBLE CENTER
    for center in range(n):
        #ODD LENGTH PALINDROME
        expand(center,center)
        #EVEN LENGTH PALINDROME
        expand(center,center+1)
    return result
s="ababa"
print(find_all_palindromes(s))