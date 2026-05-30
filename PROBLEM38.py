#CAESAR CIPHER DECODER
#TAKING EACH CHARACTER IN AN ENCODED MESSAGE
#MOVING (SHIFTING) BACKWARD BY A FIXED NUMBER OF POSITIONS
#REPLACING THE ENCODED LETTER WITH THE ORIGINAL LETTER
#CONDITION:
#NEW POSITION = (OLD POSITION - SHIFT) % 26
#FOR NUMBERS, SPACES AND SYMBOLS ARE UNCHANGED
#EDGE CASE:
    #FOR EMPTY STRING "" -> OUTPUT ""
    #FOR SHIFT 0 OUTPUT IS SAME NO CHANGE
    #FOR SHIFT = 26 SAME INPUT AS OUTPUT
    #IF SHIFT > 26 THEN % IS USED
#TAKE AN ENCODED LETTER AND FIND ITS ALPHABET POSITION
#SUBTRACT SHIFT VALUE AND APPLY MODULUS 26
#CONVERT BACK TO ORIGINAL LETTER
#SPACES, SYMBOLS AND NUMBERS ARE UNCHANGED
#REPEAT FOR ALL CHARACTERS
#FORMULA:
    #DECODED = (CURRENT POSITION - SHIFT) % 26
    
#USING BRUTE FORCE APPROACH
def caesar_decoder(text,shift):
    #STORE DECODED STRING
    result=""
    #HANDLE LARGER SHIFTS
    shift=shift%26
    for char in text:
        #UPPERCASE LETTERS
        if 'A'<=char<='Z':
            old_pos=ord(char)-ord('A')
            new_pos=(old_pos-shift)%26
            new_char=chr(new_pos+ord('A'))
            result+=new_char
        #LOWERCASE LETTERS
        elif 'a'<=char<='z':
            old_pos=ord(char)-ord('a')
            new_pos=(old_pos-shift)%26
            new_char=chr(new_pos+ord('a'))
            result+=new_char
        #FOR OTHER THAN ALPHABETS
        else:
            result+=char
    return result
print(caesar_decoder("KHOOR ZRUOG",3))

#BEST METHOD
def caesar_decoder(text,shift):
    shift%=26
    result=[]
    for char in text:
        if 'A'<=char<='Z':
            result.append(
                chr((ord(char)-ord('A')-shift)%26 + ord('A'))
            )
        elif 'a'<=char<='z':
            result.append(
                chr((ord(char)-ord('a')-shift)%26 + ord('a'))
            )
        else:
            result.append(char)
    return "".join(result)
print(caesar_decoder("KHOOR ZRUOG",3))

#SIMPLEST METHOD
def caesar_decoder(text,shift):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer=""
    for ch in text:
        if ch.isalpha():
            pos=alphabet.index(ch.upper())
            new_pos=(pos-shift)%26
            answer+=alphabet[new_pos]
        else:
            answer+=ch
    return answer
print(caesar_decoder("KHOOR ZRUOG",3))