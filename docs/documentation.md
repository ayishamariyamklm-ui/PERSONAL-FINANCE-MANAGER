
---

# 📗 documentation.md

```markdown
# Personal Finance Manager – Detailed Documentation

---

## 1️⃣ Introduction

This document provides a detailed explanation of the Personal Finance Manager project, including architecture, modules, logic, and usage instructions.

---

## 2️⃣ Application Architecture

The application follows a **modular architecture**, where each component has a specific responsibility.

### Key Principles:
- Separation of concerns
- Reusable functions
- Clean and readable code
- Error handling and validation

---

## 3️⃣ Module Descriptions

---

### 📄 main.py
**Purpose:** Entry point of the application

Responsibilities:
- Starts the program
- Loads saved expense data
- Displays menu options
- Handles user choices
- Calls appropriate functions
- Saves data before exit

---

### 📄 expense.py
**Purpose:** Defines the Expense class

Attributes:
- amount
- category
- date
- description

Key Methods:
- `__init__()` – initializes expense data
- `__str__()` – formatted display
- `to_list()` – CSV conversion
- `from_list()` – CSV to object

---

### 📄 file_manager.py
**Purpose:** Handles CSV file operations

Functions:
- `save_expenses()` – writes data to CSV
- `load_expenses()` – reads data from CSV
- Handles missing files safely

---

### 📄 menu.py
**Purpose:** Command-line user interface

Responsibilities:
- Display menus
- Collect user input
- Validate entries
- Call logic functions

---

### 📄 reports.py
**Purpose:** Data analysis and reporting

Functions:
- Category-wise summary
- Monthly report
- Overall expense statistics
- Export report to text file

---

### 📄 utils.py
**Purpose:** Utility and validation helpers

Functions:
- Validate amount
- Validate date format
- Validate category
- Validate menu choices
- Format currency output

---

## 4️⃣ Data Storage

- Expenses are stored in `data/expenses.csv`
- CSV format ensures:
  - Easy readability
  - Simple backup
  - Compatibility with Excel

---

## 5️⃣ Error Handling

Implemented using:
- Try-except blocks
- Input validation functions
- Graceful failure messages

---

## 6️⃣ Testing

Basic testing can be done by:
- Adding invalid inputs
- Verifying CSV persistence
- Checking reports accuracy


---

## 7️⃣ GitHub Submission Guide

### Steps:
1. Create GitHub repository
2. Upload project files
3. Add README.md and documentation.md
4. Commit changes
5. Copy repository URL


---

## 8️⃣ Future Enhancements

- Budget planning feature
- Graphical charts using Matplotlib
- Export reports to PDF/Excel
- GUI version using Tkinter

---

## 9️⃣ Conclusion

This project demonstrates strong fundamentals in Python programming, object-oriented design, file handling, and real-world application development.  
It is suitable for academic submission, certification evaluation, and portfolio showcasing.

---



