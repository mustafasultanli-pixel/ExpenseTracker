
from expenses import *
from reports import *


def showMenu():
    print("=" * 40)
    print("            EXPENSE TRACKER           ")
    print("=" * 40)

    print("""
    1. Add Expenses
    2. Show All Expenses
    3. Edit Expense
    4. Delete Expense
    5. Search Expense
    6. Show Total Expenses

    0. Exit
    """)

    print("=" * 40)


def startApp():
    while True:
        showMenu()

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                title = input("Enter expense title: ")
                amount = input("Enter expense amount: ")
                category = input("Enter expense category: ")

                expense = addExpenses(title, amount, category)

                print("Expense added successfully!")
                print("Expense ID:", expense["id"])

            elif choice == 2:
                expenses = getAllExpenses()

                if not expenses:
                    print("No expenses found!")
                else:
                    for e in expenses:
                        print("-" * 40)
                        print("ID:", e["id"])
                        print("Title:", e["title"])
                        print("Amount:", e["amount"])
                        print("Category:", e["category"])
                        print("Date:", e["date"])

            elif choice == 3:
                expenseID = input("Enter expense ID to edit: ")

                expense = searchExpense(expenseID)
                print("Current expense:", expense)

                title = input("Enter new title: ")
                amount = input("Enter new amount: ")
                category = input("Enter new category: ")

                updated = updateExpenses(
                    expenseID, title, amount, category
                )

                print("Expense updated successfully!")
                print(updated)

            elif choice == 4:
                expenseID = input("Enter expense ID to delete: ")

                deleteExpense(expenseID)
                print("Expense deleted successfully!")

            elif choice == 5:
                expenseID = input("Enter expense ID to search: ")

                expense = searchExpense(expenseID)

                print("Expense found!")
                print("ID:", expense["id"])
                print("Title:", expense["title"])
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                print("Date:", expense["date"])

            elif choice == 6:
                total = totalExpenses()
                print("Total Expenses:", total)

            elif choice == 0:
                print("Exiting Expense Tracker...")
                break

            else:
                print("Invalid choice!")

        except ValueError as e:
            print("Error:", e)

        except LookupError as e:
            print("Error:", e)


if __name__ == "__main__":
    startApp()
