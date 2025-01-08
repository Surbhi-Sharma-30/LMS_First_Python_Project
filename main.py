"""
Library Management System
Copyright 2025, Surbhi Sharma
"""
from Project.library_io import load_library
from Project.library_operations import add_book, view_books, borrow_book, return_book

def main():
    """
    Main menu to navigate and perform library management operations.
    """
    library = load_library()

    while True:
        print("\t\t\t==============================================================")
        print("\n\t\t\t******** WELCOME TO SHIKSHA LIBRARY MANAGEMENT SYSTEM ********")
        print("\t\t\t==============================================================")
        print("""CHOOSE WHAT YOU WANT TO DO:-
1. Add Book
2. View Books
3. Borrow Book
4. Return Book
5. Exit the library
""")
        choice = input("Enter Your Choice (1-5): ")

        if choice == '1':  # Add a Book
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            try:
                quantity = int(input("Enter the number of copies: "))
                add_book(library, title, author, quantity)
            except ValueError:
                print("Invalid input for quantity. Please enter an integer.")

        elif choice == '2':  # View Books
            view_books(library)

        elif choice == '3':  # Borrow a Book
            title = input("Enter the book title to borrow: ")
            borrower_name = input("Enter your name: ")
            borrow_book(library, title, borrower_name)

        elif choice == '4':  # Return a Book
            title = input("Enter the book title to return: ")
            return_book(library, title)

        elif choice == '5':  # Exit the library
            print("\n\n\t\t\t======================================================")
            print("\t\t\tThank You for using Shiksha Library Management System.\n\t\t\t\t\t******Good Bye!!!******")
            break  # Exit the loop

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")  # Error handle

if __name__ == "__main__":
    main()