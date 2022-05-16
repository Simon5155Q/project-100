class atm:
    def _init_(self, cashWithdrawal, balance):
        self.cashWithdrawal = cashWithdrawal
        self.balance = balance

    def bankBalance(balance):
        print("you currently have ", balance)
    
    def withdrawal(bal, amount):
        if(bal < amount):
            print("You do not have enough balance in your bank account!")
        else:
            print("you have succesfully withdrawn",amount)

bankOptions = input("Do you want to withdraw money or check your bank balance? (reply with withdraw or balance) ")
ballance = 50
if(bankOptions == "withdraw"):
    withdrawalAmnt = int(input("Enter the withdrawal amount: "))
    atm.withdrawal(ballance, withdrawalAmnt)
if(bankOptions == "balance"):
    atm.bankBalance(ballance)




