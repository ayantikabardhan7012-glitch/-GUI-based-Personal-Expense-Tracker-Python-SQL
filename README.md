# Student Management System (Tkinter + SQLite)

A simple desktop GUI app to **add, view, update, and delete student records** using Python’s Tkinter for the interface and SQLite for storage. Great as a starter project for learning GUI programming, layout management, and basic CRUD with a local database.

---

## ✨ Features
- **CRUD operations** for students (Roll, Name, Class, Marks).  
- **SQLite database** with a `student` table created automatically on first run.  
- **Tkinter GUI** using common widgets: **Button, Label, Entry, Combobox, Text**.  
- **Grid layout** for clean placement of controls.  

---

## 🖼️ Screens (from the project PDF)
- Before inserting any record  
- Data entry  
- After adding / viewing records  
- Update by roll number  
- Delete by roll number  

---

## 🧱 Tech Stack
- **Python 3**  
- **Tkinter** (GUI – standard library)  
- **SQLite3** (database – standard library)
  
---

## 🗄️ Database Schema
The app uses a single table:

```sql
CREATE TABLE IF NOT EXISTS student(
  roll   INTEGER PRIMARY KEY,
  name   TEXT,
  class  TEXT,
  marks  INTEGER
);
```

---

## 🔧 How It Works (Quick Tour)
- On startup, connects to SQLite and ensures the table exists.  
- UI built with **Labels**, **Entry** fields, action **Buttons**, and a **Text** area.  
- Buttons trigger handlers that perform **INSERT/SELECT/UPDATE/DELETE**.  

---

## 🗺️ Widgets Used
- **Button**  
- **Label**  
- **Entry**  
- **Combobox**  
- **Text**  

---

## 🚀 Future Scope
- More interactive input controls (date pickers, autosuggest).  
- Enhanced dashboards and dynamic tables.  
- Light/Dark themes, packaged executables (e.g., PyInstaller).  
- Cloud sync, backups, role-based access for multi-user support.  

---

## 🙏 Acknowledgments
- **Mentor:** *Soumili Kundu* (certificate dated 23 June, 2025)  
- Developed under the **Academy of Skill Development**  
- Submitted by **Ayantika Bardhan (KIIT)**  


---
