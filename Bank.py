class Bank:
  def __init__(self,Account_holder_name,Account_number,pin,Balance):
    self.Account_holder_name=Account_holder_name
    self.Account_number=Account_number
    self.pin=pin
    self.Balance=Balance
    self.transaction_history=[]
  def verify_pin(self):
    Enter_pin =int(input("Enter your pin: "))
    return Enter_pin==self.pin
  def Deposit(self,Amount):
    if Amount<=0:
      print("Enter Valid amount...!!!")
    else:
      self.Balance+=Amount
      self.transaction_history.append(f"Credited {Amount}")
      print(f"\n{Amount} deposited in your account. \nAvl Bal is {self.Balance}")
  def Withdraw(self,Amount):
    if Amount<=0:
      print("Enter Valid amount")
    elif Amount<=self.Balance:
      self.Balance-=Amount
      self.transaction_history.append(f"Debited {Amount}")
      print(f"\nYour account is debited with {Amount}. \nAvl Bal is {self.Balance}")
    elif Amount>self.Balance:
      print("\nInsufficient Funds in Your Account")
    else:
      print("Invalid Input")
  def Statement(self):
    if len(self.transaction_history)==0:
      print("No Transactions....!!!!!")
    else:
      print("Your Transaction History...")

      for transaction in self.transaction_history:
       print("",transaction)
  def Check_balance(self):
    print(f"Current Bal : {self.Balance}")
accounts={
    101:Bank("Siva",101,4264,10000),
    102:Bank("Rahul",102,9494,5000),
    103:Bank("Vineela",103,5959,20000)
}

while True:
  try:
    account_number= int(input("Enter Your Account number: "))
  except ValueError:
    print("Enter Only numbers ")
    continue
  except KeyboardInterrupt:
    print("Transaction Ended")
    break

  if account_number not in accounts:
    print("Account not found...!!!")
    continue
  account =accounts[account_number]
  print(f"\nWelcome Mr/Mrs {account.Account_holder_name}")
  print("\nWelcome to SBI\n")
  print("1-Check Balance")
  print("2-Deposit")
  print("3-Withdraw")
  print("4-Statement")
  print("5-Cancel the Transaction")
  try:
    option = int(input("Enter Your Option: "))
  except ValueError:
    print("Enter Numbers only\n")
    continue
  except KeyboardInterrupt:
    print("Transaction Ended")
    break
  if option == 1:
    if account.verify_pin():
      account.Check_balance()
      break
    else:
      print("Incorrect PIN...!!!!")
  elif option == 2:
    if account.verify_pin():
      try:
        amount=int(input("Enter Amount: "))
        account.Deposit(amount)
      except ValueError:
        print("Enter numbers Only\n")
    else:
      print("Incorrect PIN....!!!")
  elif option ==3:
    if account.verify_pin():
      try:
        amount=int(input("Enter Amount: "))
        account.Withdraw(amount)
      except ValueError:
        print("Enter Only numbers")
    else:
      print("Incorrect PIN")
  elif option == 4:
    if account.verify_pin():
      account.Statement()
    else:
      print("Incorrect PIN....!!!!")
  elif option ==5:
    print("Last Transaction Cancelled...!!!")
    break
  else:
    print("Enter Valid option")
