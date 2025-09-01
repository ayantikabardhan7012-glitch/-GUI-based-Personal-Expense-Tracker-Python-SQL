import pyodbc
from datetime import datetime

# Connection string
driver = 'SQL SERVER'
server_name = 'bardh\\SQLEXPRESS'
database_name = 'Expenses'

connection_string = f"""
    DRIVER={{{driver}}};
    SERVER={server_name};
    DATABASE={database_name};
    Trusted_Connection=yes;
"""

# Connect to DB
def connect_db():
    """Establishes and returns a connection to the SQL Server database."""
    return pyodbc.connect(connection_string)

# Insert new transaction
def insert_transaction():
    """Prompts user for details and inserts a new expense transaction."""
    try:
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
        date_value = date_input if date_input else datetime.now().strftime('%Y-%m-%d')

        with connect_db() as conn:
            cursor = conn.cursor()
            query = "INSERT INTO transactions (amount, description, date) VALUES (?, ?, ?)"
            cursor.execute(query, (amount, description, date_value))
            conn.commit()
            print("\nTransaction added successfully.\n")
    except ValueError:
        print("\nInvalid amount. Please enter a number.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# View all transactions
def view_transactions():
    """Fetches and displays a summary of all transactions."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT expense_id, amount, date FROM transactions ORDER BY expense_id")
        rows = cursor.fetchall()
        if rows:
            print("\nAll Transactions:")
            print(f"{'ID':<5}{'Amount':<15}{'Date':<15}")
            print("-" * 35)
            for row in rows:
                print(f"{row.expense_id:<5}₹{row.amount:<13.2f}{str(row.date):<15}")
        else:
            print("\nNo transactions found.\n")

# View specific transaction details
def view_transaction_details():
    """Prompts for an ID, shows full details, and presents an action menu."""
    transaction_id = input("\nEnter Transaction ID to view details: ")
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM transactions WHERE expense_id = ?", (transaction_id,))
            row = cursor.fetchone()
            if row:
                print("\n--- Transaction Details ---")
                print(f"ID:          {row.expense_id}")
                print(f"Amount:      ₹{row.amount:.2f}")
                print(f"Date:        {row.date}")
                print(f"Description: {row.description}")
                print("---------------------------")
                print("\n1. Delete this transaction")
                print("2. Update this transaction")
                print("3. Back to Main Menu")
                choice = input("Choose an option: ")
                if choice == '1':
                    delete_transaction(row.expense_id)
                elif choice == '2':
                    update_transaction(row.expense_id)
            else:
                print("\nTransaction not found.\n")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# Delete a transaction
def delete_transaction(expense_id):
    """Deletes a transaction specified by its ID."""
    confirm = input(f"Are you sure you want to delete transaction {expense_id}? (y/n): ").lower()
    if confirm == 'y':
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transactions WHERE expense_id = ?", (expense_id,))
            conn.commit()
            print("\nTransaction deleted successfully.\n")
    else:
        print("\nDeletion cancelled.")

# Update a transaction
def update_transaction(expense_id):
    """Updates a transaction specified by its ID."""
    try:
        new_amount = float(input("Enter new amount: "))
        new_description = input("Enter new description: ")
        new_date_input = input("Enter new date (YYYY-MM-DD) or leave blank to keep current: ")
        
        with connect_db() as conn:
            cursor = conn.cursor()
            # Fetch current date if new one isn't provided
            if not new_date_input:
                row = cursor.execute("SELECT date FROM transactions WHERE expense_id = ?", (expense_id,)).fetchone()
                new_date = row.date
            else:
                new_date = new_date_input

            query = "UPDATE transactions SET amount = ?, description = ?, date = ? WHERE expense_id = ?"
            cursor.execute(query, (new_amount, new_description, new_date, expense_id))
            conn.commit()
            print("\nTransaction updated successfully.\n")
    except ValueError:
        print("\nInvalid amount. Please enter a number.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# Main Menu
def main_menu():
    """The main control loop for the application."""
    while True:
        print("\n===== Personal Expense Tracker =====")
        view_transactions()
        print("\n1. Add New Expense")
        print("2. View/Update/Delete Transaction Details")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == '1':
            insert_transaction()
        elif choice == '2':
            view_transaction_details()
        elif choice == '3':
            print("\nExiting the tracker. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main_menu()

