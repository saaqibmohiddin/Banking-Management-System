<div align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:071426,50:172C49,100:D6AD55&height=90&text=BANKING%20SYSTEM&fontSize=28&fontColor=FFFFFF&desc=PROJECT%20ARCHITECTURE&descSize=13&descAlignY=72"/><img src="https://img.shields.io/badge/BANKING%20%26%20FINANCE-172C49?style=for-the-badge"/>
<img src="https://img.shields.io/badge/ACCOUNT%20SECURITY-D6AD55?style=for-the-badge"/></div>

---



The Banking Management System is a console-based banking application developed using Python and SQLite. It provides essential banking operations through a simple and user-friendly interface while maintaining account information and transaction records in a local database.

The application allows users to create bank accounts, securely authenticate using PIN verification, deposit and withdraw money, check account balances, and view transaction history.

It uses PIN hashing, input validation, database error handling, and transaction rollback to improve account security and data reliability.

✨ Key Highlights

- 🏦 Bank account creation and management
- 🔐 Secure PIN hashing and authentication
- 💰 Deposit and withdrawal operations
- 📊 Real-time balance inquiry
- 📜 Transaction history with automatic timestamps
- 🛡️ Input validation and insufficient balance checks
- 🗄️ SQLite database storage
- ⚙️ Database error handling and transaction rollback
- 🇮🇳 Indian Rupee (INR) currency formatting

🎯 Project Objective

To develop a simple and reliable banking application that demonstrates core banking operations, database management, authentication, and secure transaction handling using Python.


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


## 🏗️ Project Structure – Architecture

<p align="center">
  <img src="https://img.shields.io/badge/BANKING%20%26%20FINANCE-071426?style=for-the-badge&logoColor=D6AD55" />
  <img src="https://img.shields.io/badge/ACCOUNT%20SECURITY-172C49?style=for-the-badge&logoColor=D6AD55" />
</p>

### 📂 Project Folder Structure

```text
🏦 BankingSystem/
│
├── 📁 screenshots/
│   ├── main_menu.png
│   ├── deposit.png
│   └── transaction_history.png
│
├── 🐍 banking_system.py
├── 🗄️ database.py
├── 📄 README.md
├── ⚙️ .gitignore
└── 💾 bank.db
```

### ⚙️ Component Architecture

| Component | Responsibility |
|---|---|
| 🐍 banking_system.py | Banking Operations |
| 🗄️ database.py | Database Management |
| 💾 bank.db | Account & Transaction Storage |
| 📁 screenshots/ | Project Screenshots |


---

## 🚀 Installation & Setup

<p align="center">
  <img src="https://img.shields.io/badge/INSTALLATION-071426?style=for-the-badge&logoColor=D6AD55" />
  <img src="https://img.shields.io/badge/PYTHON%203-172C49?style=for-the-badge&logo=python&logoColor=FFD43B" />
  <img src="https://img.shields.io/badge/SQLITE-D6AD55?style=for-the-badge&logo=sqlite&logoColor=071426" />
</p>

Follow these steps to download, configure, and run the Banking Management System on your computer.

### 1️⃣ Prerequisites

Make sure you have installed:

| Requirement | Version / Tool |
|---|---|
| Python | Python 3.10 or later |
| Database | SQLite |
| Code Editor | VS Code (recommended) |
| Version Control | Git |

### 2️⃣ Clone the Repository

Open your terminal and execute:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project folder:

```bash
cd BankingSystem
```

> Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 3️⃣ Verify Python Installation

Check whether Python is installed:

```bash
python --version
```

If your system uses the Python launcher, try:

```bash
py --version
```

### 4️⃣ Run the Application

Start the Banking Management System:

```bash
python banking_system.py
```

On Windows, you can also use:

```bash
py banking_system.py
```

### 5️⃣ Database Setup

This project uses SQLite for storing account and transaction information.

- SQLite does not require a separate database server.
- The `bank.db` file stores the application data.
- The database setup is handled by the project's database code.

### 6️⃣ Required Dependencies

The project uses Python's built-in modules:

- `sqlite3`
- `hashlib`
- `decimal`
- `getpass`
- `pathlib`

No separate package installation is required for these standard-library modules.

### 7️⃣ Start Banking Operations

After successfully running the application, use the main menu to access:

- Create Bank Account
- Account Authentication
- Deposit Money
- Withdraw Money
- Balance Inquiry
- Transaction History

---

<p align="center">

**🏦 BANKING & FINANCE**

**🔐 SECURE ACCOUNT MANAGEMENT**

*Simple • Reliable • Secure*

</p>


---

## 🎯 Project Objective

<p align="center">
  <img src="https://img.shields.io/badge/PROJECT%20OBJECTIVE-071426?style=for-the-badge&logoColor=D6AD55" />
  <img src="https://img.shields.io/badge/BANKING%20MANAGEMENT-172C49?style=for-the-badge&logoColor=D6AD55" />
</p>

### 🏦 Purpose of the Project

The main objective of this Banking Management System is to develop a secure, reliable, and user-friendly banking application using Python and SQLite.

It aims to simplify basic banking operations by allowing users to create accounts, authenticate securely, deposit and withdraw money, check account balances, and view transaction history through a simple menu-driven interface.

### 🎯 Key Objectives

| Objective | Description |
|---|---|
| 🏦 Account Management | Create and manage bank accounts |
| 🔐 Security | Protect account PINs using hashing |
| 💰 Money Transactions | Perform deposits and withdrawals |
| 📊 Balance Inquiry | Check available account balance |
| 📜 Transaction Tracking | Maintain transaction history |
| 🗄️ Data Management | Store account information using SQLite |
| ✅ Input Validation | Prevent invalid user inputs |
| ⚡ Reliability | Handle database errors and transaction failures |

### 💡 Project Vision

To demonstrate how fundamental banking operations can be managed through a simple Python-based application while maintaining account security, accurate transaction records, and reliable database operations.

---

<p align="center">

<img src="https://img.shields.io/badge/SECURE%20BANKING-071426?style=for-the-badge&logoColor=D6AD55" />
<img src="https://img.shields.io/badge/SMART%20TRANSACTIONS-172C49?style=for-the-badge&logoColor=D6AD55" />

**🏦 Secure Banking • 💰 Reliable Transactions • 🔐 Account Protection**

</p>

---



<p align="center">
  <img src="https://img.shields.io/badge/DEVELOPED%20BY-071426?style=for-the-badge&logoColor=D6AD55" />
  <img src="https://img.shields.io/badge/PYTHON%20DEVELOPER-172C49?style=for-the-badge&logo=python&logoColor=FFD43B" />
</p>

<h2 align="center">MOHAMMED SAAQIB MOHIDDIN</h2>

<p align="center">
  <b>Computer Science & Engineering | Artificial Intelligence</b>
</p>

<p align="center">
  Passionate about Python, Artificial Intelligence, Machine Learning,
  and building practical software applications.
</p>

<p align="center">
  <a href="https://github.com/saaqibmohiddin">
    <img src="https://img.shields.io/badge/GitHub-071426?style=for-the-badge&logo=github&logoColor=D6AD55" />
  </a>
  <a href="https://github.com/saaqibmohiddin?tab=repositories">
    <img src="https://img.shields.io/badge/MY%20PROJECTS-172C49?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PROJECT-BANKING%20MANAGEMENT-D6AD55?style=flat-square" />
  <img src="https://img.shields.io/badge/BUILT%20WITH-PYTHON-071426?style=flat-square" />
  <img src="https://img.shields.io/badge/DATABASE-SQLITE-172C49?style=flat-square" />
</p>

---

<p align="center">
  <b>🏦 Designed & Developed with Python</b>
  <br/>
  <sub>Secure Banking • Reliable Transactions • Continuous Learning</sub>
</p>
