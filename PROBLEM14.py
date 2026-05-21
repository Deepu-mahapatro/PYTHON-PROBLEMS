#AUTOMORPHIC NUMBER
#MEANS TEH NUMBER MUST ENDS WITH SQUARE OF ITS TERM
#FOR 25->25 * 25-> 625-> HENCE 25 ENDS WITH 625
#THIS TYPE OF NUMBER IS CALLED AUTOMORPHIC NUMBER

#USING STRING METHOD ENDSWITH()
def auto_mor(n):
    if n<0:
        return "NEGATIVE NUMBER"
    square=n*n
    if str(square).endswith(str(n)):
        return "AUTOMORPHIC NUMBER"
    return "NOT A AUTOMORPHIC NUMBER"
print(auto_mor(25))

#USING MATHEMATICAL MODULUS METHOD
def auto_mor(n):
    if n<0:
        return "NEGATIVE NUMBER"
    square=n*n
    num=len(str(n))
    last=10**num
    last__num=square%last
    if last__num==n:
        return "AUTOMORPHIC NUMBER"
    return "NOT A AUTOMORPHIC NUMBER"
print(auto_mor(625))

#USING RECURSION METHOD
def check(n,square):
    if n==0:
        return True
    if n%10!=square%10:
        return False
    return check(n//10,square//10)
def auto_mor(num):
    if num<0:
        return "NEGATIVE NUMBER"
    square=num*num
    if check(num,square):
        return "AUTOMORPHIC NUMBER"
    return "NOT A AUTOMORPHIC NUMBER"
print(auto_mor(625))