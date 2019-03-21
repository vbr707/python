num=int(input("enter positive integer: "))
for i in range(2,num//2):

     if num%i==0:
         print(num," is not a prime")
         break
else:
    print(num," is a prime number")