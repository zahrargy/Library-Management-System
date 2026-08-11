📚 Library Management System

A simple, menu-driven Library Management System built in Python using Object-Oriented Programming principles — no inheritance, just clean class composition.

Overview

This project simulates the core operations of a real library: adding books and members, lending and returning books, searching by author, and tracking library statistics — all through an interactive command-line menu.

Features
Add Books — Store book details (name, writer, ISBN, genre, availability status)
Add Members — Register library members with unique IDs
Lend Book — Check availability and lend a book to a member
Return Book — Process returns and update book availability
Search by Writer — Find all books by a specific author
Available Books — List all currently available books
Most Active Member — Identify the member who has borrowed the most books
Genre Tracking — Maintain a set of unique genres in the library
Project Structure

The project uses three core classes:

Class	Responsibility
Book	Represents a single book (name, writer, ISBN, status, genre)
Member	Represents a library member and their borrowed books
Library	Manages the collection of books, members, and all operations
Concepts Used
Object-Oriented Programming (classes, __init__, __str__)
Dictionaries (books and members are stored by unique keys)
Lists (tracking each member's borrowed books)
Sets (tracking unique genres)
Exception handling (try/except for invalid input)
Interactive CLI menu with a while loop
How to Run
bash
python MyLibrary.py

You'll be prompted to name your library, then presented with a menu:

1. Add Book
2. Add Member
3. Lend Book
4. Return Book
5. Search by Writer
6. Available Books
7. Most Active Member
8. Exit
Example
Enter Library Name: City Library
1. Add Book
...
Enter BookName: Clean Code
Enter Writer: Robert C. Martin
Is it Available: (True/False) True
Enter isbn: 111
Enter jenre: Programming
Clean Code Added!
Author

Built as a hands-on practice project to strengthen OOP fundamentals in Python — classes, data structures (lists, dicts, sets), and interactive program design.
