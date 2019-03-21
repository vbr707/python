num=int(input("enter a +ve integer: "))
rev=0
a=num
while num>0:
    rem=num%10
    num=num//10
    rev=rev*10+rem
print(rev)
if a==rev:
    print(a," is palindrome.")
else:
    print(a,"is not a palindrome")