# CHECK PRIME NUMBER

nums=int(input("enter a number"))
if nums<=1:
    print("not a prime number")
else:
    for i in range(2,nums):
        if nums%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")
        
#FOR A GIVEN RANGE START TO END
start=int(input("enter a number"))
end=int(input("enter b number"))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)