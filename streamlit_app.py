
import streamlit as st
import sqlite3
import hashlib
from decimal import Decimal, InvalidOperation
from database import get_connection, initialize_database

st.set_page_config(
    page_title="FinCore Banking System",
    page_icon="🏦",
    layout="centered"
)

initialize_database()


# ---------------- HELPER FUNCTIONS ----------------

def hash_pin(pin):
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


def money_to_paise(amount):
    try:
        value = Decimal(str(amount))
        if not value.is_finite() or value <= 0:
            raise ValueError("Amount must be greater than zero.")
        if value.as_tuple().exponent < -2:
            raise ValueError("Maximum 2 decimal places allowed.")
        return int(value * 100)
    except (InvalidOperation, ValueError):
        raise ValueError("Enter a valid positive amount.")


def format_money(paise):
    return f"₹{Decimal(paise) / Decimal(100):,.2f}"


def get_account(account_number):
    conn = get_connection()
    try:
        return conn.execute(
            """SELECT account_number, name, pin_hash,
                      balance_paise, created_at
               FROM accounts WHERE account_number = ?""",
            (account_number,)
        ).fetchone()
    finally:
        conn.close()


# ---------------- SESSION ----------------

if "account_number" not in st.session_state:
    st.session_state.account_number = None


# ---------------- TITLE ----------------

st.title("🏦 FinCore Banking System")
st.caption("Simple and secure banking management demonstration")
st.divider()


# ---------------- CREATE ACCOUNT ----------------

st.subheader("Create a Bank Account")

with st.form("create_account"):
    name = st.text_input("Account Holder Name")
    pin = st.text_input("Create 4-digit PIN", type="password", max_chars=4)
    confirm_pin = st.text_input("Confirm PIN", type="password", max_chars=4)
    initial_balance = st.number_input(
        "Initial Deposit (₹)",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

    create_button = st.form_submit_button("Create Account")

    if create_button:
        if not name.strip():
            st.error("Enter your name.")
        elif len(pin) != 4 or not pin.isdigit():
            st.error("PIN must contain exactly 4 digits.")
        elif pin != confirm_pin:
            st.error("PINs do not match.")
        else:
            try:
                balance = Decimal(str(initial_balance))
                if not balance.is_finite() or balance < 0:
                    raise ValueError()
                if balance.as_tuple().exponent < -2:
                    raise ValueError()

                balance_paise = int(balance * 100)

                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT COALESCE(MAX(account_number), 100000) + 1 FROM accounts"
                )
                account_number = cursor.fetchone()[0]

                cursor.execute(
                    """INSERT INTO accounts
                       (account_number, name, pin_hash, balance_paise)
                       VALUES (?, ?, ?, ?)""",
                    (account_number, name.strip(), hash_pin(pin), balance_paise)
                )

                if balance_paise > 0:
                    cursor.execute(
                        """INSERT INTO transactions
                           (account_number, transaction_type,
                            amount_paise, balance_after_paise)
                           VALUES (?, ?, ?, ?)""",
                        (account_number, "Initial Deposit",
                         balance_paise, balance_paise)
                    )

                conn.commit()
                conn.close()

                st.success("Account created successfully!")
                st.info(f"Your account number is: {account_number}")
                st.warning("Save your account number. You need it to log in.")

            except (ValueError, InvalidOperation):
                st.error("Enter a valid initial deposit.")
            except sqlite3.Error as error:
                st.error(f"Database error: {error}")


st.divider()


# ---------------- LOGIN ----------------

st.subheader("Account Login")

with st.form("login_form"):
    login_account = st.text_input("Account Number")
    login_pin = st.text_input("4-digit PIN", type="password", max_chars=4)
    login_button = st.form_submit_button("Login")

    if login_button:
        if not login_account.isdigit():
            st.error("Enter a valid account number.")
        elif len(login_pin) != 4 or not login_pin.isdigit():
            st.error("Enter a valid 4-digit PIN.")
        else:
            account = get_account(int(login_account))

            if account and account["pin_hash"] == hash_pin(login_pin):
                st.session_state.account_number = int(login_account)
                st.success(f"Welcome, {account['name']}!")
            else:
                st.error("Incorrect account number or PIN.")


# ---------------- BANKING DASHBOARD ----------------

account_number = st.session_state.account_number

if account_number is not None:
    account = get_account(account_number)

    if account is None:
        st.session_state.account_number = None
        st.error("Account not found. Please log in again.")
        st.stop()

    st.divider()
    st.header(f"Welcome, {account['name']}")

    st.metric(
        "Account Balance",
        format_money(account["balance_paise"])
    )

    st.caption(f"Account Number: {account_number}")
    st.caption(f"Account Created: {account['created_at']}")

    tab_deposit, tab_withdraw, tab_history = st.tabs(
        ["Deposit", "Withdraw", "Transaction History"]
    )

    # ---------------- DEPOSIT ----------------

    with tab_deposit:
        st.subheader("Deposit Money")

        with st.form("deposit_form"):
            deposit_amount = st.number_input(
                "Deposit Amount (₹)", min_value=0.0, step=100.0,
                key="deposit_amount"
            )
            deposit_button = st.form_submit_button("Deposit")

            if deposit_button:
                try:
                    amount = money_to_paise(deposit_amount)
                    conn = get_connection()
                    cursor = conn.cursor()

                    cursor.execute(
                        """UPDATE accounts
                           SET balance_paise = balance_paise + ?
                           WHERE account_number = ?""",
                        (amount, account_number)
                    )

                    cursor.execute(
                        """SELECT balance_paise FROM accounts
                           WHERE account_number = ?""",
                        (account_number,)
                    )
                    new_balance = cursor.fetchone()["balance_paise"]

                    cursor.execute(
                        """INSERT INTO transactions
                           (account_number, transaction_type,
                            amount_paise, balance_after_paise)
                           VALUES (?, ?, ?, ?)""",
                        (account_number, "Deposit", amount, new_balance)
                    )

                    conn.commit()
                    conn.close()
                    st.success(f"Deposited {format_money(amount)} successfully.")
                    st.rerun()

                except ValueError as error:
                    st.error(str(error))
                except sqlite3.Error as error:
                    st.error(f"Transaction failed: {error}")

    # ---------------- WITHDRAW ----------------

    with tab_withdraw:
        st.subheader("Withdraw Money")

        with st.form("withdraw_form"):
            withdraw_amount = st.number_input(
                "Withdrawal Amount (₹)", min_value=0.0, step=100.0,
                key="withdraw_amount"
            )
            withdraw_button = st.form_submit_button("Withdraw")

            if withdraw_button:
                try:
                    amount = money_to_paise(withdraw_amount)
                    conn = get_connection()
                    cursor = conn.cursor()

                    cursor.execute(
                        """UPDATE accounts
                           SET balance_paise = balance_paise - ?
                           WHERE account_number = ?
                           AND balance_paise >= ?""",
                        (amount, account_number, amount)
                    )

                    if cursor.rowcount == 0:
                        conn.rollback()
                        st.error("Insufficient balance.")
                    else:
                        cursor.execute(
                            """SELECT balance_paise FROM accounts
                               WHERE account_number = ?""",
                            (account_number,)
                        )
                        new_balance = cursor.fetchone()["balance_paise"]

                        cursor.execute(
                            """INSERT INTO transactions
                               (account_number, transaction_type,
                                amount_paise, balance_after_paise)
                               VALUES (?, ?, ?, ?)""",
                            (account_number, "Withdrawal", amount, new_balance)
                        )

                        conn.commit()
                        st.success(
                            f"Withdrawn {format_money(amount)} successfully."
                        )
                        st.rerun()

                    conn.close()

                except ValueError as error:
                    st.error(str(error))
                except sqlite3.Error as error:
                    st.error(f"Transaction failed: {error}")

    # ---------------- HISTORY ----------------

    with tab_history:
        st.subheader("Transaction History")

        conn = get_connection()
        transactions = conn.execute(
            """SELECT transaction_id, transaction_type,
                      amount_paise, balance_after_paise, created_at
               FROM transactions
               WHERE account_number = ?
               ORDER BY transaction_id DESC""",
            (account_number,)
        ).fetchall()
        conn.close()

        if transactions:
            rows = []
            for transaction in transactions:
                rows.append({
                    "Transaction ID": transaction["transaction_id"],
                    "Type": transaction["transaction_type"],
                    "Amount": format_money(transaction["amount_paise"]),
                    "Balance After": format_money(
                        transaction["balance_after_paise"]
                    ),
                    "Date": str(transaction["created_at"])
                })

            st.dataframe(rows, use_container_width=True)
        else:
            st.info("No transactions found.")

    if st.button("Logout"):
        st.session_state.account_number = None
        st.rerun()


st.divider()
st.caption("FinCore | Educational project demonstration only")
