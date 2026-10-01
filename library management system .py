####    LIBRARY MANAGEMENT SYSTEM    ####

class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

class Library:

    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self):

        book_id = input("Enter Book ID: ").strip()

        if book_id == "":
            print("Book ID cannot be empty.")
            return

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists.")
                return

        title = input("Enter Book Title: ").strip()

        if title == "":
            print("Book title cannot be empty.")
            return

        author = input("Enter Author Name: ").strip()

        if author == "":
            print("Author name cannot be empty.")
            return

        new_book = Book(book_id, title, author)

        self.books.append(new_book)

        print("Book added successfully.")

    def view_books(self):

        if len(self.books) == 0:
            print("No books available in the library.")
            return

        print("    LIBRARY BOOKS    ")

        for book in self.books:

            if book.is_available:
                status = "Available"
            else:
                status = "Borrowed"

            print("Book ID :", book.book_id)
            print("Title   :", book.title)
            print("Author  :", book.author)
            print("Status  :", status)

    def search_book(self):

        search = input("Enter Book ID or Title to search: ").strip().lower()

        if search == "":
            print("Search value cannot be empty.")
            return

        found = False

        for book in self.books:

            if (book.book_id.lower() == search or
                    book.title.lower() == search):

                print("\nBook Found!")
                print("Book ID :", book.book_id)
                print("Title   :", book.title)
                print("Author  :", book.author)

                if book.is_available:
                    print("Status  : Available")
                else:
                    print("Status  : Borrowed")

                found = True

        if not found:
            print("Book not found.")

    def borrow_book(self):

        if len(self.books) == 0:
            print("No books available.")
            return

        book_id = input("Enter Book ID to borrow: ").strip()

        if book_id == "":
            print("Book ID cannot be empty.")
            return

        selected_book = None

        for book in self.books:

            if book.book_id == book_id:
                selected_book = book
                break

        if selected_book is None:
            print("Book not found.")
            return

        if not selected_book.is_available:
            print("Book is already borrowed.")
            return

        student_name = input("Enter Student Name: ").strip()

        if student_name == "":
            print("Student name cannot be empty.")
            return

        selected_book.is_available = False

        self.borrowed_books[book_id] = student_name

        print("Book borrowed successfully.")

    def return_book(self):

        book_id = input("Enter Book ID to return: ").strip()

        if book_id == "":
            print("Book ID cannot be empty.")
            return

        if book_id not in self.borrowed_books:
            print("This book is not currently borrowed.")
            return

        for book in self.books:

            if book.book_id == book_id:
                book.is_available = True
                break

        del self.borrowed_books[book_id]

        print("Book returned successfully.")

    def view_borrowed_books(self):

        if len(self.borrowed_books) == 0:
            print("No books are currently borrowed.")
            return

        print("    BORROWED BOOKS    ")

        for book_id, student_name in self.borrowed_books.items():

            print("Book ID      :", book_id)
            print("Borrowed By  :", student_name)

library = Library()

while True:

    print("     LIBRARY MANAGEMENT SYSTEM")

    print("1] Add Book")
    print("2] View Books")
    print("3] Search Book")
    print("4] Borrow Book")
    print("5] Return Book")
    print("6] View Borrowed Books")
    print("7] Exit")

    choice = input("Enter Your Choice: ").strip()

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.borrow_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.view_borrowed_books()

    elif choice == "7":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")