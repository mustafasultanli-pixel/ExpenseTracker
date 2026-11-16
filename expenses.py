import uuid
from datetime import date
from storage import *
from validation import *
from exceptions import expensesNotFound

# CRUD operations
def addExpenses(title,amount,category):
    expenses = loadExpenses()

    expense = {
        "id": str(uuid.uuid4())[:8],
        "title": validateTitle(title),
        "amount": validateAmount(amount),
        "category": validateCategory(category),
        "date": date.today().isofornat()
    }

    expenses.append(expenses)
    saveExpenses(expenses)

    return expense


def getAllExpenses():
    return loadExpenses()


def searchExpense(expenseID):
    expenses = loadExpenses()

    for e in expenses:
        if e["id"] == expenseID:
            return e
    
    expensesNotFound()


def updateExpenses(expenseID,title,amount,category):
    expenses = loadExpenses()

    for e in expenses:
        if e["id"] == expenseID:
            e["title"] = validateTitle(title)
            e["amount"] = validateAmount(amount)
            e["category"] = validateCategory(category)

            saveExpenses(expenses)

            return e

    expensesNotFound()

def deleteExpense(expenseID):
    expenses= loadExpenses()

    for e in expenses:
        if e["id"] == expenseID:
            expenses.remove(e)

            saveExpenses(expenses)

            return True

    expensesNotFound()

