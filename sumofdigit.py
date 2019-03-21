# sum of digit
num=int(input("enter a +ve integer: "))
res=0
n=num
#while num>0:
for i in range(len(str(num))):
    rem=num%10
    res=res+rem
    num=num//10

print("the sum of ",n," is :",res)

