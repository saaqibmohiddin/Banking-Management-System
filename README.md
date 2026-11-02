🏦 Project Structure

<div align="center"><img src="https://img.shields.io/badge/BANKING_SYSTEM-PROJECT_ARCHITECTURE-071426?style=for-the-badge&labelColor=071426&color=D6AD55"/><img src="https://img.shields.io/badge/DARK_NAVY-071426?style=flat-square"/> <img src="https://img.shields.io/badge/LUXURY_GOLD-D6AD55?style=flat-square"/>

</div>🏦 BankingSystem
│
├── 📁 screenshots/
│
├── 🐍 banking_system.py
│
├── 🗄️ database.py
│
├── 📄 README.md
│
├── ⚙️ .gitignore
│
└── 💾 bank.db

<div align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:071426,100:D6AD55&height=55&section=footer&text=SECURE%20BANKING%20%7C%20SMART%20TRANSACTIONS&fontSize=15&fontColor=FFFFFF"/></div>

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

