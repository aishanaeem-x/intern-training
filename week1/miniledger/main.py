from account import BankAccount
def main():
    name=input("Enter account name:")
    acc= BankAccount(name)
    while True:
        print("\nMENU:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Transaction History")
        print("5. Quit")
        action = input("Choose: ")
        match action:
            case "1":
                amount=int(input("Enter amount to deposit:"))
                acc.deposit(amount)
            case "2":
                amount=int(input("Enter amount to withdraw:"))
                acc.withdraw(amount)
            case"3":
                acc.show_balance()
            case "4":
                acc.show_history()
            case "5":
                print("Quiting...")
                break
            case _:
                print("Enter valid choice(1,2,3,4)")
if __name__ == "__main__":
    main()
   
        