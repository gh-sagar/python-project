from functools import reduce

def total_spent(expenses):
    return reduce(lambda acc, e: acc + e["amount"], expenses, 0)

def filter_by_category(category):
    return lambda expenses: list(
        filter(lambda e: e["category"] == category.lower(), expenses)
    )

def group_by_category(expenses):
    return reduce(
        lambda acc, e: {
            **acc,
            e["category"]: acc.get(e["category"], 0) + e["amount"]
        },
        expenses,
        {}
    )
