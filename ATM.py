import time

transactions = []

def view_balance(balance):
    print(f"Your current balance is: {balance}")

def withdraw_amount(balance):
    withdrawal_amt = int(input("How much amount you want to withdraw? "))
    if withdrawal_amt <= balance:
        balance -= withdrawal_amt
        transactions.append(f"Withdrawal: ${withdrawal_amt}")
        print(f"{withdrawal_amt} is debited from your account.")
        print(f"Your current balance is {balance}")
    else:
        print("Insufficient balance.")

def deposit_amount(balance):
    deposit_amt = int(input("How much amount you want to deposit? "))
    balance += deposit_amt
    transactions.append(f"Deposit: ${deposit_amt}")
    print(f"{deposit_amt} is deposited to your account.")
    print(f"Your current balance is {balance}")
    return balance

def transactions_history():
    print("Transactions History")
    for transaction in transactions:
        print(transaction)

def transfer_amount(balance):
    transfer_amt = int(input("How much amount you want to transfer? "))
    if transfer_amt <= balance:
        recipient_account = input("Enter recipient's account number: ")
        # Add code to perform the transfer
        balance -= transfer_amt
        transactions.append(f"Transfer to {recipient_account}: ${transfer_amt}")
        print(f"{transfer_amt} has been transferred to account {recipient_account}.")
        print(f"Your current balance is {balance}")
    else:
        print("Insufficient balance.")

print("WELCOME TO DHCB BANK")
print("Please insert your card details: ")
password = 1234
pin = int(input("Enter your card PIN: "))
balance = 5000

if pin == password:
    while True: 
        print('''
            1 == View Balance
            2 == Withdraw Amount
            3 == Deposit Amount
            4 == Transfer Amount
            5 == Transactions History
            6 == Exit
            ''')
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Please, enter valid choice!")
            continue
        if option == 1:
            view_balance(balance)
        elif option == 2:
            withdraw_amount(balance)
        elif option == 3:
            balance = deposit_amount(balance)
        elif option == 4:
            transfer_amount(balance)
        elif option == 5:
            transactions_history()
        elif option == 6:
            print("Thankyou!")
            break
        else:
            print("Invalid option. Please try again.")

else:
    print("Incorrect PIN entered!")
