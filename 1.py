import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Clifton Public Library Management System")
        self.root.geometry("600x400")
        
        # Add Book Button
        tk.Button(self.root, text="Add Book", command=self.add_book).pack(pady=10)
        
        # Check Out Book Button
        tk.Button(self.root, text="Check Out Book", command=self.check_out_book).pack(pady=10)
        
        # Return Book Button
        tk.Button(self.root, text="Return Book", command=self.return_book).pack(pady=10)
        
        # Notifications Button
        tk.Button(self.root, text="Notifications", command=self.show_notifications).pack(pady=10)

    def add_book(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Book")
        add_window.geometry("300x200")
        tk.Label(add_window, text="Enter Book Title:").pack()
        title_entry = tk.Entry(add_window, width=25)
        title_entry.pack()
        tk.Label(add_window, text="Enter Author Name:").pack()
        author_entry = tk.Entry(add_window, width=25)
        author_entry.pack()
        tk.Button(add_window, text="Submit", command=lambda: self.save_book(title_entry.get(), author_entry.get())).pack(pady=10)

    def check_out_book(self):
        checkout_window = tk.Toplevel(self.root)
        checkout_window.title("Check Out Book")
        checkout_window.geometry("350x250")
        tk.Label(checkout_window, text="Enter Member ID:").pack()
        member_id_entry = tk.Entry(checkout_window, width=25)
        member_id_entry.pack()
        tk.Label(checkout_window, text="Enter Book ID:").pack()
        book_id_entry = tk.Entry(checkout_window, width=25)
        book_id_entry.pack()
        tk.Label(checkout_window, text="Select Due Date:").pack()
        due_date_entry = DateEntry(checkout_window, width=25, year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        due_date_entry.pack()
        tk.Button(checkout_window, text="Check Out", command=lambda: self.process_checkout(member_id_entry.get(), book_id_entry.get(), due_date_entry.get_date())).pack(pady=10)

    def return_book(self):
        return_window = tk.Toplevel(self.root)
        return_window.title("Return Book")
        return_window.geometry("350x250")
        tk.Label(return_window, text="Enter Book ID:").pack()
        book_id_entry = tk.Entry(return_window, width=25)
        book_id_entry.pack()
        tk.Label(return_window, text="Select Return Date:").pack()
        return_date_entry = DateEntry(return_window, width=25, year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        return_date_entry.pack()
        tk.Button(return_window, text="Return", command=lambda: self.process_return(book_id_entry.get(), return_date_entry.get_date())).pack(pady=10)

    def show_notifications(self):
        messagebox.showinfo("Notifications", "List of overdue books and alerts here")

    def save_book(self, title, author):
        messagebox.showinfo("Success", "Book added successfully!")

    def process_checkout(self, member_id, book_id, due_date):
        # Since DateEntry returns a datetime.date object, it is already valid
        messagebox.showinfo("Success", f"Book checked out successfully! Due date is {due_date}.")

    def process_return(self, book_id, return_date):
        # Since DateEntry returns a datetime.date object, it is already valid
        messagebox.showinfo("Success", f"Book returned successfully! Return date was {return_date}.")

# Create the main window and pass it to the LibraryManagementSystem class
root = tk.Tk()
app = LibraryManagementSystem(root)
root.mainloop()
