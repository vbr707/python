n=int(input("NO:"))
a=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==a:
    print(a," is perfect")
else:
    print(a," is not perfect")