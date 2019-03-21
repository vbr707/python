num=int(input("enter a +ve integer: "))
a=num
result=0
n=len(str(num))
while(num!=0):
    digit=num%10
    result=result+digit**n
    num=num//10

if a==result:
    print(a," is an armstrong number")
else:
    print(a," is not an armstrong number")