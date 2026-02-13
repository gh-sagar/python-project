from loader import load_expenses

def normalize_expense(expense_dict: dict) -> dict:
    
    return {
        "date": expense_dict["date"],
        "category": expense_dict["category"].lower(),
        "amount": float(expense_dict["amount"])
    }

def clean_expenses(expenses: list) -> list:
    return list(map(normalize_expense, expenses))

path=r"/home/mrrobot/Desktop/PYTHON-PROJECT/expense_analyzer/data/expenses.csv"
raw_expenses = load_expenses(path)
cleaned_expenses = clean_expenses(raw_expenses)
if __name__ == "__main__":
   print(cleaned_expenses)
