# Library Book Inventory Manager

LINKEDIN POST LINK
https://www.linkedin.com/posts/esha-ghosh_github-eshag23syntecxhublibrary-book-inventory-manager-share-7471089169990119425-DRg9/?utm_source=share&utm_medium=member_ios&rcm=ACoAAFFbqJMB3C11ce_6iHE3z-F1nQd6d4mvOkg


## Project Overview

The **Library Book Inventory Manager** is a console-based Python application designed to manage a library's book inventory efficiently. The system allows staff members to add, delete, search, and manage books, while customers can register, log in, borrow books, return books, and view their borrowing history.

The project uses **Object-Oriented Programming (OOP)** concepts, **Python dictionaries (HashMap-like structure)** for fast book lookup, and **JSON file storage** for persistent data management.

---

## Features

### Staff Module

* Add new books
* Delete existing books
* View all books
* Search books by title or author
* View customer borrowing records
* Generate library reports

### Customer Module

* New customer registration
* Customer login authentication
* Search books
* Borrow books
* Return books
* View borrowed books

### Data Persistence

* Stores book information in `books.json`
* Stores user information in `users.json`
* Automatically reloads data when the program starts

### Reporting

* Total book copies
* Issued book copies
* Available book copies
* Total unique book titles

---

## Technologies Used

* Python 3
* Object-Oriented Programming (Classes & Objects)
* JSON File Handling
* Dictionaries (HashMap Implementation)
* Lists and Iteration

---

## Project Structure

```text
Library_Project/
│
├── library_book_inventory_manager.py
├── books.json
├── users.json
└── README.md
```

---

## Classes Used

### Book Class

Stores information about each book:

* Book ID
* Title
* Author
* Total Copies
* Issued Copies

Methods:

* Available Copies Calculation
* JSON Conversion

### Library Class

Handles:

* Book Management
* User Management
* Borrowing & Returning
* Searching
* Reporting
* Data Storage

---

## Functionalities

### Add Book

Staff can add a new book by providing:

* Book ID
* Title
* Author
* Number of Copies

### Search Book

Search using:

* Book Title
* Author Name

### Borrow Book

Customers can:

* View available books
* Select a book
* Borrow if copies are available

### Return Book

Customers can:

* View borrowed books
* Return borrowed books

### Reports

Generate:

* Total Books
* Issued Books
* Available Books
* Number of Unique Titles

---

## File Storage

### books.json

Stores:

```json
{
  "book_id": "101",
  "title": "Python Programming",
  "author": "Guido",
  "total_copies": 5,
  "issued_count": 2
}
```

### users.json

Stores:

```json
{
  "esha": {
    "password": "1234",
    "borrowed_books": {
      "101": {
        "title": "Python Programming",
        "borrowed_on": "08-06-2026 10:30:00"
      }
    }
  }
}
```

---

## How to Run

### Step 1

Save the source code as:

```text
library_book_inventory_manager.py
```

### Step 2

Open terminal in the project folder.

### Step 3

Run:

```bash
python library_book_inventory_manager.py
```

---

## Default Staff Credentials

```text
Password: admin123
```

---

## Sample Workflow

### Staff

```text
1. Staff Login
2. Add Book
3. View Books
4. Generate Reports
```

### Customer

```text
1. Register
2. Login
3. Search Book
4. Borrow Book
5. Return Book
6. Logout
```

---

## Concepts Demonstrated

* Classes and Objects
* Encapsulation
* File Handling
* JSON Serialization
* Dictionaries (HashMap)
* Lists
* Searching Algorithms
* Menu-Driven Programming
* Data Persistence
* Exception Handling

---

## Learning Outcomes

After completing this project, students will understand:

* Object-Oriented Programming in Python
* File-based Database Systems
* Collection Frameworks (Lists & Dictionaries)
* Real-world Inventory Management Systems
* Menu-driven Console Applications

---

## Author

**Esha Ghosh**
B.Tech Computer Science & Engineering
Ramdeobaba University, Nagpur

---

**Project Title:** Library Book Inventory Manager
**Language:** Python
**Type:** Console-Based Inventory Management System
**Storage:** JSON Files
**Version:** 1.0 
