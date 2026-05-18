#COUNT NUMBER OF DIGITS

#USING WHILE LOOP METHOD

num=int(input("enter a number"))
num=abs(num)
if num==0:
    count=1
else:
    count=0
    while num >0:
        num=num//10
        count+=1
print("TOTAL COUNT: ",count)


#USING STR LENGTH

num=int(input("enter a number"))
count=len(str(abs(num)))
print("TOTAL COUNT: ",count)