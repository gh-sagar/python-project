from typing import List, Dict
path=r"expense_analyzer/data/expenses.csv"

def load_expenses(path: str) -> List[Dict[str, str]]:
    # 1. Open the file in read mode
    with open(path, "r") as file:
        
        # 2. Read the entire file as ONE string
        file_content = file.read()
        
        # 3. Remove extra whitespace (like last newline)
        cleaned_content = file_content.strip()
        
        # 4. Split the content into individual lines
        lines = cleaned_content.split("\n")
        
        # 5. Take the first line (header row)
        header_line = lines[0]
        
        # 6. Split header line into column names
        headers = header_line.split(",")
        
        # 7. Prepare an empty list to store results
        expenses = []
        
        # 8. Loop over each data row (skip header)
        for row in lines[1:]:
            
            # 9. Split the row into values
            values = row.split(",")
            
            # 10. Create an empty dictionary for one expense
            expense_dict = {}
            
            # 11. Match headers with values manually
            for index in range(len(headers)):
                key = headers[index]
                value = values[index]
                expense_dict[key] = value
            
            # 12. Add the dictionary to the list
            expenses.append(expense_dict)
        
        # 13. Return the final list
        return expenses
if __name__ == "__main__":
  result = load_expenses(path)
  print(result)