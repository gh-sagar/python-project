FROM python:3.10-slim

WORKDIR /app

COPY . .

CMD ["python", "expense_analyzer/src/main.py"]
