🏦 Banking Management System

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:071426,50:172C49,100:D6AD55&height=180&section=header&text=BANKING%20MANAGEMENT%20SYSTEM&fontSize=27&fontColor=FFFFFF&animation=fadeIn&fontAlignY=38&desc=Secure%20Banking%20%7C%20Smart%20Transactions&descAlignY=60&descSize=15" width="100%"/>A Python-based banking application for secure account management and financial transactions.

"Python" (https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
"SQLite" (https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
"SQL" (https://img.shields.io/badge/SQL-D6AD55?style=for-the-badge)
"Git" (https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>---

📖 About

A console-based Banking Management System developed using Python and SQLite. It provides account creation, PIN authentication, deposits, withdrawals, balance checking, and transaction history.

✨ Features

- 🏦 Create Bank Accounts
- 🔐 Secure PIN Hashing
- 🔑 Account Authentication
- 💰 Deposit Money
- 💸 Withdraw Money
- 📊 Check Account Balance
- 📜 Transaction History
- 🕒 Automatic Timestamps
- 🛡️ Input Validation
- ⚠️ Insufficient Balance Checking
- 🔄 Database Transaction Rollback
- 🇮🇳 Indian Rupee Formatting

🛠️ Technologies Used

Technology| Purpose
Python 3| Application Development
SQLite| Database Management
SQL| Database Queries
Git & GitHub| Version Control

Python Modules: "sqlite3", "hashlib", "decimal", "getpass", "pathlib"


📂 Project Structure

🏦 BankingSystem/
│
├── 📁 screenshots/
│   ├── 🖼️ main_menu.png
│   ├── 🖼️ deposit.png
│   └── 🖼️ transaction_history.png
│
├── 🐍 banking_system.py
├── 🗄️ database.py
├── 📄 README.md
├── ⚙️ .gitignore
└── 💾 bank.db

📁 File Description

File| Purpose
🐍 "banking_system.py"| Main banking application
🗄️ "database.py"| Database operations
📁 "screenshots/"| Application previews
💾 "bank.db"| SQLite database
📄 "README.md"| Project documentation
⚙️ ".gitignore"| Git ignored files

---


🏗️ SYSTEM ARCHITECTURE

The Banking Management System follows a simple application architecture in which the user interacts with the Python application, which processes banking operations and communicates with the SQLite database.

Architecture Workflow

                 👤 USER
                    |
                    ▼
             MAIN MENU
                    |
          ┌─────────┴─────────┐
          ▼                   ▼
      CREATE ACCOUNT        LOGIN
          |                   |
          ▼                   ▼
      PIN HASHING        AUTHENTICATION
          |                   |
          ▼                   ▼
       DATABASE        BANKING OPERATIONS
                             |
                 ┌───────────┼───────────┐
                 ▼           ▼           ▼
              DEPOSIT     WITHDRAW    BALANCE
                 |           |           |
                 └───────────┼───────────┘
                             ▼
                     TRANSACTION HISTORY
                             |
                             ▼
                       SQLITE DATABASE

