idno=int(input("idno: "))
name=input("name: ")
salary=float(input("salary: "))
contact=int(input("contact: "))

from firebase.firebase import FirebaseApplication
fire=FirebaseApplication("https://project1-5c3d3.firebaseio.com/")
d={
    "name":name,
    "salary":salary,
    "contact":contact}
res=fire.get("employee",idno)
if res == None:
    res=fire.put("employee",idno,d)
    print("employee ",idno," inserted")
else:
    print("employee with ",idno," is exist")

