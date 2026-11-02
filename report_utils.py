import datetime

today = datetime.date.today()
month = today.month
year = today.year

print(today)
print("Month :", month)
print("Year: ", year)

formattedd_date = today.strftime("%d-%m-%Y")
print(formattedd_date)

import os
print(os.getcwd())
if os.path.exists("reports"):
    print("already Exist")
else:
    os.mkdir("reports")
    print("folder is Created")



from tabulate import tabulate

data = [
    ["Food", 500],
    ["Travel", 250],
    ["Shopping", 300]
]

headers = ["Category", "Amount"]

print(tabulate(data, headers=headers, tablefmt="grid"))

def generate_report(expenses):
    print("\n========== EXPENSE REPORT ==========")

    print("Date:", formattedd_date)

    print("Total Expenses:", sum(item["amount"] for item in expenses))

    print("\nCategory-wise Expenses:")

    categories = []

    for item in expenses:
        if item["category"] not in categories:
            categories.append(item["category"])

    for category in categories:
        total = 0

        for item in expenses:
            if item["category"] == category:
                total += item["amount"]

        print(category, ":", total)

    if len(expenses) > 0:
        average = sum(item["amount"] for item in expenses) / len(expenses)
    else:
        average = 0

    print("Average Expense:", average)   

    print("\nExpense Details:")

    data = []

    for item in expenses:
        data.append([
            item["id"],
            item["description"],
            item["category"],
            item["amount"]
        ])

    headers = ["ID", "Description", "Category", "Amount"]

    print(tabulate(data, headers=headers, tablefmt="grid"))

    file = open("reports/monthly_report.txt", "w")

    file.write("MONTHLY EXPENSE REPORT\n")
    file.write("Date: " + str(formattedd_date) + "\n")
    file.write("Total Expenses: " + str(sum(item["amount"] for item in expenses)))

    file.write("\n\nCategory-wise Expenses:\n")

    for category in categories:
        total = 0

        for item in expenses:
            if item["category"] == category:
                total += item["amount"]

        file.write(category + ": " + str(total) + "\n")

    average = 0
    if len(expenses) > 0:
        average = sum(item["amount"] for item in expenses) / len(expenses)

    file.write("\nAverage Expense: " + str(average) + "\n") 

    file.write("\n\nExpense Details:\n")

    for item in expenses:
        file.write(
            item["id"] + " | " +
            item["description"] + " | " +
            item["category"] + " | " +
            str(item["amount"]) + "\n"
        )   

    file.close()

    print("\nReport saved successfully!") 

generate_report([
    {
        "id": "EXP-10001",
        "description": "Lunch",
        "category": "food",
        "amount": 250
    },
    {
        "id": "EXP-10002",
        "description": "Bus",
        "category": "travel",
        "amount": 150
    }
])   

