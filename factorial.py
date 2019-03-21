number=int(input("enter a +ve number:"))
fact=1
for i in range(number,0,-1):
    fact=fact*i

print("factorial of ",number,"is: ",fact)