# import tkinter as tk
# from tkinter import messagebox
# from tkcalendar import DateEntry
# from datetime import datetime

# class LibraryManagementSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Clifton Public Library Management System")
#         self.root.geometry("600x400")
#         self.root.config(bg='#424242')  # Setting the background color to dark grey

#         # Configure button style for better contrast and visibility
#         button_style = {'bg': '#424242', 'fg': 'white', 'bd': 1, 'relief': 'flat'}

#         # Add Book Button
#         tk.Button(self.root, text="Add Book", command=self.add_book, **button_style).pack(pady=10)

#         # Check Out Book Button
#         tk.Button(self.root, text="Check Out Book", command=self.check_out_book, **button_style).pack(pady=10)

#         # Return Book Button
#         tk.Button(self.root, text="Return Book", command=self.return_book, **button_style).pack(pady=10)

#         # Notifications Button
#         tk.Button(self.root, text="Notifications", command=self.show_notifications, **button_style).pack(pady=10)

#     def add_book(self):
#         add_window = self.create_toplevel_window("Add Book", "300x300")
#         tk.Label(add_window, text="Enter Book ID:", bg='#424242', fg='white').pack()
#         book_id_entry = tk.Entry(add_window, width=25)
#         book_id_entry.pack()
#         tk.Label(add_window, text="Enter ISBN:", bg='#424242', fg='white').pack()
#         book_id_entry = tk.Entry(add_window, width=25)
#         book_id_entry.pack()
#         tk.Label(add_window, text="Enter Publication Year:(YYYY)", bg='#424242', fg='white').pack()
#         book_id_entry = tk.Entry(add_window, width=25)
#         book_id_entry.pack()
#         tk.Label(add_window, text="Enter Book Title:", bg='#424242', fg='white').pack()
#         title_entry = tk.Entry(add_window, width=25)
#         title_entry.pack()
#         tk.Label(add_window, text="Enter Author Name:", bg='#424242', fg='white').pack()
#         author_entry = tk.Entry(add_window, width=25)
#         author_entry.pack()
#         tk.Button(add_window, text="Submit", command=lambda: self.save_book(book_id_entry.get(), title_entry.get(), author_entry.get())).pack(pady=10)

#     def check_out_book(self):
#         checkout_window = self.create_toplevel_window("Check Out Book", "350x250")
#         tk.Label(checkout_window, text="Enter Member ID:", bg='#424242', fg='white').pack()
#         member_id_entry = tk.Entry(checkout_window, width=25)
#         member_id_entry.pack()
#         tk.Label(checkout_window, text="Enter Book ID:", bg='#424242', fg='white').pack()
#         book_id_entry = tk.Entry(checkout_window, width=25)
#         book_id_entry.pack()
#         tk.Label(checkout_window, text="Select Due Date:", bg='#424242', fg='white').pack()
#         due_date_entry = DateEntry(checkout_window, width=25, year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
#         due_date_entry.pack()
#         tk.Button(checkout_window, text="Check Out", command=lambda: self.process_checkout(member_id_entry.get(), book_id_entry.get(), due_date_entry.get_date())).pack(pady=10)

#     def return_book(self):
#         return_window = self.create_toplevel_window("Return Book", "350x250")
#         tk.Label(return_window, text="Enter Book ID:", bg='#424242', fg='white').pack()
#         book_id_entry = tk.Entry(return_window, width=25)
#         book_id_entry.pack()
#         tk.Label(return_window, text="Select Return Date:", bg='#424242', fg='white').pack()
#         return_date_entry = DateEntry(return_window, width=25, year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
#         return_date_entry.pack()
#         tk.Button(return_window, text="Return", command=lambda: self.process_return(book_id_entry.get(), return_date_entry.get_date())).pack(pady=10)

#     def show_notifications(self):
#         messagebox.showinfo("Notifications", "List of overdue books and alerts here", bg='#424242', fg='white')

#     def create_toplevel_window(self, title, size):
#         top_window = tk.Toplevel(self.root)
#         top_window.title(title)
#         top_window.geometry(size)
#         top_window.config(bg='#424242')
#         return top_window

#     def save_book(self, book_id, title, author):
#         messagebox.showinfo("Success", f"Book with ID {book_id} added successfully!")

#     def process_checkout(self, member_id, book_id, due_date):
#         messagebox.showinfo("Success", f"Book checked out successfully! Due date is {due_date}.")

#     def process_return(self, book_id, return_date):
#         messagebox.showinfo("Success", f"Book returned successfully! Return date was {return_date}.")

# # Create the main window and pass it to the LibraryManagementSystem class
# root = tk.Tk()
# app = LibraryManagementSystem(root)
# root.mainloop()

