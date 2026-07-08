# Shopping Cart System

A simple console-based **Shopping Cart System** built with Python. This project demonstrates how products and a shopping cart interact while performing inventory operations. It focuses on CRUD operations, stock management, and real-world shopping cart logic.

## Features

* View available products
* Add products to cart
* Prevent duplicate Product IDs
* Check stock availability before adding items
* Automatically reduce stock when items are added
* View cart with subtotals
* Update product quantity in the cart
* Remove products from the cart
* Calculate the total bill
* Checkout and clear the cart
* Input validation and exception handling

## Technologies Used

* Python 3

## Concepts Covered

* Functions
* Lists
* Dictionaries
* CRUD Operations
* Loops
* Conditional Statements
* Exception Handling (`try` / `except`)
* Input Validation
* List Methods (`append()`, `remove()`, `clear()`)
* Built-in Functions (`sum()`, `next()`)
* Inventory & Cart Interaction
* Problem Solving

## Project Structure

```text
Shopping-Cart-System/
│
├── Shopping Cart System.py
└── README.md
```

## Example Output

```text
============ Welcome to Shopping Cart System =============

=============== Select the Option (0-7) ===============
1. View Products
2. Add to Cart
3. Remove from Cart
4. View Cart
5. Update Cart
6. Calculate Total
7. Checkout
0. Exit

Enter the number: 2

Enter the Product ID: 101
Enter the Quantity: 2

Product added to cart successfully!

Enter the number: 4

---------------------------------------------------
Name: Keyboard
Category: Electronics
Product ID: 101
Price: 2500.0
Quantity: 2
Total: 5000.0
---------------------------------------------------

Enter the number: 6

Grand Total: 5000.0

Enter the number: 7

Your total amount is: 5000.0
Proceeding to checkout...
Thank you for shopping with us!
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/osaid400/Shopping-Cart-System.git
```

2. Navigate to the project folder:

```bash
cd Shopping-Cart-System
```

3. Run the program:

```bash
python "Shopping Cart System.py"
```

## Future Improvements

* Search products
* Apply discount coupons
* Generate invoices
* Save cart using file handling
* Store products in SQLite
* User authentication
* Product categories filtering

## Learning Outcomes

This project helped me practice:

* Managing multiple data structures
* Synchronizing inventory with cart operations
* Implementing business logic
* Writing modular functions
* Performing CRUD operations
* Improving debugging and problem-solving skills

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
