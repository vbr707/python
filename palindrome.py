string=input("enter the string: ")
rev=string[::-1]
print("reverse of the given string is: ",rev)
if string==rev:
    print("given string is palindrome")
else:
    print("given string is not a palindrome")

