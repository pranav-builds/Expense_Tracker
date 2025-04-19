import os
import csv
from collections import defaultdict
from datetime import datetime

def get_valid_date(prompt="Enter date (YYYY-MM-DD): "):
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.\n")

def initialize_file():
    if not os.path.exists('expenses.csv'):
        with open('expenses.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'category', 'amount'])

def convert_to_standard_date(date_str):
    for fmt in ("%Y-%m-%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None

def get_category_list():
    categories = set()
    if os.path.exists('expenses.csv'):
        with open('expenses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                categories.add(row['category'])
    return list(categories)

def get_valid_amount():
    while True:
        amount = input("Enter amount: ").strip()
        try:
            return float(amount)
        except ValueError:
            print("❌ Please enter a valid number for amount.\n")

def add_expense():
    date = get_valid_date()
    categories = get_category_list()
    print("📂 Available Categories:", categories if categories else "None")
    category = input("Enter category: ").strip()
    amount = get_valid_amount()

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("✅ Expense added successfully.\n")

def view_expenses_by_date():
    target_date = get_valid_date("Enter the date to view expenses (YYYY-MM-DD): ")
    found = False
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        print(f"\nExpenses on {target_date}:")
        print("-" * 35)
        for row in reader:
            row_date = convert_to_standard_date(row['date'])
            if row_date == target_date:
                print(f"Category: {row['category']} | Amount: ₹{row['amount']}")
                found = True
    if not found:
        print("No expenses found on this date.\n")
    else:
        print()

def view_expenses_by_category():
    category = input("Enter the category to view expenses: ").strip()
    found = False
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        print(f"\nExpenses in category '{category}':")
        print("-" * 35)
        for row in reader:
            if row['category'].lower() == category.lower():
                date = convert_to_standard_date(row['date']) or row['date']
                print(f"Date: {date} | Amount: ₹{row['amount']}")
                found = True
    if not found:
        print("No expenses found in this category.\n")
    else:
        print()

def view_expenses_by_date_and_category():
    date = get_valid_date("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ").strip()
    found = False
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        print(f"\nExpenses on {date} in category '{category}':")
        print("-" * 35)
        for row in reader:
            row_date = convert_to_standard_date(row['date'])
            if row_date == date and row['category'].lower() == category.lower():
                print(f"Amount: ₹{row['amount']}")
                found = True
    if not found:
        print("No matching expenses found.\n")
    else:
        print()

def view_category_summary():
    category_totals = defaultdict(float)
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                category_totals[row['category']] += float(row['amount'])
            except ValueError:
                continue
    print("\n📊 Category-wise Summary:")
    print("-" * 35)
    for category, total in category_totals.items():
        print(f"{category}: ₹{total}")
    print()

def view_total_summary():
    total = 0
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                total += float(row['amount'])
            except ValueError:
                continue
    print(f"\n💰 Overall total spent: ₹{total}\n")

def view_monthly_summary():
    monthly_totals = defaultdict(float)
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                date = convert_to_standard_date(row['date'])
                if date:
                    month_key = date[:7]  # YYYY-MM
                    monthly_totals[month_key] += float(row['amount'])
            except ValueError:
                continue
    print("\n📅 Monthly Summary:")
    print("-" * 35)
    for month, total in sorted(monthly_totals.items()):
        print(f"{month}: ₹{total}")
    print()

def delete_expense():
    print("🗑️ Delete Expense:")
    date = get_valid_date("Enter date of expense to delete (YYYY-MM-DD): ")
    category = input("Enter category to delete: ").strip()

    updated_rows = []
    deleted = False

    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row_date = convert_to_standard_date(row['date'])
            if row_date == date and row['category'].lower() == category.lower() and not deleted:
                deleted = True  # Delete only first match
                continue
            updated_rows.append(row)

    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount'])
        writer.writeheader()
        writer.writerows(updated_rows)

    if deleted:
        print("✅ Expense deleted successfully.\n")
    else:
        print("❌ No matching expense found to delete.\n")

def main_menu():
    initialize_file()
    while True:
        print("📋 Expense Tracker Menu:")
        print("1. Add New Expense")
        print("2. View Expenses by Date")
        print("3. View Expenses by Category")
        print("4. View Expenses by Date & Category")
        print("5. View Category-wise Summary")
        print("6. View Total Summary")
        print("7. View Monthly Summary")
        print("8. Delete an Expense")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses_by_date()
        elif choice == '3':
            view_expenses_by_category()
        elif choice == '4':
            view_expenses_by_date_and_category()
        elif choice == '5':
            view_category_summary()
        elif choice == '6':
            view_total_summary()
        elif choice == '7':
            view_monthly_summary()
        elif choice == '8':
            delete_expense()
        elif choice == '9':
            print("👋 Exiting the program. Bye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

main_menu()
