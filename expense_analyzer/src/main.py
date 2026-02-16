# expense_analyzer/src/main.py
from loader import load_expenses
from cleaner import clean_expenses
from analytics import total_spent, filter_by_category, group_by_category

# Relative path from src/ folder
path = "../data/expenses.csv"

# Load and clean data
expenses = clean_expenses(load_expenses(path))

def print_expenses_table(expenses):
    print(f"{'Date':<12} {'Category':<15} {'Amount':>10}")
    print("-" * 40)
    for e in expenses:
        print(f"{e['date']:<12} {e['category']:<15} {float(e['amount']):>10.2f}")

print("\nTOTAL SPENT")
print(total_spent(expenses))

print("\nALL EXPENSES")
print_expenses_table(expenses)

print("\nFOOD EXPENSES")
print_expenses_table(filter_by_category("food")(expenses))

print("\nCATEGORY BREAKDOWN")
print(f"{'Category':<15} {'Total':>10}")
print("-" * 30)

for category, total in group_by_category(expenses).items():
    print(f"{category:<15} {total:>10.2f}")
