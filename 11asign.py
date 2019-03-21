tm=int(input("enter total marks: "))

if tm>360:
    print("first class")
elif tm>=300 and tm<360:
    print("second class")
elif tm<300:
    print("third class")