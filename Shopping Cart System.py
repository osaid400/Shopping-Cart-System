# SHOPPING CART SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

import sys

print ("============ Welcome to Shopping Cart System =============")

# ---------------- Shopping Cart System ----------------
products = [
    {"Product ID": 101, "Name": "Keyboard", "Category": "Electronics", "Price": 2500.0, "Stock": 15},
    {"Product ID": 102, "Name": "Mouse", "Category": "Electronics", "Price": 1200.0, "Stock": 25},
    {"Product ID": 103, "Name": "Monitor", "Category": "Electronics", "Price": 28500.0, "Stock": 8},
    {"Product ID": 104, "Name": "Laptop", "Category": "Electronics", "Price": 125000.0, "Stock": 5},
    {"Product ID": 105, "Name": "USB Flash Drive", "Category": "Accessories", "Price": 1800.0, "Stock": 30},
    {"Product ID": 106, "Name": "External Hard Drive", "Category": "Storage", "Price": 14500.0, "Stock": 10},
    {"Product ID": 107, "Name": "Printer", "Category": "Office", "Price": 22000.0, "Stock": 6},
    {"Product ID": 108, "Name": "Notebook", "Category": "Stationery", "Price": 350.0, "Stock": 100},
    {"Product ID": 109, "Name": "Pen", "Category": "Stationery", "Price": 50.0, "Stock": 250},
    {"Product ID": 110, "Name": "Office Chair", "Category": "Furniture", "Price": 18500.0, "Stock": 7},
    {"Product ID": 111, "Name": "Desk", "Category": "Furniture", "Price": 32000.0, "Stock": 4},
    {"Product ID": 112, "Name": "Headphones", "Category": "Electronics", "Price": 6500.0, "Stock": 18},
    {"Product ID": 113, "Name": "Webcam", "Category": "Electronics", "Price": 5400.0, "Stock": 12},
    {"Product ID": 114, "Name": "Microphone", "Category": "Electronics", "Price": 8900.0, "Stock": 9},
    {"Product ID": 115, "Name": "Router", "Category": "Networking", "Price": 7600.0, "Stock": 11},
    {"Product ID": 116, "Name": "Power Bank", "Category": "Accessories", "Price": 4200.0, "Stock": 20},
    {"Product ID": 117, "Name": "Smartphone", "Category": "Electronics", "Price": 78000.0, "Stock": 9},
    {"Product ID": 118, "Name": "Tablet", "Category": "Electronics", "Price": 56000.0, "Stock": 7},
    {"Product ID": 119, "Name": "Calculator", "Category": "Office", "Price": 1800.0, "Stock": 22},
    {"Product ID": 120, "Name": "Projector", "Category": "Office", "Price": 47000.0, "Stock": 3},
    {"Product ID": 121, "Name": "Ethernet Cable", "Category": "Networking", "Price": 650.0, "Stock": 50},
    {"Product ID": 122, "Name": "HDMI Cable", "Category": "Accessories", "Price": 900.0, "Stock": 40},
    {"Product ID": 123, "Name": "SSD 512GB", "Category": "Storage", "Price": 9800.0, "Stock": 14},
    {"Product ID": 124, "Name": "Gaming Mouse", "Category": "Electronics", "Price": 4200.0, "Stock": 16},
    {"Product ID": 125, "Name": "Mechanical Keyboard", "Category": "Electronics", "Price": 8500.0, "Stock": 10}
]

cart = []

def view_products():
    if len(products) == 0:
        print("No Products in stocks!")
        return
    for product in products:
            print("---------------------------------------------------")
            print("Name:", product["Name"])
            print("Category:", product["Category"])
            print("Product ID:", product["Product ID"])
            print("Price:", product["Price"])
            print("Stock:", product["Stock"])
            print("---------------------------------------------------")

def add_to_cart():
    try:
        product_id = int(input("Enter the Product ID: "))
    except ValueError:
        print("Invalid Product ID! Please enter a number.")
        return
    if product_id <= 0:
        print("Enter a valid Product ID!")
        return
    
    product = next((p for p in products if p["Product ID"] == product_id), None)
    if product is None:
        print("Product not found!")
        return
    Name = product["Name"]
    Category = product["Category"]
    Price = product["Price"]
    
    try:
        Quantity = int(input("Enter the quantity: "))
        if Quantity <= 0:
            print("Quantity must be a positive number!")
            return
    except ValueError:
        print("Invalid quantity! Please enter a number.")
        return

    cart_item = {
        "Product ID": product_id,
        "Name": Name,
        "Category": Category,
        "Price": Price,
        "Quantity": Quantity,
    }

    for product in products:
        if product["Product ID"] == product_id:
            if product["Stock"] < Quantity:
                print("Not enough stock available!")
                return
            product["Stock"] -= Quantity
            break

    for item in cart:
        if item["Product ID"] == product_id:
            item["Quantity"] += Quantity
            print("Product added to cart successfully!")
            return

    cart.append(cart_item)
    print("Product added to cart successfully!")

def remove_from_cart(): 
    try:
        search = int(input("Enter the Product ID: "))
    except ValueError:
        print("Invalid Product ID! Please enter a number.")
        return
    found = False
    for cart_items in cart:
        if cart_items["Product ID"] == search:
            confirm = input(f"Are you sure you want to delete Product {cart_items['Name']}? (y/n): ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                return
            cart.remove(cart_items)
            for product in products:
                if product["Product ID"] == search:
                    product["Stock"] += cart_items["Quantity"]
                    break

            print("Item Removed Successfully!")
            found = True
            break
    if not found:
        print("Item Not Found!")
    
def view_cart():
    if not cart:
        print("Cart is Empty!")
        return
    found = False
    for cart_items in cart:
        subtotal = cart_items["Price"] * cart_items["Quantity"]
        print("---------------------------------------------------")
        print("Name:", cart_items["Name"])
        print("Category:", cart_items["Category"])
        print("Product ID:", cart_items["Product ID"])
        print("Price:", cart_items["Price"])
        print("Quantity:", cart_items["Quantity"])
        print("Total:", subtotal)
        print("---------------------------------------------------")
        found = True
    if not found:
        print("Cart is Empty!")

def update_cart():
    try:
        search = int(input("Enter the Product ID: "))
    except ValueError:
        print("Invalid Product ID! Please enter a number.")
        return
    found = False
    for cart_item in cart:
        if cart_item["Product ID"] == search:
            print("---------------------------------------------------")
            print("Name:", cart_item["Name"])
            print("Category:", cart_item["Category"])
            print("Product ID:", cart_item["Product ID"])
            print("Price:", cart_item["Price"])
            print("Current Quantity:", cart_item["Quantity"])
            print("---------------------------------------------------")
            try:
                new_quantity = int(input("Enter the new quantity: "))
            except ValueError:
                print("Invalid quantity!")
                return
            if new_quantity <= 0:
                print("Quantity must be greater than 0!")
                return
            old_quantity = cart_item["Quantity"]
            for product in products:
                if product["Product ID"] == search:
                    product["Stock"] += old_quantity
                    if new_quantity > product["Stock"]:
                        print("Not enough stock available!")
                        product["Stock"] -= old_quantity
                        return
                    product["Stock"] -= new_quantity
                    cart_item["Quantity"] = new_quantity
                    print("Cart Updated Successfully!")
                    found = True
                    break
            break
    if not found:
        print("Product Not Found!")

def calculate_total():
    grand_total = sum(item["Price"] * item["Quantity"] for item in cart)
    print("---------------------------------------------------")
    print(f"Grand Total: {grand_total}")
    print("---------------------------------------------------")
    return grand_total

def checkout():
    if not cart:
        print("Cart is Empty! Cannot proceed to checkout.")
        return

    cart_total = calculate_total()
    print(f"Your total amount is: {cart_total}")
    print("Proceeding to checkout...")
    cart.clear()
    print("Thank you for shopping with us!")

def exit_system():
    print("Thank you for shopping with us!")
    print("Good Bye! Have a nice day!")
    print("Exiting the Shopping Cart System...")
    import sys
    sys.exit()

while True:
    print()
    print("=============== Select the Option (0-7) ===============")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Update Cart")
    print("6. Calculate Total")
    print("7. Checkout")
    print("0. Exit")

    try:
        choice = int(input("Enter the number: "))
    except ValueError:
        print("Invalid Choice! Please enter a number.")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
    
    if choice == 1:
        view_products()
    elif choice == 2:
        add_to_cart()
    elif choice == 3:
        remove_from_cart()
    elif choice == 4:
        view_cart()
    elif choice == 5:
        update_cart()
    elif choice == 6:
        calculate_total()
    elif choice == 7:
        checkout()
    elif choice == 0:
        exit_system()
        break
    else:
        print("Invalid choice! Please try again.")
