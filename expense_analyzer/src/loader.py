from typing import List, Dict
import csv

# Use relative path for Docker compatibility
path = "expense_analyzer/data/expenses.csv"

def load_expenses(path: str) -> List[Dict[str, str]]:
    expenses = []
    
    # Open the CSV file properly
    with open(path, newline='') as file:
        reader = csv.DictReader(file)  # Automatically uses header row
        for row in reader:
            expenses.append(dict(row))  # Convert OrderedDict to normal dict
    
    return expenses

if __name__ == "__main__":
    result = load_expenses(path)
    print(result)
