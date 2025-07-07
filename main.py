import json
import os
from dataclasses import dataclass, asdict
from typing import List
from tabulate import tabulate

print("="*40)
print(" " * 10 + "Book Store Management")
print("="*40)


@dataclass
class Book:
    serial_number: int
    title: str
    author: str
    isbn: str
    price: float
    stock: int

@dataclass
class Customer:
    name: str
    phone: str
    purchased_books: List[Book]

# Sample book list
book_list = [
    Book(serial_number=1, title="To Kill a Mockingbird", author="Harper Lee", isbn="9780061120084", price=7.19, stock=12),
    Book(serial_number=2, title="1984", author="George Orwell", isbn="9780451524935", price=6.89, stock=8),
    Book(serial_number=3, title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="9780743273565", price=10.29, stock=5),
    Book(serial_number=4, title="Pride and Prejudice", author="Jane Austen", isbn="9780141439518", price=5.99, stock=10),
    Book(serial_number=5, title="The Catcher in the Rye", author="J.D. Salinger", isbn="9780316769488", price=8.99, stock=7),
    Book(serial_number=6, title="The Hobbit", author="J.R.R. Tolkien", isbn="9780547928227", price=8.79, stock=9),
    Book(serial_number=7, title="Fahrenheit 451", author="Ray Bradbury", isbn="9781451673319", price=7.99, stock=4),
    Book(serial_number=8, title="Jane Eyre", author="Charlotte Brontë", isbn="9780142437209", price=7.95, stock=6),
    Book(serial_number=9, title="Animal Farm", author="George Orwell", isbn="9780451526342", price=7.19, stock=11),
    Book(serial_number=10, title="Over a Sea", author="Herman Melville", isbn="9781503280786", price=9.99, stock=3)
]

# Conversion rate from USD to INR
usd_to_inr = 83.0

# Function to view available books
def view_books():
    print("\nAvailable Books:")
    table = []
    for book in book_list:
        inr_price = book.price * usd_to_inr
        table.append([book.serial_number, book.title, book.author, f"₹{inr_price:.2f}", book.stock])
    headers = ["Serial No", "Title", "Author", "Price (INR)", "Stock"]
    print(tabulate(table, headers, tablefmt="grid"))
    print()

# Function to purchase a book
def buy_book(serial_number: int, customer: Customer):
    for book in book_list:
        if book.serial_number == serial_number:
            if book.stock > 0:
                book.stock -= 1
                customer.purchased_books.append(book)
                print(f"You have purchased '{book.title}' by {book.author}.")
                return
            else:
                print("Sorry, this book is out of stock.")
                return
    print("Invalid serial number. Please try again.")

# Function to save customer data to 'purchases/' folder
def save_customer_data(customer: Customer):
    os.makedirs("purchases", exist_ok=True)  # Create folder if not exists
    customer_data = asdict(customer)
    file_path = f"purchases/{customer.name.replace(' ', '_').lower()}_purchases.json"
    with open(file_path, "w") as file:
        json.dump(customer_data, file, indent=4)
    print(f"Customer data saved for {customer.name} in '{file_path}'.")

# Function to display customers and their purchases
def view_customers(customers: List[Customer]):
    print("\nList of Customers Who Purchased Books:")
    customer_table = []
    for customer in customers:
        book_titles = ", ".join([book.title for book in customer.purchased_books])
        customer_table.append([customer.name, customer.phone, book_titles])
    headers = ["Name", "Phone", "Purchased Books"]
    print(tabulate(customer_table, headers, tablefmt="grid"))
    print()

# Function to view saved customers from JSON files
def view_saved_customers():
    import glob

    customer_files = glob.glob("purchases/*_purchases.json")
    customers = []

    for file_name in customer_files:
        with open(file_name, "r") as file:
            customer_data = json.load(file)
            customer = Customer(
                name=customer_data["name"],
                phone=customer_data["phone"],
                purchased_books=[
                    Book(**book) for book in customer_data["purchased_books"]
                ]
            )
            customers.append(customer)

    if customers:
        view_customers(customers)
    else:
        print("No customers have purchased books yet.")

# Main program loop
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. View Available Books")
        print("2. Buy a Book")
        print("3. View Purchased Customers (Owner Only)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_books()

        elif choice == "2":
            customer_name = input("Enter your name: ")
            customer_phone = input("Enter your phone number: ")
            customer = Customer(name=customer_name, phone=customer_phone, purchased_books=[])

            while True:
                try:
                    serial_number = int(input("Enter the serial number of the book to purchase (0 to finish): "))
                    if serial_number == 0:
                        break
                    buy_book(serial_number, customer)
                except ValueError:
                    print("Invalid input. Please enter a number.")

            save_customer_data(customer)
            view_customers([customer])

        elif choice == "3":
            print("\nPurchased Customers:")
            view_saved_customers()

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
