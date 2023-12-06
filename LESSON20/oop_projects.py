from bank_accounts import * # * means all

Jackson = BankAccount(1000, "Jackson")
Kathleen = BankAccount(2000, "Kathleen")

Jackson.getBalance()
Kathleen.getBalance()

Kathleen.deposit(500)

Jackson.withdraw(10000)
Jackson.withdraw(10)

Jackson.transfer(10000, Kathleen)
Jackson.transfer(100, Kathleen)

Edgar = InterestRewardsAcct(1000, "Edgar")

Edgar.getBalance()

Edgar.deposit(100)

Edgar.transfer(100, Jackson)

Jasson = SavingsAcct(1000, "Jasson")

Jasson.getBalance()

Jasson.deposit(100)

Jasson.transfer(10000, Kathleen)
Jasson.transfer(1000, Kathleen)