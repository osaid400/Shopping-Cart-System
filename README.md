
# Shopping Cart System (Python)

A beginner-friendly console-based Shopping Cart System built with Python using **Object-Oriented Programming (OOP)**. This project demonstrates how to manage products, carts, inventory, admin access, sales logs, and receipts while storing data permanently using **JSON File Handling**.

## Features

* View available products
* Add products to cart
* Remove products from cart
* Update product quantity
* Calculate grand total
* Checkout with customer details
* Generate receipt
* Automatic stock management
* **Admin Login System** (Default: `admin` / `123`)
* **Add, Update, and Delete Products** (With product details confirmation before updating)
* **Sales Record & Revenue Tracking** for Admin
* Persistent data storage using JSON (`products.json`, `cart.json`, `users.json`, `sales.json`)
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
├── Shopping_Cart_System.py
├── .gitignore
├── products.json
└── README.md

```

## How to Run

### 1. Clone the repository

```bash
git clone [https://github.com/osaid400/Shopping-Cart-System.git](https://github.com/osaid400/Shopping-Cart-System.git)

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
============ WELCOME TO SHOPPING CART SYSTEM =============
1. Continue as Customer
2. Login as Admin
0. Exit System
==========================================================

```

---

## Customer Menu

```text
=============== CUSTOMER STORE (Abdullah) ===============
1. View Available Products
2. Add Item to Cart
3. Remove Item from Cart
4. View Cart & Summary
5. Update Quantity in Cart
6. Calculate Total Price
7. Complete Checkout
0. Exit Store
=========================================================

```

---

## View Products

```text
==============================================================================================================
Product ID          Name                      Category             Price                     Stock
==============================================================================================================
101                 Keyboard                  Electronics          Rs. 2,500.00              15
102                 Mouse                     Electronics          Rs. 1,200.00              25
103                 Monitor                   Electronics          Rs. 28,500.00             8
==============================================================================================================

```

---

## Add Product to Cart

```text
Enter Product ID: 101
Enter quantity for 'Keyboard': 2

[✓] Added 2x 'Keyboard' to cart successfully!

```

---

## View Cart

```text
------------------------------------------------------- CART OVERVIEW -------------------------------------------------------
=============================================================================================================================
Product ID          Name                      Category             Price                Quantity        Total
=============================================================================================================================
101                 Keyboard                  Electronics          Rs. 2,500.00             2         Rs. 5,000.00
=============================================================================================================================
-----------------------------------------------------------------------------------------------------------------------------
Grand Total:                                                                                    Rs. 5,000.00
-----------------------------------------------------------------------------------------------------------------------------

```

---

## Update Cart

```text
Enter Product ID to update: 101
Enter new quantity for 'Keyboard': 4

[✓] Cart updated successfully!

```

---

## Remove Product

```text
Enter Product ID to remove: 101
Remove 'Keyboard' from cart? (y/n): y

[✓] Item removed successfully!

```

---

## Calculate Total

```text
--------------------------------------------------------------
Grand Total:                              Rs. 35,400.00
---------------------------------------------------------------

```

---

## Checkout

```text
Enter customer phone number (optional): 03001234567
Proceed to checkout for 'Abdullah'? (y/n): y

```

```text
============================================================
                  SHOPPING CART - RECEIPT
============================================================
Customer : Abdullah
Phone    : 03001234567
DateTime : 2026-07-31 11:15:00
------------------------------------------------------------
ID     Name                   Qty               Subtotal
------------------------------------------------------------
101    Keyboard                 2           Rs. 5,000.00
102    Mouse                    3           Rs. 3,600.00
------------------------------------------------------------
                                Grand Total: Rs. 8,600.00
============================================================

[✓] Checkout complete! Receipt generated.

Thank you for shopping with us!

```

---

## Admin Menu

```text
================ ADMIN PANEL (ADMIN) ================
1. View Inventory Products
2. Add New Product to Inventory
3. Update Inventory Details (Price & Stock)
4. Delete Product from Inventory
5. View Sales Records & Revenue
0. Logout
=====================================================

```

---

## Admin: Update Inventory Details (With Confirmation)

```text
Enter Product ID: 101

==================================================
         CURRENT PRODUCT DETAILS         
==================================================
  Product ID    : 101
  Name          : Keyboard
  Category      : Electronics
  Price         : Rs. 2,500.00
  Current Stock : 15
==================================================

Do you want to update this product? (y/n): y
Enter new price (Press Enter to keep current price '2500.0'): 2700
Enter additional stock to add (Press Enter to keep current stock '15'): 5

[✓] Product 'Keyboard' details updated successfully!
    New Price: Rs. 2,700.00 | New Total Stock: 20

```

---

## Admin: Sales History & Revenue Report

```text
==========================================================================================
                                  SALES HISTORY & RECORD
==========================================================================================
Sale ID: #1  |  Date: 2026-07-31 11:15:00  |  Customer: Abdullah (Phone: 03001234567)
------------------------------------------------------------------------------------------
  ID     Product Name                   Qty            Price               Subtotal            
  101    Keyboard                        2          Rs. 2,500.00         Rs. 5,000.00        
  102    Mouse                           3          Rs. 1,200.00         Rs. 3,600.00        
  Total Sale Amount: Rs. 8,600.00
==========================================================================================

[★] OVERALL TOTAL REVENUE GENERATED: Rs. 8,600.00
==========================================================================================

```

---

## Exit

```text
==============================================
  Thank you for using Shopping Cart System! 
        Good Bye! Have a nice day!         
==============================================

```

---

## Concepts Covered

* Object-Oriented Programming (OOP - Classes & Methods)
* Role-based Logic (Customer vs Admin)
* Functions
* Lists and Dictionaries
* Loops
* Conditional Statements
* JSON File Handling
* Reading and Writing Files
* Inventory Management
* Input Validation
* Exception Handling
* `datetime` Module
* Searching and Updating Records
* Receipt Generation & Sales History Logging

---

## Future Improvements

* Product sorting and filtering
* Discount and coupon system
* SQLite Database Integration
* Password hashing for security
* GUI using Tkinter or CustomTkinter

---

## Learning Outcomes

This project helped me practice:

* Building a complete menu-driven application with OOP
* Managing inventory using persistent JSON files
* Implementing role-based access control (Admin vs Customer)
* Persisting shopping cart data and recording transaction histories
* Confirming existing details before updating product records
* Updating stock automatically upon checkout
* Performing CRUD operations
* Generating formatted receipts and sales reports
* Improving problem-solving and debugging skills

---

## Author:

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400

```