def verify_pin(correct_pin):
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == correct_pin:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")
    
    print("Too many incorrect attempts. Transaction blocked.")
    return False

def check_balance(balance):
    print(f"\nYour current balance is: ${balance:.2f}")

def deposit_money(balance, amount):
    if amount <= 0:
        print("Error: You must deposit an amount greater than $0.")
        return balance 
        
    new_balance = balance + amount
    print(f"Successfully deposited: ${amount:.2f}")
    return new_balance

def withdraw_money(balance, amount):
    if amount <= 0:
        print("Error: You must withdraw an amount greater than $0.")
        return balance
        
    if amount > balance:
        print("Error: Insufficient funds! You cannot withdraw more than your balance.")
        return balance 
        
    new_balance = balance - amount
    print(f"Successfully withdrew: ${amount:.2f}")
    return new_balance

def change_pin(current_pin):
    verify = input("Enter your current PIN to authorize change: ")
    if verify != current_pin:
        print("Error: PIN verification failed. PIN change canceled.")
        return current_pin
        
    new_pin = input("Enter your new 4-digit PIN: ").strip()

    if len(new_pin) == 4 and new_pin.isdigit():
        print("PIN changed successfully!")
        return new_pin
    else:
        print("Error: PIN must be exactly 4 digits (numbers only).")
        return current_pin

def main():
    balance = 10000.0  
    pin = "1234"       
    
    print("=== Welcome to the Simple ATM Simulator ===")

    if not verify_pin(pin):
        return

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            check_balance(balance)
            
        elif choice == '2':
            try:
                amount = float(input("Enter deposit amount: $"))
                balance = deposit_money(balance, amount)
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '3':
            try:
                amount = float(input("Enter withdrawal amount: $"))
                balance = withdraw_money(balance, amount)
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '4':
            pin = change_pin(pin)
            
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select an option between 1 and 5.")

if __name__ == "__main__":
    main()