#KARPREKAR NUMBER 
#TAKE A INPUT NUMBER 
#FIND THE SQUARE OF THAT INPUT
#NOW SPLIT THR SQUARE COMPONENT INTO TWO PARTS
#NOW THE LOGIC IS THE RIGHT PART SHOULD CONTAIN 
#SAME DIGITS OF INPUT NUMBER
#AND THE REMAINING DIGITS ARE MOVED TO LEFT 
#NOW ADD TEH LEFT + RIGHT AS RESULT
#IF RESULT==INPUT NUMBER THEN THOSE NUMBER 
#ARE CALLED KARPREKAR NUMBER
#LOGIC:
     #THE RIGHT PART SHOULD MUST CONTAIN 
     #SAME NUMBER OF DIGITS AS INPUT NUMBER
     #REMAINING DIGITS ARE MOVED TO LEFT 

#USING STRING SLICING METHOD
def karprekar(n):
    #EDGE CASE 
    if n<0:
        return "NEGATIVE NUMBER"
    #SPECIAL CASE FOR 1
    if n==1:
        return True
    #FIND SQUARE
    square=n*n
    square_str=str(square)
    digits=len(str(n))
    #SPLIT THE LEFT AND RIGHT
    left=square_str[:-digits]
    right=square_str[-digits:]
    #IF LEFT PART BECOMES EMPTY
    if left=="":
        left=0
    else:
        left=int(left)
    right=int(right)
    return left+right==n
print(karprekar(45))

#MATHEMATICAL MODULUS METHOD
def karprekar(n):
    #NEGATIVE NUMBER
    if n<0:
        return "NEGATIVE NUMBER"
    #SPECIAL CASE
    if n==1:
        return True
    #SQUARE OF A NUMBER
    square=n*n
    #COUNT DIGITS IN ORIGINAL NUMBER
    digits=len(str(n))
    #CREATE DIVISOR
    divisor=10**digits
    #SPLIT USING MATHEMATICS
    right=square%divisor
    left=square//divisor
    return left+right==n
print(karprekar(45))