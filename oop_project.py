from bank_accounts import BankAccount, InterestRewardsAcct

# create two bank accounts
b_acc_1 = BankAccount(10, "Rituram Ojha")
b_acc_2 = BankAccount(10, "Rajesh Dai")

# get balance for both accounts
b_acc_1.getBalance()
b_acc_2.getBalance()

# deposit 500 in the second account
b_acc_2.deposit(500)
b_acc_1.withdraw(1000)

# transfer 500 from the first account to the second account
b_acc_1.transfer(b_acc_1, 500)


# reward_acc =
