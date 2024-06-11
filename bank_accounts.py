class BankAccount:

    def __init__(self, initialAmount, accName):

        self.initialAmount = initialAmount
        self.accName = accName

        print(
            f"The bank account named {self.accName} has been initialized with Rs.{initialAmount}. Thank you !")
        print("")

    def getBalance(self):
        print(
            f"The current balance in the account named {self.accName} is {self.initialAmount}")
        print("--------------------------------------------------------------------------------")

    def deposit(self, deposit_amt):
        self.initialAmount += deposit_amt
        self.getBalance()

    def check_withdrawal_validity(self, amt):
        if self.initialAmount >= amt:
            return True
        else:
            return False

    def withdraw(self, withdraw_amt):

        if self.check_withdrawal_validity(withdraw_amt):
            self.initialAmount -= withdraw_amt
        else:
            print("Sorry! You don't have enough fund.")

    def transfer(self, b_acc, t_amt):
        if self.check_withdrawal_validity(t_amt):
            b_acc.initialAmount += t_amt
            self.initialAmount -= t_amt
        else:
            print("Sorry! You don't have enough fund.")


class InterestRewardsAcct(BankAccount):
    def __init__(self, initialAmount, accName):
        super.__init__(initialAmount, accName)

    def deposit(self, deposit_amt):
        self.initialAmount += deposit_amt+0.05*deposit_amt
        self.getBalance()
