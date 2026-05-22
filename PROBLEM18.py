#FIND ALL FACTORS OF A NUMBER
#A FACTOR IS A NUMBER THAT CNA DIVIDE THE ANOTHER NUMBER PERFECTLY
#MEANS : NO REMAINDER,NO DECIMAL VALUE,EXACT VALUE
#A NUMBER I IS A FACTOR OF N IF-> N%I==0
#IF EQUAL DIVISIONS HAPPEN :
    #FACTOR EXISTS
#IF REMAINDER COMES:
    #FACTOR DOES NOT EXISTS

#USING BRUTE FORCE METHOD
def factors(n):
    #EDGE CASE 
    if n==0:
        return "NEGATIVE NUMBERS"
    #HANDLE NEGATIVE NUMBERS
    n=abs(n)
    print("FACTORS ARE :")
    #CHECK FORM 1 TO N
    for i in range(1,n+1):
        if n%i==0:
            print(i)
factors(12)

#SQUARE ROOT OPTIMIZATION METHOD
import math
def factors(n):
    #ZERO EDGE CASE
    if n==0:
        return "INFINITE NUMBER"
    n=abs(n)
    print("FACTORS ARE :")
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            print(i)
            #AVOID DUPLICATES IN PERFECT SQUARE
            if i!=n//i:
                print(n//i)
factors(36)






#USING WHILE LOOP METHOD
def factors(n):
    if n==0:
        return "INFINITE FACTORS"
    n=abs(n)
    i=1
    while i<=n:
        if n%i==0:
            print(i) 
        i+=1
factors(12)