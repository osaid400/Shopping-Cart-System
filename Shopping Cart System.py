# SHOPPING CART SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python


import sys
import os
import json
from datetime import datetime

print ("============ Welcome to Shopping Cart System =============")


class Product:

    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "Product ID": self.product_id,
            "Name": self.name,
            "Category": self.category,
            "Price": self.price,
            "Stock": self.stock
        }

    def from_dict(cls, data):
        return cls(
            product_id=data["Product ID"],
            name=data["Name"],
            category=data["Category"],
            price=data["Price"],
            stock=data["Stock"]
        )


class CartItem:

    def __init__(self, product, Quantity):
        self.product = product
        self.Quantity = Quantity

    def subtotal(self):
        return self.product.price * self.Quantity


class Shopping_Cart_Manager:

    def __init__(self, filename = "products.json" , cart_file = "cart.json" ,products=None, cart=None):
        self.products_file = filename
        self.cart_file = cart_file
        self.products = products if products is not None else []
        self.cart = cart if cart is not None else []

    def load_products(self):
        if os.path.exists(self.products_file):
            with open(self.products_file, "r") as file:
                data = json.load(file)
            return data

    def load_cart(self):
        if os.path.exists(self.cart_file):
            with open(self.cart_file, "r") as file:
                data = json.load(file)
            return data

    def save_cart(self):
        with open(self.cart_file, "w") as file:
            json.dump(self.cart, file, indent=5)

    def save_products(self):
        with open(self.products_file, "w") as file:
            json.dump(self.products, file, indent=5)
    
    def print_product(self, product):
        print(f"{product['Product ID']:<17} {product['Name']:<25} {product['Category']:<25} {self.format_currency(product['Price']):<30} {product['Stock']:<5}")

    def print_cart(self, cart_item):
        print(f"{cart_item['Product ID']:<17} {cart_item['Name']:<25} {cart_item['Category']:<25} {self.format_currency(cart_item['Price']):<30} {cart_item['Quantity']:<10} {self.format_currency(cart_item['Total']):<10}")

    def format_currency(self, Price):
        return f"Rs. {Price:,}"


# -------------- OLD DATA ---------------------

def view_products():
    if not products:
        print("No Products in stocks!")
        return
    print("="*110)
    print("{:<20} {:<24} {:<23} {:<28} {:<5}".format("Product ID", "Name", "Category", "Price", "Stock"))
    print("="*110)
    for product in products:
        print_product(product)
    print("="*110)

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
            save_products()
            save_cart()
            print("Product added to cart successfully!")
            return

    cart.append(cart_item)
    save_products()
    save_cart()
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
                    save_cart()
                    save_products()
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
    print("------------------------------------------------------------ CART ITEMS ----------------------------------------------------------")
    print("="*130)
    print("{:<20} {:<24} {:<23} {:<24} {:<20} {:<15}".format("Product ID", "Name", "Category", "Price", "Quantity", "Total"))
    print("="*130)
    for cart_items in cart:
        subtotal = cart_items["Price"] * cart_items["Quantity"]
        print(f"{cart_items['Product ID']:<17} {cart_items['Name']:<25} {cart_items['Category']:<22} {format_currency(cart_items['Price']):<30} {cart_items['Quantity']:<15} {format_currency(subtotal):<10}")
    print("="*130)
    calculate_total()

def update_cart():
    if not cart:
        print("Cart is Empty! Nothing to update.")
        return

    view_cart()
    try:
        search = int(input("Enter the Product ID to update: "))
    except ValueError:
        print("Invalid Product ID! Please enter a number.")
        return

    cart_item = next((c for c in cart if c["Product ID"] == search), None)
    if cart_item is None:
        print("Product not found in cart!")
        return

    try:
        new_quantity = int(input("Enter the new quantity: "))
    except ValueError:
        print("Invalid quantity! Please enter a number.")
        return

    if new_quantity <= 0:
        print("Quantity must be a positive number!")
        return

    product = next((p for p in products if p["Product ID"] == search), None)
    if product is None:
        print("Product not found in inventory!")
        return

    # Restore the old quantity back to stock before checking availability
    available_stock = product["Stock"] + cart_item["Quantity"]
    if new_quantity > available_stock:
        print("Not enough stock available!")
        return

    product["Stock"] = available_stock - new_quantity
    cart_item["Quantity"] = new_quantity
    save_products()
    save_cart()
    print("Cart Updated Successfully!")

def calculate_total():
    grand_total = sum(item["Price"] * item["Quantity"] for item in cart)
    print("-"*130)
    print(f"Grand Total: {format_currency(grand_total):>60}")
    print("-"*130)
    return grand_total

def checkout():
    if not cart:
        print("Cart is Empty! Cannot proceed to checkout.")
        return

    view_cart()
    grand_total = calculate_total()

    name = input("Enter customer name (leave blank for 'Guest'): ").strip() or "Guest"
    phone = input("Enter customer phone (optional): ").strip()

    confirm = input(f"Proceed to checkout and generate bill for {name}? (y/n): ")
    if confirm.lower() != 'y':
        print("Checkout cancelled.")
        return

    lines = []
    lines.append("="*60)
    lines.append("{:^60}".format("SHOPPING CART - RECEIPT"))
    lines.append("="*60)
    lines.append(f"Customer: {name}")
    if phone:
        lines.append(f"Phone   : {phone}")
    lines.append(f"Date and Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-"*60)
    lines.append("{:<6} {:<20} {:>7} {:>12}".format("ID","Name","Qty","Subtotal"))
    lines.append("-"*60)

    for item in cart:
        subtotal = item["Price"] * item["Quantity"]
        lines.append("{:<6} {:<20} {:>6} {:>12}".format(item["Product ID"], item["Name"][:25], item["Quantity"], format_currency(subtotal)))

    lines.append("-"*60)
    lines.append(f"{'Grand Total:':>26} {format_currency(grand_total)}")
    lines.append("="*60)

    bill_text = "\n".join(lines)

    print(f"\n{bill_text}\n")
    print("Receipt printed!.")

    cart.clear()
    save_cart()
    save_products()
    print("Thank you for shopping with us!")

def exit_system():
    print("Thank you for shopping with us!")
    print("Good Bye! Have a nice day!")
    print("Exiting the Shopping Cart System...")
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
