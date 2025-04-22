import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Database setup
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    status TEXT DEFAULT 'Available'
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    trans_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    user TEXT,
    borrow_date TEXT,
    due_date TEXT,
    returned INTEGER DEFAULT 0,
    FOREIGN KEY(book_id) REFERENCES books(book_id)
)
""")
conn.commit()


# Tkinter GUI
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        # Labels
        tk.Label(root, text="Book Title").grid(row=0, column=0)
        tk.Label(root, text="Author").grid(row=1, column=0)

        # Entry fields
        self.title_entry = tk.Entry(root)
        self.author_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)
        self.author_entry.grid(row=1, column=1)

        # Buttons
        tk.Button(root, text="Add Book", command=self.add_book).grid(row=2, column=0, columnspan=2)
        tk.Button(root, text="Borrow Book", command=self.borrow_book).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Return Book", command=self.return_book).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="View Books", command=self.view_books).grid(row=5, column=0, columnspan=2)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
            conn.commit()
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showerror("Error", "Title and Author cannot be empty.")

    def borrow_book(self):
        book_id = tk.simpledialog.askinteger("Borrow Book", "Enter Book ID:")
        user = tk.simpledialog.askstring("User Name", "Enter Your Name:")
        cursor.execute("SELECT status FROM books WHERE book_id=?", (book_id,))
        result = cursor.fetchone()

        if result and result[0] == "Available":
            borrow_date = datetime.today().strftime('%Y-%m-%d')
            due_date = (datetime.today() + timedelta(days=14)).strftime('%Y-%m-%d')
            cursor.execute("UPDATE books SET status='Borrowed' WHERE book_id=?", (book_id,))
            cursor.execute("INSERT INTO transactions (book_id, user, borrow_date, due_date) VALUES (?, ?, ?, ?)",
                           (book_id, user, borrow_date, due_date))
            conn.commit()
            messagebox.showinfo("Success", "Book borrowed successfully!")
        else:
            messagebox.showerror("Error", "Book not available or invalid ID.")

    def return_book(self):
        book_id = tk.simpledialog.askinteger("Return Book", "Enter Book ID:")
        cursor.execute("SELECT status FROM books WHERE book_id=?", (book_id,))
        result = cursor.fetchone()

        if result and result[0] == "Borrowed":
            cursor.execute("UPDATE books SET status='Available' WHERE book_id=?", (book_id,))
            cursor.execute("UPDATE transactions SET returned=1 WHERE book_id=?", (book_id,))
            conn.commit()
            messagebox.showinfo("Success", "Book returned successfully!")
        else:
            messagebox.showerror("Error", "Invalid Book ID or not borrowed.")

    def view_books(self):
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        books_str = "Book ID | Title | Author | Status\n" + "-" * 40 + "\n"
        for book in books:
            books_str += f"{book[0]} | {book[1]} | {book[2]} | {book[3]}\n"

        messagebox.showinfo("Library Books", books_str)


# Run the application
root = tk.Tk()
app = LibraryApp(root)
root.mainloop()

# Close the database connection when finished
conn.close()