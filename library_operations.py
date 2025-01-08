"""
Library Operations Module
Copyright 2025, Surbhi Sharma
"""
from Project.library_io import save_library

def add_book(library, title, author, quantity):
    """
    Add a new book to the library or update the quantity if the book already exists.
    """
    if title in library:
        print("Book already exists. Updating the quantity.")
        library[title]['quantity'] += quantity
    else:
        library[title] = {'author': author, 'quantity': quantity, 'borrowed_by': None}
    save_library(library)
    print(f"Book '{title}' added successfully")

def view_books(library):
    """
    Display all books in the library along with their details.
    """
    if not library:
        print("The library is currently empty.")
        return

    for title, details in library.items():
        status = f"Available Books: ({details['quantity']})" if not details['borrowed_by'] else f"Borrowed by {details['borrowed_by']}"
        print(f"Title: {title}, Author: {details['author']}, Status: {status}")

def borrow_book(library, title, borrower_name):
    """
    Allow a user to borrow a book from the library.
    """
    if title not in library:
        print(f"'{title}' not found in the library.")
        return

    if library[title]['quantity'] == 0:
        print(f"All copies of '{title}' are currently borrowed.")
        return

    if library[title]['borrowed_by']:
        print(f"The book '{title}' is already borrowed by {library[title]['borrowed_by']}.")
        return

    library[title]['quantity'] -= 1
    library[title]['borrowed_by'] = borrower_name
    save_library(library)
    print(f"'{title}' has been successfully borrowed by {borrower_name}.")

def return_book(library, title):
    """
    Allow a user to return a borrowed book to the library.
    """
    if title not in library:
        print("Book not found in the library.")
        return

    if not library[title]['borrowed_by']:
        print(f"The book '{title}' was not borrowed.")
        return

    library[title]['quantity'] += 1
    borrower_name = library[title]['borrowed_by']
    library[title]['borrowed_by'] = None
    save_library(library)
    print(f"'{title}' has been successfully returned by {borrower_name}.")