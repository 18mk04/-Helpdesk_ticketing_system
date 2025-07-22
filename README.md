# 🎫 Helpdesk Ticketing System (Simulated)

A command-line based helpdesk ticketing system built with **Python** and **SQLite**, designed to simulate real-world IT support operations including ticket creation, tracking, resolution, and escalation.

---

## 🛠 Tech Stack

- **Python** – Core scripting language
- **SQLite** – Lightweight database for storing tickets
- **CLI (Command Line Interface)** – User interface
- **Shell Scripting** – For optional database backup

---

## 📌 Features

- 🎟 Create new support tickets via CLI
- 📂 Categorize tickets (e.g., Software, Hardware, Network)
- ⏱ Set priorities (Low, Medium, High)
- 🔄 Update ticket status (Open → Resolved)
- 🚨 Escalate unresolved tickets automatically based on priority
- 🗃 Store all data locally using SQLite
- 💾 Optional: Shell script to back up ticket database

---

## 📷 Sample Workflow

1. **User reports an issue:**
   - Name: `Alice`
   - Category: `Network`
   - Priority: `High`
   - Description: `Internet is not working`

2. **Ticket is stored in SQLite DB:**
   - Status: `Open`
   - Created: `2025-07-22 17:45:00`

3. **Support agent views, updates, or resolves the ticket**

---

## 🚀 How to Run

### 🔹 Clone the Repository

```bash
git clone https://github.com/18mk04/-Helpdesk_ticketing_system
cd -Helpdesk-ticketing-system
