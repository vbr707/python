n=int(input("no:"))
rev=0
a=n
digits=len(str(n))
while n!=0:
   r=n%10
   n=n//10
   rev=rev*10+r
if rev==a:
    print(a," is palindrome")
else:
    print(a," is not a palindrome")