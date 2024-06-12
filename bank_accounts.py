from typing import Union


class BankAccount:

    def __init__(self, initialAmount: Union[int, float], accName: str) -> None:

        self.initialAmount = initialAmount
        self.accName = accName

        print(
            f"The bank account named {self.accName} has been initialized with Rs.{initialAmount}. Thank you !")
        print("")

    def getBalance(self) -> None:
        print(
            f"The current balance in the account named {self.accName} is {self.initialAmount}")
        print("--------------------------------------------------------------------------------")

    def deposit(self, deposit_amt: Union[int, float]) -> None:
        self.initialAmount += deposit_amt
        self.getBalance()

    def check_withdrawal_validity(self, amt: Union[int, float]) -> bool:
        if self.initialAmount >= amt:
            return True
        else:
            return False

    def withdraw(self, withdraw_amt: Union[int, float]) -> Union[str, None]:

        if self.check_withdrawal_validity(withdraw_amt):
            self.initialAmount -= withdraw_amt
            print(f"Rs. {withdraw_amt} is withdrawed from the account named {self.accName}")
        else:
            print("Sorry! You don't have enough fund.")

    def transfer(self, b_acc: 'BankAccount', t_amt: Union[int, float]) -> None:
        if self.check_withdrawal_validity(t_amt):
            b_acc.initialAmount += t_amt
            self.initialAmount -= t_amt
        else:
            print("Sorry! You don't have enough fund.")


class InterestRewardsAcct(BankAccount):

    def deposit(self, deposit_amt: Union[int, float]) -> None:
        self.initialAmount += deposit_amt+0.05*deposit_amt
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):

    def __init__(self, initialAmount: Union[int, float], accName: str, fee=5):
        super().__init__(initialAmount, accName)
        self.fee = fee

    def check_withdrawal_validity(self, amt: Union[int, float]) -> bool:
        if (self.initialAmount - amt) > 5:
            return True
        else:
            return False

    def withdraw(self, withdraw_amt: Union[int, float]) -> Union[str, None]:
        if self.check_withdrawal_validity(withdraw_amt):
            self.initialAmount -= withdraw_amt-self.fee

            print(f"Rs. {withdraw_amt} is withdrawed from the account named {self.accName}")
        else:
            print("Sorry! You don't have enough fund.")
