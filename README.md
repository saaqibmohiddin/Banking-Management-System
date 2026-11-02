🏦 Project Structure

<div align="center">"Navy" (https://img.shields.io/badge/THEME-DARK%20NAVY-071426?style=for-the-badge)
"Gold" (https://img.shields.io/badge/DESIGN-LUXURY%20GOLD-D6AD55?style=for-the-badge)

💳 BANKING SYSTEM — FILE ARCHITECTURE

</div>🏦 BankingSystem/
│
├── 📁 screenshots/
├── 🐍 banking_system.py
├── 🗄️ database.py
├── 📄 README.md
├── ⚙️ .gitignore
└── 💾 bank.db

<div align="center">SECURE BANKING • SMART TRANSACTIONS

</div>

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

