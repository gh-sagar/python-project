from typing import List, Dict
import csv

def load_expenses(path: str) -> List[Dict[str, str]]:
    """Reads a CSV file and returns a list of dictionaries."""
    expenses = []
    
    # Open the CSV safely
    with open(path, newline='') as file:
        reader = csv.DictReader(file)  # Automatically uses header row
        for row in reader:
            expenses.append(dict(row))  # Convert OrderedDict to normal dict
    
    return expenses

# Optional: test loader directly
if __name__ == "__main__":
    path = "expense_analyzer/data/expenses.csv"  # Relative path
    result = load_expenses(path)
    print(result)
