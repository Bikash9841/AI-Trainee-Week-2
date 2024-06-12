from bank_accounts import BankAccount, InterestRewardsAcct, SavingsAcct

# create two bank accounts
b_acc_1 = BankAccount(2700, "Rituram Ojha")
b_acc_2 = BankAccount(3400, "David Miller")

# get balance for both accounts
b_acc_1.getBalance()
b_acc_2.getBalance()

# deposit 500 in the second account
b_acc_2.deposit(500)
b_acc_1.withdraw(1000)

# transfer 500 from the first account to the second account
b_acc_1.transfer(b_acc_1, 500)

# Create an instance of InterestRewardsAcct.
reward_acc = InterestRewardsAcct(0, "David Miller Reward Account")

# Deposit 100 to that instance.
reward_acc.deposit(100)

# Transfer 100 to the above first account.
reward_acc.transfer(b_acc_1, 100)

# Create an instance of SavingsAcct.
saving_acc = SavingsAcct(110, "Harry Savings")

# Transfer 100 to the above second account.
saving_acc.withdraw(100)
