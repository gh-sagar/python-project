from loader import load_expenses
import csv  # Make sure loader.py reads CSV using csv module

def normalize_expense(expense_dict: dict) -> dict:
    return {
        "date": expense_dict["date"],
        "category": expense_dict["category"].lower(),
        "amount": float(expense_dict["amount"])
    }

def clean_expenses(expenses: list) -> list:
    return list(map(normalize_expense, expenses))

# Use relative path for Docker compatibility
path = "expense_analyzer/data/expenses.csv"

# Load CSV correctly
raw_expenses = load_expenses(path)
cleaned_expenses = clean_expenses(raw_expenses)

if __name__ == "__main__":
    for expense in cleaned_expenses:
        print(expense)
