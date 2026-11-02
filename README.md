🏦 Project Structure

<div align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:071426,50:172C49,100:D6AD55&height=90&text=BANKING%20SYSTEM&fontSize=28&fontColor=FFFFFF&fontAlignY=40&desc=PROJECT%20ARCHITECTURE&descSize=13&descAlignY=72"/><img src="https://img.shields.io/badge/DARK%20NAVY-071426?style=for-the-badge&labelColor=071426&color=172C49"/>
<img src="https://img.shields.io/badge/LUXURY%20GOLD-D6AD55?style=for-the-badge&labelColor=604A19&color=D6AD55"/></div>🏦 BankingSystem/
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

<div align="center"><img src="https://capsule-render.vercel.app/api?type=rect&color=0:071426,100:D6AD55&height=55&text=SECURE%20BANKING%20%7C%20SMART%20TRANSACTIONS&fontSize=14&fontColor=FFFFFF"/></div>

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

