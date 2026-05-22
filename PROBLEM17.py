#HAPPY NUMBER
#TAKE A INPUT NUMBER
#SQUARE EACH DIGIT OIF THE INPUT NUMBER
#NOW ADD THE SQUARE OF EACH DIGITS
#THIS PROCESS CONTINUES LOOP INFINITE TIMES
#UNTIL TEH 1 REACHES 
#IF 1 REACHES AT LAST CALLED HAPPY NUMBER
#OR ELSE IT IS NOT A HAPPY NUMBER

#USING SET METHOD
def happy(n):
    #EDGE CASE 
    if n<0:
        return "NEGATIVE NUMBERS"
    #STORE THE VISITED NUMBERS
    visited=set()
    #REPEAT UNTIL INPUT BECOMES 1
    while n!=1:
        #IF NUMBER REPEATS,LOOP DETECTED
        if n in visited:
            return False
        visited.add(n)
        #FIND SUM OF SQUARE OF DIGITS
        total=0
        while n>0:
            rem=n%10
            total+=rem*rem
            n=n//10
        #UPDATE N
        n=total
    return True
print(happy(19))

#USING FAMOUS DETECTION METHOD
    #FLOYD CYCLE DETECTION ALGORITHM
    #SLOW FAST POINTER METHOD
#IF TWO POINTERS MEET: CYCLE EXITS->NOT A HAPPY
#IF ONE REACHES 1->THEN IT IS A HAPPY NUMBER
def square(n):
    total=0
    while n>0:
        rem=n%10
        total+=rem*rem
        n=n//10
    return total
def happy(n):
    if n<=0:
        return False
    slow=n
    fast=n
    while True:
        slow=square(slow)
        fast=square(square(fast))
        if fast==1:
            return True
        if slow==fast:
            return False
print(happy(19))