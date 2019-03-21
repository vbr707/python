from firebase.firebase import FirebaseApplication
fire=FirebaseApplication("https://project1-5c3d3.firebaseio.com/")
d={
    "name":"ravi",
    "salary":125000.00,
    "contact":8500684100}
res=fire.put("employee",102,d)
print(res)