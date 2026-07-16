# Shopping Cart System (Python)

A beginner-friendly console-based Shopping Cart System built with Python. This project demonstrates how to manage products, carts, inventory, and receipts while storing data permanently using **JSON File Handling**.

## Features

* View available products
* Add products to cart
* Remove products from cart
* Update product quantity
* Calculate grand total
* Checkout with customer details
* Generate receipt
* Automatic stock management
* Persistent data storage using JSON
* Input validation and exception handling

## Technologies Used

* Python 3
* JSON
* File Handling
* `datetime` Module

## Project Structure

```text
Shopping-Cart-System/
│
├── shopping_cart.py
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/osaid400/Shopping-Cart-System.git
```

### 2. Navigate to the project folder

```bash
cd Shopping-Cart-System
```

### 3. Run the program

```bash
python shopping_cart.py
```

---

# Example Outputs

## Main Menu

```text
=============== Select the Option (0-7) ===============
1. View Products
2. Add to Cart
3. Remove from Cart
4. View Cart
5. Update Cart
6. Calculate Total
7. Checkout
0. Exit
```

---

## View Products

```text
==============================================================================================================
Product ID          Name                     Category               Price                        Stock
==============================================================================================================
101                 Keyboard                 Electronics            Rs. 2,500.0                  15
102                 Mouse                    Electronics            Rs. 1,200.0                  25
103                 Monitor                  Electronics            Rs. 28,500.0                 8
...
==============================================================================================================
```

---

## Add Product to Cart

```text
Enter the Product ID: 101
Enter the quantity: 2

Product added to cart successfully!
```

---

## View Cart

```text
------------------------------------------------------------ CART ITEMS ----------------------------------------------------------
==================================================================================================================================
Product ID          Name                     Category               Price                    Quantity            Total
==================================================================================================================================
101                 Keyboard                 Electronics            Rs. 2,500.0             2                   Rs. 5,000.0
==================================================================================================================================
Grand Total:                                                Rs. 5,000.0
----------------------------------------------------------------------------------------------------------------------------------
```

---

## Update Cart

```text
Enter the Product ID to update: 101
Enter the new quantity: 4

Cart Updated Successfully!
```

---

## Remove Product

```text
Enter the Product ID: 101
Are you sure you want to delete Product Keyboard? (y/n): y

Item Removed Successfully!
```

---

## Calculate Total

```text
----------------------------------------------------------------------------------------------------------------------------------
Grand Total:                                                Rs. 35,400.0
----------------------------------------------------------------------------------------------------------------------------------
```

---

## Checkout

```text
Enter customer name (leave blank for 'Guest'): Abdullah
Enter customer phone (optional): 03001234567
Proceed to checkout and generate bill for Abdullah? (y/n): y
```

```text
============================================================
                  SHOPPING CART - RECEIPT
============================================================
Customer: Abdullah
Phone   : 03001234567
Date and Time   : 2026-07-16 18:30:21
------------------------------------------------------------
ID     Name                  Qty     Subtotal
------------------------------------------------------------
101    Keyboard               2       Rs. 5,000.0
102    Mouse                  3       Rs. 3,600.0
------------------------------------------------------------
              Grand Total: Rs. 8,600.0
============================================================

Receipt printed!

Thank you for shopping with us!
```

---

## Exit

```text
Thank you for shopping with us!
Good Bye! Have a nice day!
Exiting the Shopping Cart System...
```

---

## Concepts Covered

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* JSON File Handling
* Reading and Writing Files
* Inventory Management
* Input Validation
* Exception Handling
* `datetime` Module
* Searching and Updating Records
* Receipt Generation

---

## Future Improvements

* Search products by name or category
* Product sorting and filtering
* Discount and coupon system
* User login system
* Sales history
* SQLite Database
* Object-Oriented Programming (OOP) version
* GUI using Tkinter or CustomTkinter

---

## Learning Outcomes

This project helped me practice:

* Building a complete menu-driven application
* Managing inventory using JSON
* Persisting shopping cart data
* Updating stock automatically
* Performing CRUD operations
* Working with nested dictionaries and lists
* Generating formatted receipts
* Improving problem-solving and debugging skills

---

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
