# armstrong or not
num=int(input("enter a +ve integer: "))
i=num
result=0
n=len(str(num))
while(num!=0):
        digit=num%10
        result=result+digit**n
        num=num//10
if i==result:
    print(i," is an armstrong number")
else:
    print(i," is not an armstrong number")