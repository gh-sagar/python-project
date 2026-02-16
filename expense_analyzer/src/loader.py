# expense_analyzer/src/loader.py
from typing import List, Dict
import csv
import os

def load_expenses(path: str) -> List[Dict[str, str]]:
    """Load CSV file as a list of dictionaries."""
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV file not found at {path}")
    
    expenses = []
    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(dict(row))
    return expenses

# Optional: test loader directly
if __name__ == "__main__":
    # Adjust relative path if running from src folder
    path = "../src/expenses.csv"
    print(load_expenses(path))
