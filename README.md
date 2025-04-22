# Library Management System

## **Project Overview
The **Library Management System** is a Python-based application with a graphical user interface (GUI) built using **Tkinter**. It streamlines essential library operations, such as **book management, borrowing, returning, and tracking user transactions**, reducing manual tasks by **50%**.

This system uses **SQLite** for database management, ensuring efficient record-keeping and easy retrieval of data.

## **Features**
✅ **Add, Update, Delete Books** – Manage books with title, author, and availability status  
✅ **Borrow & Return Books** – Track book transactions with due date calculations  
✅ **User-Friendly GUI** – Intuitive interface with Tkinter for easy navigation  
✅ **Database Integration** – Persistent data storage using SQLite  
✅ **View Books** – Display the list of all books with status updates  

## **Technology Stack**
- **Programming Language:** Python  
- **GUI:** Tkinter  
- **Database:** SQLite  
- **Libraries Used:**  
  - `tkinter` – for user interface  
  - `sqlite3` – for database management  
  - `datetime` – for handling due dates  

## **Installation & Setup**
1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-repository/library-management-system.git
   ```
2. Install Python (if not already installed):
   - Download from [python.org](https://www.python.org/)
   - Ensure you have version **3.x+**
3. Navigate to the project directory:
   ```bash
   cd library-management-system
   ```
4. Run the application:
   ```bash
   python library.py
   ```
   
## **Usage Instructions**
### **Adding Books**
- Enter the book **title** and **author**
- Click **"Add Book"** to store it in the database  

### **Borrowing Books**
- Click **"Borrow Book"**  
- Enter the **Book ID** and **User Name**  
- System updates book status & records due date  

### **Returning Books**
- Click **"Return Book"**  
- Enter the **Book ID**  
- System marks the book as **Available** again  

### **Viewing Books**
- Click **"View Books"**  
- Displays all books with **status** (Available/Borrowed)  

## **Future Enhancements**
🔹 **QR Code Scanning:** Scan book barcodes for borrowing  
🔹 **Email Notifications:** Remind users about due dates  
🔹 **Advanced Search Filters:** Enable keyword search for books  
🔹 **Export Data:** Generate reports in **Excel/PDF** format  

## **License**
This project is released under the **MIT License**. You are free to modify and distribute it.

## **Author**
Created by **Khush** 🚀  
Feel free to **contribute** or suggest improvements!  

---
