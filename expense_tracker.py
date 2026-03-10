import json

file_name = "expenses.json"

try:
    with open(file_name, "r") as file:
        expenses = json.load(file)
except:
    expenses = []

while True:
    print("\n----- SMART EXPENSE TRACKER -----")
    print("1. Add Expense")
    print("2. Show All Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        category = input("Enter category (food/travel/shopping): ")
        amount = float(input("Enter amount: "))

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        with open(file_name, "w") as file:
            json.dump(expenses, file)

        print("Expense saved successfully")

    elif choice == "2":
        print("\nYour Expenses:")
        for e in expenses:
            print(e["name"], "-", e["category"], "-", e["amount"])

    elif choice == "3":
        total = 0
        for e in expenses:
            total += e["amount"]

        print("Total Expense:", total)

    elif choice == "4":
        print("Program Closed")
        break