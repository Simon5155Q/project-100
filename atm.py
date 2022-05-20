class atm:
    def _init_(self, cashWithdrawal, balance):
        self.cashWithdrawal = cashWithdrawal
        self.balance = balance

    def PIN():
        print("You now have access to your account")

    def bankBalance(balance):
        print("you currently have ", balance)
    
    def withdrawal(bal, amount):
        bal = bal - amount
        if(bal < amount):
            print("You do not have enough balance in your bank account!")
        else:
            print("you have succesfully withdrawn",amount)

def bank():   
    cardN = 1234567890
    pinNum = 1234
    cardNumber = int(input("Please enter your card number "))
    if(cardNumber == cardN):
        pin = int(input("please enter your PIN "))
        if(pin == pinNum):
            atm.PIN()
        else:
            print("your entered PIN is incorrect, please try again")
            pin = int(input("please enter your PIN "))
    else:
        print("your entered card number is incorrect, please try again")
        cardNumber = int(input("Please enter your card number "))
        if(cardNumber == cardN):
            pin = int(input("please enter your PIN "))
            if(pin == pinNum):
                atm.PIN()
            else:
                print("your entered PIN is incorrect, please try again")
                pin = int(input("please enter your PIN "))
        else:
            exit()


bank()
ballance = 50

while(1 == 1): 
    bankOptions = input("Do you want to withdraw money, check your bank balance or end your interaction? (reply with withdraw, balance or end) ")
    if(bankOptions == "withdraw"):
        withdrawalAmnt = int(input("Enter the withdrawal amount: "))
        ballance -= withdrawalAmnt
        atm.withdrawal(ballance, withdrawalAmnt)
    if(bankOptions == "balance"):
        atm.bankBalance(ballance)

    if(bankOptions == "end"):
        break
    

    
        

    



    


