# Personal Expense Tracker

A clean, modular command-line **Personal Expense Tracker** built in **Python**. It is designed to help you efficiently log expenses, manage budgets, and generate structured summary reports.

## Features

* **Modular Architecture:** Clean separation of concerns with dedicated utility modules for expense management and reporting.
* **Expense Tracking:** Add, view, and organize daily transactions and expenditures seamlessly.
* **Automated Reports:** Generate and export summary reports into dedicated storage directories.

## Project Structure

```text
personal-expense-tracker/
│
├── main.py             # Application entry point and CLI interface
├── expense_utils.py    # Core business logic for adding and tracking expenses
├── report_utils.py     # Utilities for generating expenditure and summary reports
├── reports/            # Directory storing generated report outputs
└── requirements.txt    # Project dependencies and package requirements
