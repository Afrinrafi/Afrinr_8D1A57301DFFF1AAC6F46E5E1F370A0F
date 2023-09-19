class BankAccount:
 def __init__(self, account_number,  account_holder_name,initial_balance=0.0):
   self.__account_number=account_number 
   self.__account_holder_name=account_holder_name
   self.__amount_balance=initial_balance
 def deposit (self,amount):
  if amount>0:
    self.__amount_balance+=amount
    print("Deposited ₹{}.New balance: ₹{}".format(amount,self.__amount_balance))
  else:
    print("Invalid deposit amount.please deposit positive amount.")
  def withdraw(self,amount):
      if amount > 0 and amount<=self.__account_balance:
       self.__account_balance-=amount
       print("withdraw{}.now balance:{}",format (amount,self.__account_balance))
      else:
        print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
        print("Account balance for {} (Account #{}):₹{}".format(self.__account_holder_name, self.__account_number,self.__account_balance))
account=BankAccount(account_number="123456789",account_holder_name="Afrin",initial_balance=98400.)
account.deposit(1000.0)
