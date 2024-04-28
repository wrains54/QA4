import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, Entry, Button
from tkcalendar import DateEntry
from datetime import datetime
import sqlite3

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x300")
        self.db = sqlite3.connect('library.db')
        self.db.row_factory = sqlite3.Row

        self.setup_database()

        Button(root, text="Add or Update Book", command=self.manage_books).pack(pady=10)
        Button(root, text="Search Books", command=self.search_books).pack(pady=10)
        Button(root, text="Check Out Book", command=lambda: self.checkout_return_book("out")).pack(pady=10)
        Button(root, text="Return Book", command=lambda: self.checkout_return_book("in")).pack(pady=10)
        Button(root, text="Show Notifications", command=self.show_notifications).pack(pady=10)

    def setup_database(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT UNIQUE,
                status TEXT DEFAULT 'available'
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                member_id INTEGER,
                checkout_date DATE,
                due_date DATE,
                return_date DATE,
                FOREIGN KEY (book_id) REFERENCES books(book_id)
            );
        ''')
        self.db.commit()

    def manage_books(self):
        window = Toplevel(self.root)
        window.title("Add or Update Book")
        Label(window, text="Book ID (leave empty to add new):").pack()
        book_id_entry = Entry(window)
        book_id_entry.pack()

        Label(window, text="Title:").pack()
        title_entry = Entry(window)
        title_entry.pack()

        Label(window, text="Author:").pack()
        author_entry = Entry(window)
        author_entry.pack()

        Label(window, text="ISBN:").pack()
        isbn_entry = Entry(window)
        isbn_entry.pack()

        Button(window, text="Submit", command=lambda: self.submit_book(
            book_id_entry.get(), title_entry.get(), author_entry.get(), isbn_entry.get(), window)).pack()

    def submit_book(self, book_id, title, author, isbn, window):
        if book_id:
            self.db.execute('UPDATE books SET title=?, author=?, isbn=? WHERE book_id=?', (title, author, isbn, book_id))
        else:
            self.db.execute('INSERT INTO books (title, author, isbn, status) VALUES (?, ?, ?, "available")', (title, author, isbn))
        self.db.commit()
        window.destroy()
        messagebox.showinfo("Success", "Book saved successfully!")

    def search_books(self):
        search_term = simpledialog.askstring("Search", "Enter title, author, or ISBN:", parent=self.root)
        if search_term:
            books = self.db.execute('''
                SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?
            ''', ('%'+search_term+'%', '%'+search_term+'%', '%'+search_term+'%')).fetchall()

            if books:
                message = "\n".join([f"ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {book['status']}" for book in books])
                messagebox.showinfo("Search Results", message)
            else:
                messagebox.showinfo("Search Results", "No books found.")

    def checkout_return_book(self, action):
        window = Toplevel(self.root)
        window.title(f"Book Check {action}")
        Label(window, text="Book ID:").pack()
        book_id_entry = Entry(window)
        book_id_entry.pack()

        if action == "out":
            Label(window, text="Due Date:").pack()
            due_date_entry = DateEntry(window)
            due_date_entry.pack()
            Button(window, text=f"Check {action}", command=lambda: self.process_checkout(
                book_id_entry.get(), due_date_entry.get_date(), window)).pack()
        else:
            Button(window, text=f"Check {action}", command=lambda: self.process_return(
                book_id_entry.get(), window)).pack()

    def process_checkout(self, book_id, due_date, window):
        current_date = datetime.now().strftime('%Y-%m-%d')
        self.db.execute('UPDATE books SET status="checked out" WHERE book_id=?', (book_id,))
        self.db.execute('INSERT INTO transactions (book_id, checkout_date, due_date) VALUES (?, ?, ?)',
                        (book_id, current_date, due_date.strftime('%Y-%m-%d')))
        self.db.commit()
        window.destroy()
        messagebox.showinfo("Success", f"Book checked out successfully on {current_date}! Due date is {due_date.strftime('%Y-%m-%d')}.")

    def process_return(self, book_id, window):
        current_date = datetime.now().strftime('%Y-%m-%d')
        self.db.execute('UPDATE books SET status="available" WHERE book_id=?', (book_id,))
        self.db.execute('UPDATE transactions SET return_date=? WHERE book_id=? AND return_date IS NULL',
                        (current_date, book_id))
        self.db.commit()
        window.destroy()
        messagebox.showinfo("Success", "Book returned successfully!")

    def show_notifications(self):
        overdue_books = self.db.execute('SELECT title, due_date FROM books JOIN transactions ON books.book_id = transactions.book_id WHERE return_date IS NULL AND due_date < ?', (datetime.now().strftime('%Y-%m-%d'),)).fetchall()
        message = "Overdue Books:\n\n" + "\n".join([f"{book['title']} was due on {book['due_date']}" for book in overdue_books])
        messagebox.showinfo("Notifications", message if overdue_books else "No overdue books.")

# GUI setup
root = tk.Tk()
app = LibraryApp(root)
root.mainloop()


