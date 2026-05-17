num=int(input("enter a number"))
original=num
sum=0
while num>0:
    digits=num%10
    sum=sum+digits**3
    num=num//10
if original==sum:
    print("ARMSTRONG NUMBER")
else:
    print("NOT AN ANAGRAM NUMBER")