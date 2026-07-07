from datetime import datetime
import storage

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        self.transactions=[]
        self.filename=f"{owner}_account.json"
        self.load()

    def save(self):
        storage.save(self.filename,{"owner":self.owner,"balance": self.balance,"transactions":self.transactions})
        

    def load(self):
        data= storage.load(self.filename)
        if data:
            self.balance= data["balance"]
            self.transactions=data.get("transactions",[])
            print(f"Account loaded. balance: {self.balance}")
    
    def deposit(self,amount):
        if amount<=0:
            print("Amount must be positive")
            return
        self.balance+=amount
        self.transactions.append({
            "type": "deposit",
            "amount":amount,
            "balance_after":self.balance,
            "time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save()
        print(f"Deposited {amount}. New Balance:{self.balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive")
            return
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        self.transactions.append({
            "type": "withdrawal",
            "amount":amount,
            "balance_after":self.balance,
            "time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save()
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")
    def show_history(self):
        if not self.transactions:
            print("No transactions yet")
            return
        print(f"\n TRANSACTION HISTORY for {self.owner}")
        for t in self.transactions:
            print(f"{t['time']} {t['type'].upper():<12} {t['amount']:<10} Balance:{t['balance_after']}")
