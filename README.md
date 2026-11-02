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


## 🏗️ Project Structure – Architecture Diagram

<p align="center">
  <img src="https://img.shields.io/badge/BANKING%20%26%20FINANCE-071426?style=for-the-badge&logo=bank&logoColor=D6AD55" />
  <img src="https://img.shields.io/badge/ACCOUNT%20SECURITY-172C49?style=for-the-badge&logo=shield&logoColor=D6AD55" />
</p>

```mermaid
flowchart TD
    A["🏦 BANKING SYSTEM"] --> B["📁 BankingSystem/"]

    B --> C["📁 screenshots/"]
    B --> D["🐍 banking_system.py"]
    B --> E["🗄️ database.py"]
    B --> F["📄 README.md"]
    B --> G["⚙️ .gitignore"]
    B --> H["💾 bank.db"]

    C --> I["main_menu.png"]
    C --> J["deposit.png"]
    C --> K["transaction_history.png"]

    D --> L["Banking Operations"]
    E --> M["Database Management"]
    H --> N["Account & Transaction Storage"]

    classDef main fill:#071426,stroke:#D6AD55,color:#FFFFFF,stroke-width:3px
    classDef folder fill:#172C49,stroke:#D6AD55,color:#FFFFFF,stroke-width:2px
    classDef files fill:#101D30,stroke:#8298B5,color:#FFFFFF,stroke-width:1.5px
    classDef data fill:#243B53,stroke:#D6AD55,color:#FFFFFF,stroke-width:2px

    class A,B main
    class C folder
    class D,E,F,G,I,J,K files
    class H,L,M,N data
```

<p align="center">
  <b>🏦 BANKING & FINANCE</b> &nbsp; | &nbsp; <b>🔐 ACCOUNT SECURITY</b>
</p>


