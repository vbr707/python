from firebase.firebase import FirebaseApplication
import time
fire=FirebaseApplication("https://project2-c28f8.firebaseio.com/")
#res=fire.put("User","user",{"username":'raju',"password":'raju@123'})
res=fire.get("User","user")
#print(res)
username = input("enter username:")
password = input("enter password:")
print("please wait validating...")
#time.sleep(5)
if res:
    if username in res.values() and password in res.values():
        print("welcome")
        #if password in res.values():
         #   print("succesfully login")
    else:
       print("hint:invalid username/password")
#else:
 #   print("no data for users")