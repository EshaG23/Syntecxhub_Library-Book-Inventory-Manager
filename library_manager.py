import json
import os
from datetime import datetime


BOOKS_FILE = "books.json"
USERS_FILE = "users.json"


class Book:
    def __init__(self, book_id, title, author, total_copies, issued_count=0):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.issued_count = issued_count

    def available_copies(self):
        return self.total_copies - self.issued_count

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "total_copies": self.total_copies,
            "issued_count": self.issued_count
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["book_id"],
            data["title"],
            data["author"],
            data["total_copies"],
            data.get("issued_count", 0)
        )


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r") as file:
                data = json.load(file)
                for item in data:
                    book = Book.from_dict(item)
                    self.books[book.book_id] = book

        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as file:
                self.users = json.load(file)

    def save_data(self):
        with open(BOOKS_FILE, "w") as file:
            json.dump([book.to_dict() for book in self.books.values()], file, indent=4)

        with open(USERS_FILE, "w") as file:
            json.dump(self.users, file, indent=4)

    def add_book(self):
        book_id = input("Enter Book ID: ").strip()

        if book_id in self.books:
            print("Book ID already exists.")
            return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        try:
            total_copies = int(input("Enter Total Copies: "))
            if total_copies <= 0:
                print("Copies must be greater than 0.")
                return
        except ValueError:
            print("Invalid number.")
            return

        self.books[book_id] = Book(book_id, title, author, total_copies)
        self.save_data()
        print("Book added successfully.")

    def delete_book(self):
        book_id = input("Enter Book ID to delete: ").strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        if self.books[book_id].issued_count > 0:
            print("Cannot delete. Some copies are currently issued.")
            return

        del self.books[book_id]
        self.save_data()
        print("Book deleted successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n----- Book List -----")
        for book in self.books.values():
            print(f"""
Book ID        : {book.book_id}
Title          : {book.title}
Author         : {book.author}
Total Copies   : {book.total_copies}
Issued Copies  : {book.issued_count}
Available      : {book.available_copies()}
-------------------------
""")

    def search_book(self):
        keyword = input("Enter title or author to search: ").lower().strip()
        found = False

        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                print(f"""
Book ID      : {book.book_id}
Title        : {book.title}
Author       : {book.author}
Available    : {book.available_copies()}
""")
                found = True

        if not found:
            print("No matching book found.")

    def borrow_book(self, username):
        self.display_books()

        book_id = input("Enter Book ID to borrow: ").strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if book.available_copies() <= 0:
            print("Book is currently not available.")
            return

        if book_id in self.users[username]["borrowed_books"]:
            print("You have already borrowed this book.")
            return

        book.issued_count += 1
        self.users[username]["borrowed_books"][book_id] = {
            "title": book.title,
            "borrowed_on": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        self.save_data()
        print("Book borrowed successfully.")

    def return_book(self, username):
        borrowed = self.users[username]["borrowed_books"]

        if not borrowed:
            print("You have not borrowed any books.")
            return

        print("\nYour Borrowed Books:")
        for book_id, details in borrowed.items():
            print(f"{book_id} - {details['title']} | Borrowed on: {details['borrowed_on']}")

        book_id = input("Enter Book ID to return: ").strip()

        if book_id not in borrowed:
            print("This book is not in your borrowed list.")
            return

        if book_id in self.books:
            self.books[book_id].issued_count -= 1

        del self.users[username]["borrowed_books"][book_id]
        self.save_data()
        print("Book returned successfully.")

    def reports(self):
        total_books = sum(book.total_copies for book in self.books.values())
        issued_books = sum(book.issued_count for book in self.books.values())
        available_books = total_books - issued_books

        print("\n----- Library Report -----")
        print("Total Book Copies   :", total_books)
        print("Issued Book Copies  :", issued_books)
        print("Available Copies    :", available_books)
        print("Unique Book Titles  :", len(self.books))
        print("--------------------------")

    def create_user(self):
        username = input("Create username: ").strip()
        password = input("Create password: ").strip()

        if username in self.users:
            print("Username already exists.")
            return

        self.users[username] = {
            "password": password,
            "borrowed_books": {}
        }

        self.save_data()
        print("Customer account created successfully.")

    def login_user(self):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if username in self.users and self.users[username]["password"] == password:
            print("Login successful.")
            return username

        print("Invalid username or password.")
        return None

    def view_customer_list(self):
        if not self.users:
            print("No customers found.")
            return

        print("\n----- Customer List -----")
        for username, details in self.users.items():
            print(f"Username: {username}")
            print("Borrowed Books:")
            if details["borrowed_books"]:
                for book_id, book_data in details["borrowed_books"].items():
                    print(f"  {book_id} - {book_data['title']}")
            else:
                print("  No books borrowed")
            print("-------------------------")

    def view_my_books(self, username):
        borrowed = self.users[username]["borrowed_books"]

        if not borrowed:
            print("You have not borrowed any books.")
            return

        print("\n----- My Borrowed Books -----")
        for book_id, details in borrowed.items():
            print(f"{book_id} - {details['title']} | Borrowed on: {details['borrowed_on']}")


def staff_menu(library):
    while True:
        print("""
========== Staff Menu ==========
1. Add Book
2. Delete Book
3. Display All Books
4. Search Book
5. View Customer List
6. Library Reports
7. Back to Main Menu
""")

        choice = input("Enter choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.delete_book()
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            library.search_book()
        elif choice == "5":
            library.view_customer_list()
        elif choice == "6":
            library.reports()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


def customer_menu(library, username):
    while True:
        print(f"""
========== Customer Menu ==========
Logged in as: {username}

1. Display Available Books
2. Search Book
3. Borrow Book
4. Return Book
5. View My Borrowed Books
6. Logout
""")

        choice = input("Enter choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            library.search_book()
        elif choice == "3":
            library.borrow_book(username)
        elif choice == "4":
            library.return_book(username)
        elif choice == "5":
            library.view_my_books(username)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def main():
    library = Library()

    while True:
        print("""
========== Library Book Inventory Manager ==========
1. Staff
2. Customer
3. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            staff_password = input("Enter staff password: ")

            if staff_password == "admin123":
                staff_menu(library)
            else:
                print("Wrong staff password.")

        elif choice == "2":
            while True:
                print("""
========== Customer ==========
1. New Customer Registration
2. Customer Login
3. Back
""")

                customer_choice = input("Enter choice: ")

                if customer_choice == "1":
                    library.create_user()

                elif customer_choice == "2":
                    username = library.login_user()
                    if username:
                        customer_menu(library, username)

                elif customer_choice == "3":
                    break

                else:
                    print("Invalid choice.")

        elif choice == "3":
            print("Thank you for using Library Book Inventory Manager.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()