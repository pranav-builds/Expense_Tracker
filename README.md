# 💸 Expense Tracker (Console-based)

A simple yet powerful **console-based Expense Tracker** built with **Python**.  
It allows you to efficiently track, manage, and analyze your daily spending — all through the terminal.

---

## 📂 Features

- 📆 Add new expenses with date, category, and amount.
- 🔍 View expenses by:
  - Specific **date**
  - Specific **category**
  - **Date & category** together
- 📊 Get insights:
  - Category-wise total summary
  - Overall total expense
  - Monthly breakdown of spending
- 🗑️ Delete specific expenses (first match only).
- 🧠 Smart input handling with:
  - Date format checking
  - Amount validation
  - Category suggestion

---

## 🛠️ Tech Used

- **Python 3**
- **CSV module** for data storage (`expenses.csv`)
- **collections.defaultdict** for aggregations
- **datetime** for date parsing & formatting

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x installed on your system.

### 🔧 Installation

```bash
git clone https://github.com/pranav-builds/Expense_Tracker


🧪 Sample Usage
sql
Copy
Edit
📋 Expense Tracker Menu:
1. Add New Expense
2. View Expenses by Date
3. View Expenses by Category
4. View Expenses by Date & Category
5. View Category-wise Summary
6. View Total Summary
7. View Monthly Summary
8. Delete an Expense
9. Exit
📁 Data Storage Format (expenses.csv)

date	category	amount
2025-04-17	groceries	250
2025-04-18	entertainment	500
2025-04-18	groceries	100
All entries are saved locally in CSV format.

✅ To-Do / Future Features
 GUI using Tkinter / PyQt

 Graphs and data visualization

 Export reports as PDF

 Cloud backup (Firebase integration)

 Monthly budget alerts

📃 License
This project is open source and available under the MIT License.

