class Account:
    def __init__(self,account_number=12345,balance=100000):
        
        self.account_number=account_number
        self.balance=balance

    def deposit(self,account_address,amount):
         if account_address==self.account_number:
          self.balance+=amount
          print(f'depositing balance={amount}')
          print(f' remaining balance {self.balance}')
         else:
            print('try again')

    def withdraw(self,account_address,amount):
        if account_address==self.account_number:
          if amount>self.balance:
             print('insuficient balance')
          else:
           self.balance-=amount

           print(f'withdrawal balance={amount}')
           print(f' Remaining balace{self.balance}')
        else:
           print('try again')
my_account=Account()
 
my_account.withdraw(12345,80000)#this is an argument which we are giving to the account method


