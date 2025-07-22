import sqlite3
import datetime

def connect_db():
    return sqlite3.connect("database.db")
  
def create_ticket():
    conn = connect_db()
    cur = conn.cursor()

    name = input("Enter your name: ")
    category = input("Enter issue category (Network/Software/Hardware/Access): ")
    description = input("Describe your issue: ")

    # Priority logic
    if category.lower() == 'network':
        priority = 'High'
    elif category.lower() == 'software':
        priority = 'Medium'
    else:
        priority = 'Low'

    cur.execute("""INSERT INTO tickets (user_name, issue_category, description, priority)
                   VALUES (?, ?, ?, ?)""",
                (name, category, description, priority))
    
    conn.commit()
    print("✅ Ticket created successfully!\n")
    conn.close()

def view_tickets():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets")
    rows = cur.fetchall()

    print("\n--- All Tickets ---")
    for row in rows:
        print(f"ID: {row[0]} | User: {row[1]} | Category: {row[2]} | Priority: {row[4]} | Status: {row[5]} | Created: {row[6]}")
    print()
    conn.close()

def update_ticket():
    conn = connect_db()
    cur = conn.cursor()

    ticket_id = input("Enter Ticket ID to update: ")
    new_status = input("Enter new status (In Progress/Resolved/Escalated): ")

    cur.execute("""UPDATE tickets 
                   SET status=?, last_updated=? 
                   WHERE ticket_id=?""",
                (new_status, datetime.datetime.now(), ticket_id))
    conn.commit()
    print("✅ Ticket updated successfully!\n")
    conn.close()

def menu():
    while True:
        print("===== Helpdesk Ticketing System =====")
        print("1. Create New Ticket")
        print("2. View All Tickets")
        print("3. Update Ticket Status")
        print("4. Exit")

        choice = input("Select an option: ")
        if choice == '1':
            create_ticket()
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            update_ticket()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    menu()

