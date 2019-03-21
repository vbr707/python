class bankAccount:
    global name,account_no,typeofacc,balance,deposit,withdraw
    name =input("enter name of the account holder: ")
    account_no =int(input("enter account number: "))
    typeofacc =(input("type of account: "))
    balance =float(input("enter balance: "))
    deposit =float(input("deposit ammount: "))
    withdraw =float(input("withdraw ammount: "))
    def intial(self):
        self.name=name
        self.account_no=account_no
        self.typeofacc=typeofacc
        self.balance=balance
        self.deposit=deposit
        self.withdraw=withdraw


    def dep_ammount(deposit):
        balance+=deposit
        print(balance)

    def with_ammount(withdraw):
        balance-=deposit
        print(balance)

    def disp_name_bal(balance):

        print(name,account_no,balance)

a=bankAccount
