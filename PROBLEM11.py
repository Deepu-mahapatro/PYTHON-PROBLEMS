#NEON NUMBER CHECK 
#NEON NUMBER MEANS TAKE A NUMBER 9
#SQUARE THE NUMBER 81
#ADD TEH ELEMENTS 8+1=9
#EQUAL TO TEH ORIGINAL NUMBER 9=9
#HENCE IT IS CALLED NEON NUMBER

#BASIC MATHEMATICAL LOGIC
num=int(input("enter a number"))
square=num*num
sum=0
while square>0:
    digit=square%10
    sum+=digit
    square=square//10
if sum==num:
    print("neon number")
else:
    print("non neon number")
    
#USING STRING CONVERSION METHOD
num=int(input("enter a number"))
s=num**2
sum=0
for i in str(s):
    sum=sum+int(i)
if sum==num:
    print("neon number")
else:
    print("non neon number")
    
#BEST VERSION METHOD
def is_neon(num):
    if num<0:
        return False
    square=num**2
    sum=0
    if square==0:
        sum=0
    while square>0:
        sum+=square%10
        square//=10
    return sum==num
num=int(input("enter a number"))
if is_neon(num):
    print("neon number")
else:
    print("non neon number")