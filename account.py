balance=20000
pin=int(input("enter pin no: "))
if pin == 5745:
    print("welcome")
    amt=int(input("enter amount: "))
    if amt%100==0:
        if amt<=10000:
                balance=balance-amt
                print("withdraw done")
                print("balance amount is: ",balance)
        else:
            print("limit ",10000," only")
    else:
        print("please enter valid amount")
else:
    print("invalid pin number")