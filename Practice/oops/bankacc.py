class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount 
        print(f"Rs.{amount} deposited by {self.owner}\nBalance: {self.balance} ")


    def withdraw(self,amount):
        if (amount > self.balance):
            print("Insufficient Fund!!")
        else:   
            self.balance -= amount 
            print(f"Rs.{amount} withdrawed by {self.owner}\nBalance: {self.balance} ")

    def get_balance(self):
        return self.balance  

acc1 = BankAccount("Ramu", 1000)
acc2 = BankAccount("Shyam")       # balance 0 se start hoga

acc1.deposit(500)                  # Rs.500 deposited. New balance: Rs.1500
acc1.withdraw(200)                 # Rs.200 withdrawn. New balance: Rs.1300
acc1.withdraw(5000)                # Insufficient balance!
print(acc1.get_balance())          # 1300
print(acc2.get_balance())          # 0