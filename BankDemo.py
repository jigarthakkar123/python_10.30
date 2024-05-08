class Bank:
    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello ",self.cname,", Your Account Number ",str(self.acno)," Is opened With ",str(balance)," Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("InSufficient Funds")
    def checkBalance(self):
        print("Current Balance : ",self.balance)
b1=Bank()
cname=input("Enter Customer Name : ")
acno=int(input("Enter Account Number : "))
balance=int(input("Enter Initial Balance : "))
b1.openAccount(cname,acno,balance)

while True:
    print("*****************************************************************")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*****************************************************************")

    choice=int(input("Enter Your Choice : "))
    print("*****************************************************************")
    
    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*****************************************************************")
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*****************************************************************")
    elif choice==3:
        b1.checkBalance()
        print("*****************************************************************")
    elif choice==4:
        print("Thank You For Using Our Services.")
        print("*****************************************************************")
        break
    else:
        print("Invalid Choice. Please Try Again.")
        print("*****************************************************************")
