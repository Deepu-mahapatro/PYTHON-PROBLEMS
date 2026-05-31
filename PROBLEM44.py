#REVERSE ONLY VOWELS IN A STRING
#REVERSE THE POSITIONS OF ONLY VOWELS IN A STRING WHILE 
#KEEPING ALL NON-VOWEL CHARACTERS IN THEIR POSITIONS
#PURPOSE
# REVERSE THE ORDER OF VOWELS
# WITHOUT CHANGING THE POSITION OF NON-VOWELS.
#VOWELS
# A, E, I, O, U
# a, e, i, o, u
#PROCESS
# 1. START ONE POINTER FROM LEFT.
# 2. START ONE POINTER FROM RIGHT.
# 3. MOVE LEFT POINTER UNTIL A VOWEL IS FOUND.
# 4. MOVE RIGHT POINTER UNTIL A VOWEL IS FOUND.
# 5. SWAP THE TWO VOWELS.
# 6. MOVE BOTH POINTERS TOWARD THE CENTER.
# 7. REPEAT UNTIL POINTERS CROSS.
# 8. RETURN THE MODIFIED STRING.
#KEY IDEA
# ONLY VOWELS MOVE.
# ALL OTHER CHARACTERS STAY IN THEIR ORIGINAL POSITIONS.

#USING TWO POINTERS METHOD
def reverse_vowels(s):
    vowels=set("aeiouAEIOU")
    #STRINGS ARE IMMUTABLE
    char=list(s)
    left=0
    right=len(char)-1
    while left<right:
        #FIND LEFT VOWEL
        while left<right and char[left] not in vowels:
            left+=1
        #FIND RIGHT VOWEL
        while left<right and char[right] not in vowels:
            right+=1
        #SWAP VOWELS
        char[left],char[right]=char[right],char[left]
        left+=1
        right-=1
    return ''.join(char)
print(reverse_vowels("HELLO"))

#USING EXTRACT+REVERSE+REPLACE METHODS
def reverse_vowels(s):
    vowels=set("aeiouAEIOU")
    char=list(s)
    vowel_list=[]
    #COLLECT VOWELS
    for ch in char:
        if ch in vowels:
            vowel_list.append(ch)
    #REVERSE VOWELS
    vowel_list.reverse()
    index=0
    #REPLACE THE VOWELS
    for i in range(len(char)):
        if char[i] in vowels:
            char[i]=vowel_list[index]
            index+=1
    return ''.join(char)
print(reverse_vowels("HELLO"))

#BRUTE FORCE APPROACH 
def reverse_vowels(s):
    vowels=set("aeiouAEIOU")
    char=list(s)
    positions=[]
    #STORE POSITIONS
    for i in range(len(char)):
        if char[i] in vowels:
            positions.append(i)
    left=0
    right=len(positions)-1
    while left<right:
        i=positions[left]
        j=positions[right]
        char[i],char[j]=char[j],char[i]
        left +=1
        right-=1
    return ''.join(char)
print(reverse_vowels("HELLO"))