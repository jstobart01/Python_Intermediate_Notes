from bank_accounts import * # * means all

Jackson = BankAccount(1000, "Jackson")
Kathleen = BankAccount(2000, "Kathleen")

Jackson.getBalance()
Kathleen.getBalance()

Kathleen.deposit(500)

Jackson.withdraw(10000)