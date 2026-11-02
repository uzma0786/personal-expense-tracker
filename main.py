
from tabulate import tabulate
from report_utils import generate_report

from expense_utils import (
    validate_amount,
    validate_description,
    validate_categoryy,
    generate_id,
    calculate_total,
    calculate_category_total,
    calculate_avg
)

# Store all expenses
expenses = []

# Take multiple expense details
while True:

    description = input("\nEnter expense description: ")
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    # Validate expense details
    if not validate_description(description):
        print("Invalid description")

    elif not validate_categoryy(category):
        print("Invalid category")

    elif not validate_amount(amount):
        print("Invalid amount")

    else:
        print("Expense details are valid")

        # Generate transaction ID
        expense_id = generate_id()
        print("Expense ID:", expense_id)

        # Create expense record
        expense = {
            "id": expense_id,
            "description": description,
            "category": category,
            "amount": amount
        }

        # Store expense
        expenses.append(expense)

        print("Expense added successfully!")

    # Ask user whether to continue
    choice = input("\nDo you want to add another expense? (yes/no): ")

    if choice.lower() != "yes":
        break


# Calculate total expenses
amounts = []

for i in expenses:
    amounts.append(i["amount"])

total = calculate_total(amounts)
print("\nTotal Expenses:", total)


# Calculate category-wise expenses
category = input("\nEnter category to calculate total: ")

category_total = calculate_category_total(expenses, category)

print("Total spending in", category, ":", category_total)


# Calculate average expense
average = calculate_avg(amounts)
print("Average Expense:", average)


# Generate monthly report
print("\nGenerating Monthly Report...")
generate_report(expenses)
