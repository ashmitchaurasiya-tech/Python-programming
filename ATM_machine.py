# Simple ATM Machine for Beginners
# Simulates basic ATM operations
 
# ── Account Database ──────────────────────────────────────────────
accounts = {
    "1001": {"pin": "1234", "name": "Alice",   "balance": 5000.00},
    "1002": {"pin": "5678", "name": "Bob",     "balance": 3200.50},
    "1003": {"pin": "9999", "name": "Charlie", "balance": 800.75},
}
 
MAX_PIN_ATTEMPTS = 3
 
# ── Helper Functions ──────────────────────────────────────────────
def print_header(title):
    print("\n" + "=" * 35)
    print(f"   🏧  {title}")
    print("=" * 35)
 
def check_balance(account):
    print_header("Balance Enquiry")
    print(f"  Account Holder : {account['name']}")
    print(f"  Current Balance: ${account['balance']:,.2f}")
 
def deposit(account):
    print_header("Deposit")
    try:
        amount = float(input("  Enter deposit amount: $"))
        if amount <= 0:
            print("  ❌ Amount must be greater than zero.")
            return
        account["balance"] += amount
        print(f"  ✅ ${amount:,.2f} deposited successfully!")
        print(f"  New Balance: ${account['balance']:,.2f}")
    except ValueError:
        print("  ❌ Invalid amount entered.")
 
def withdraw(account):
    print_header("Withdrawal")
    try:
        amount = float(input("  Enter withdrawal amount: $"))
        if amount <= 0:
            print("  ❌ Amount must be greater than zero.")
        elif amount > account["balance"]:
            print("  ❌ Insufficient funds!")
            print(f"  Available Balance: ${account['balance']:,.2f}")
        else:
            account["balance"] -= amount
            print(f"  ✅ ${amount:,.2f} dispensed. Please collect your cash.")
            print(f"  Remaining Balance: ${account['balance']:,.2f}")
    except ValueError:
        print("  ❌ Invalid amount entered.")
 
def change_pin(account, card_number):
    print_header("Change PIN")
    old_pin = input("  Enter current PIN: ")
    if old_pin != account["pin"]:
        print("  ❌ Incorrect current PIN.")
        return
    new_pin = input("  Enter new PIN     : ")
    confirm_pin = input("  Confirm new PIN   : ")
    if new_pin != confirm_pin:
        print("  ❌ PINs do not match. Try again.")
    elif len(new_pin) != 4 or not new_pin.isdigit():
        print("  ❌ PIN must be exactly 4 digits.")
    else:
        accounts[card_number]["pin"] = new_pin
        print("  ✅ PIN changed successfully!")
 
def mini_statement(account):
    print_header("Mini Statement")
    print(f"  Account Holder : {account['name']}")
    print(f"  Current Balance: ${account['balance']:,.2f}")
    print("\n  (Full transaction history not available in demo)")
 
# ── Login ─────────────────────────────────────────────────────────
def login():
    print_header("Welcome to PyBank ATM")
    card_number = input("\n  Insert Card (enter account number): ").strip()
 
    if card_number not in accounts:
        print("  ❌ Card not recognised. Exiting.")
        return None, None
 
    account = accounts[card_number]
 
    for attempt in range(1, MAX_PIN_ATTEMPTS + 1):
        pin = input(f"  Enter PIN (attempt {attempt}/{MAX_PIN_ATTEMPTS}): ")
        if pin == account["pin"]:
            print(f"\n  ✅ Welcome back, {account['name']}!")
            return card_number, account
        else:
            print("  ❌ Incorrect PIN.")
 
    print("\n  🔒 Card blocked after 3 failed attempts. Please contact your bank.")
    return None, None
 
# ── Main Menu ─────────────────────────────────────────────────────
def main_menu(card_number, account):
    while True:
        print_header("Main Menu")
        print("  1 → Check Balance")
        print("  2 → Deposit")
        print("  3 → Withdraw")
        print("  4 → Change PIN")
        print("  5 → Mini Statement")
        print("  6 → Exit")
        print("-" * 35)
 
        choice = input("  Select an option: ").strip()
 
        if choice == "1":
            check_balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            change_pin(account, card_number)
        elif choice == "5":
            mini_statement(account)
        elif choice == "6":
            print("\n  Thank you for using PyBank ATM. Goodbye! 👋\n")
            break
        else:
            print("  ❌ Invalid option. Please choose 1–6.")
 
# ── Run the ATM ───────────────────────────────────────────────────
card_number, account = login()
if card_number:
    main_menu(card_number, account)
 