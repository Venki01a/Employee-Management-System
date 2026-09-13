# 👨‍💼 Employee Management System

> **A simple, attractive, and user-friendly Employee Management System built with Python and Streamlit.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple?logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

The **Employee Management System (EMS)** is a simple web-based application developed using **Python and Streamlit**.

The application provides an easy and attractive interface for managing employee information. Users can add new employees, view all employee records, and search for a specific employee using their Employee ID.

The system is designed to be **simple and easy to understand**, even for users without a technical background.

---

## ✨ Features

### 🏠 Dashboard

The dashboard provides a quick summary of employee information.

It displays:

* 👥 **Total Employees**
* 🏢 **Total Departments**
* 💰 **Average Salary**
* 🏆 **Highest Salary**

---

### ➕ Add Employee

Users can easily add a new employee by entering:

* 🆔 Employee ID
* 👤 Employee Name
* 🎂 Age
* 🏢 Department
* 💰 Monthly Salary

The application also checks for duplicate Employee IDs.

---

### 👥 View All Employees

All employee records can be viewed in a clean table format.

The table contains:

| Information       | Description                           |
| ----------------- | ------------------------------------- |
| 🆔 Employee ID    | Unique employee identification number |
| 👤 Name           | Employee's name                       |
| 🎂 Age            | Employee's age                        |
| 🏢 Department     | Employee's department                 |
| 💰 Monthly Salary | Employee's salary                     |

---

### 🔍 Search Employee

Users can search for an employee by entering their **Employee ID**.

If the employee is found, the application displays their:

* 👤 Name
* 🎂 Age
* 🏢 Department
* 💰 Monthly Salary

If the Employee ID does not exist, the system displays an appropriate error message.

---

## 🎨 User Interface

The application includes an attractive and user-friendly interface with:

* 🌈 Gradient background
* 📋 Sidebar navigation
* 👨‍💼 Meaningful icons
* 📊 Dashboard cards
* 🟢 Success messages
* 🔴 Error messages
* ⚠️ Warning messages
* 📱 Wide and responsive layout

The interface is designed for **easy navigation and understanding**.

---

## 🛠️ Technologies Used

| Technology       | Purpose                            |
| ---------------- | ---------------------------------- |
| 🐍 **Python**    | Application development            |
| 🎨 **Streamlit** | Web application and user interface |
| 🐼 **Pandas**    | Data handling and table display    |
| 💻 **HTML/CSS**  | UI styling and attractive design   |

---

## 📂 Project Structure

```text
Employee_Management_System/
│
├── employee_management_system.py
│
└── README.md
```

### 📄 File Description

**`employee_management_system.py`**

Contains the complete Streamlit application, including employee data, functions, dashboard, navigation, validation, and user interface.

**`README.md`**

Contains documentation and information about the project.

---

## 📊 Sample Employee Data

The application starts with sample employee records:

| Employee ID | Name  | Age | Department |  Salary |
| ----------: | ----- | --: | ---------- | ------: |
|         101 | Satya |  27 | HR         | ₹50,000 |
|         102 | Rahul |  30 | IT         | ₹60,000 |
|         103 | Priya |  26 | Finance    | ₹55,000 |

---

## 🔄 Application Workflow

```text
                👨‍💼 Employee Management System
                            │
                            ▼
                       🏠 Dashboard
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
       ➕ Add Employee  👥 View All    🔍 Search
             │              │              │
             ▼              ▼              ▼
       Enter Details    View Records    Enter ID
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                   👨‍💼 Employee Records
```

---

## ✅ Input Validation

The application performs basic validation to avoid incorrect information.

### 🆔 Employee ID

* Must be a numeric value.
* Must be unique.
* Duplicate Employee IDs are not allowed.

### 👤 Employee Name

* Employee name cannot be empty.

### 🎂 Age

* Age must be between 1 and 100.

### 💰 Salary

* Salary cannot be negative.

---

## 🚀 Installation & Setup

### 1️⃣ Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

---

### 2️⃣ Install Required Libraries

Open Command Prompt or Terminal and run:

```bash
pip install streamlit pandas
```

---

### 3️⃣ Open the Project Folder

For example:

```bash
cd "E:\Tutedude Data Science Course Assignments\Employee Management System"
```

---

### 4️⃣ Run the Application

Execute:

```bash
streamlit run employee_management_system.py
```

The Streamlit application will automatically open in your web browser.

---

## 💡 How to Use

### Step 1 — Open Dashboard

The dashboard shows an overview of the employee records.

### Step 2 — Add Employee

Go to:

**➕ Add Employee**

Enter the required information and click:

**➕ Add Employee**

### Step 3 — View Employees

Go to:

**👥 View All Employees**

All available employee records will be displayed.

### Step 4 — Search Employee

Go to:

**🔍 Search Employee**

Enter the Employee ID and click:

**🔍 Search Employee**

---

## 🎯 Project Objectives

The main objectives of this project are:

1. To develop a simple Employee Management System.
2. To create a user-friendly web interface.
3. To manage employee information efficiently.
4. To implement employee search functionality.
5. To display employee records in a structured format.
6. To create an interactive dashboard.
7. To practice Python programming and Streamlit development.

---

## 📚 Concepts Used

This project demonstrates the use of:

* 🐍 Python
* 📦 Functions
* 🗂️ Dictionaries
* 🔄 Loops
* ✅ Conditional Statements
* 🧾 Input Validation
* 🐼 Pandas
* 🎨 Streamlit
* 📊 DataFrames
* 🎨 HTML/CSS Styling
* 🖥️ Web Application Development

---

## 🌟 Future Enhancements

The project can be improved further by adding:

* ✏️ Edit Employee
* 🗑️ Delete Employee
* 🔎 Advanced Search
* 🏢 Department Filtering
* 📥 Export Employee Data
* 📊 Employee Charts
* 📈 Salary Analysis
* 🔐 Login & Authentication
* 👤 Admin/User Roles

---

## 🎓 Learning Outcome

Through this project, I gained practical experience in developing a **Python-based web application using Streamlit**.

I learned how to create interactive forms, manage employee records, perform input validation, display data using tables, and design an attractive dashboard for users.

---

## 👨‍💻 Author

### Venkatesh Garg

🎓 **B.Tech — Data Science**

🔗 **LinkedIn:**
https://www.linkedin.com/in/venkatesh-garg-analyst

💻 **GitHub:**
https://github.com/Venki01a

---

## ⭐ Project Highlights

| Feature                   | Status |
| ------------------------- | ------ |
| 👨‍💼 Employee Management | ✅      |
| ➕ Add Employee            | ✅      |
| 👥 View Employees         | ✅      |
| 🔍 Search Employee        | ✅      |
| 🏠 Dashboard              | ✅      |
| 🎨 Attractive UI          | ✅      |
| ✅ Input Validation        | ✅      |
| 📊 Data Display           | ✅      |
| 📱 User-Friendly Design   | ✅      |

---

## ❤️ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

**Thank you for visiting my project! 🚀**
