'''1. ATM Simulation
   - Create a program to simulate an ATM where users can:
     - Check balance
     - Deposit money
     - Withdraw money
     - Exit
   - Use functions for each operation and implement proper input validation (e.g., insufficient balance for withdrawal).

'''
user_balance = 1000
def check_balance():
    print(f"Your current balance is: {user_balance}")

# Function to deposit money
def deposit():
    global user_balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Please enter a valid amount.")
        else:
            user_balance += amount
            print(f"New balance: {user_balance}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
def withdraw():
    global user_balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > user_balance:
            print("Insufficient balance.")
        else:
            user_balance -= amount
            print(f"Remaining balance: {user_balance}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
def atm_menu():
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("-1. Exit")
while True:
    atm_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "-1":
        print("you have successfully visited your account")
        break
    else:
        print("Invalid choice. Please select a valid option.")