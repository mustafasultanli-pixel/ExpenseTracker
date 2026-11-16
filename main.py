from expenses import addExpenses
from validation import CATEGORIES
from reports import *

def showMenu():
    print("="*40)
    print("            EXPENSE TRACKER           ")
    print("="*40)
    print()

    print("""
    
    1. Add Expenses
    2. Show All Expenses
    3. Edit Expense
    4. Delete Expense
    5. Search Expense
    6. Show Total Expenses
    7.Show Categories
    8. Export to CSV

    0.Exit
    
    """)

    print("=" * 40)
def startApp():
    while True:
        showMenu()

        choice = int(input("enter choice."))

        try:
            if choice == 1:
                title = input("enter expense title:")
                amount = input("enter expense amount:")
                category = input("enter expense category:")

                expense = addExpenses("title, amount, category")
                print("Expense added successfully!")
                print("Expense ID:", expense["id"])
        except ValueError:
            print("Enter a number please!")

        

            