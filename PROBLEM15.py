#DISARIUM NUMBER 
#DISARIUM NUMBER MEANS LET WE TAKE A NUMBER
#AND WE WILL RAISE TO ITS ORDER WITH POWER AND ADD
#IF THE RAISE POWER IS EQUAL TO ORIGINAL NUMBER
#THEN SUCH NUMBER IS CALLED DISARIUM NUMBER
#FOR EXAMPLE:135 -> 1*1+3*2+5*3 -> 1+9+125 = 135
#HENCE SUCH NUMBER IS CALLED DISARIUM NUMBER 

#USING STRING TRAVERSAL METHOD
def di_num(n):
    if n<0:
        return "NEGATIVE NUMBER"
    total=0
    #CONVERT NUMBER INTO STRING
    s=str(n)
    #TRAVERSE DIGITS
    for i in range(len(s)):
        digit=int(s[i])
        #POSITION I+1
        total+=digit**(i+1)
    if total==n:
        return "DISARIUM NUMBER"
    return "NOT A DISARIUM NUMBER"
print(di_num(135))

#USING RECURSION METHOD
def helper(n,pos):
    if n==0:
        return 0
    digit=n%10
    return (digit**pos)+helper(n//10,pos-1)
def di_num(n):
    if n<0:
        return "NEGATIVE NUMBER"
    digits=len(str(n))
    total=helper(n,digits)
    if total==n:
        return "DISARIUM NUMBER"
    return "NOT A DISARIUM NUMBER"
print(di_num(135))