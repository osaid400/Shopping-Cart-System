# ==========================================
# SHOPPING CART SYSTEM
# Simple Customer Access & Admin Auth
# Language: Python 3
# ==========================================

import os
import sys
import json
from datetime import datetime


class Product:
    def __init__(self, product_id: int, name: str, category: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self) -> dict:
        return {
            "Product ID": self.product_id,
            "Name": self.name,
            "Category": self.category,
            "Price": self.price,
            "Stock": self.stock
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            product_id=data["Product ID"],
            name=data["Name"],
            category=data["Category"],
            price=data["Price"],
            stock=data["Stock"]
        )


class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def subtotal(self) -> float:
        return self.product.price * self.quantity

    def to_dict(self) -> dict:
        return {
            "Product ID": self.product.product_id,
            "Quantity": self.quantity
        }


class User:

    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            username=data["username"],
            password=data["password"],
            role=data["role"]
        )


class ShoppingCartManager:
    def __init__(self, products_file="products.json", cart_file="cart.json", users_file="users.json"):
        self.products_file = products_file
        self.cart_file = cart_file
        self.users_file = users_file

        self.products: list[Product] = []
        self.cart: list[CartItem] = []
        self.users: list[User] = []

        self.load_products()
        self.load_users()
        self.load_cart()

    def load_products(self):
        if os.path.exists(self.products_file):
            try:
                with open(self.products_file, "r") as file:
                    data = json.load(file)
                    self.products = [Product.from_dict(item) for item in data]
            except json.JSONDecodeError:
                self.products = []

    def load_cart(self):
        if os.path.exists(self.cart_file):
            try:
                with open(self.cart_file, "r") as file:
                    data = json.load(file)
                    self.cart = []
                    for item in data:
                        product = self.find_product_by_id(item["Product ID"])
                        if product:
                            self.cart.append(CartItem(product, item["Quantity"]))
            except json.JSONDecodeError:
                self.cart = []

    def load_users(self):
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, "r") as file:
                    data = json.load(file)
                    self.users = [User.from_dict(item) for item in data]
            except json.JSONDecodeError:
                self.users = []

        if not self.users:
            self.users = [User("admin", "123", "admin")]
            self.save_users()

    def save_products(self):
        with open(self.products_file, "w") as file:
            json.dump([p.to_dict() for p in self.products], file, indent=4)

    def save_cart(self):
        with open(self.cart_file, "w") as file:
            json.dump([c.to_dict() for c in self.cart], file, indent=4)

    def save_users(self):
        with open(self.users_file, "w") as file:
            json.dump([u.to_dict() for u in self.users], file, indent=4)

    @staticmethod
    def format_currency(price: float) -> str:
        return f"Rs. {price:,.2f}"

    def find_product_by_id(self, product_id: int) -> Product | None:
        return next((p for p in self.products if p.product_id == product_id), None)

    def find_cart_item_by_id(self, product_id: int) -> CartItem | None:
        return next((item for item in self.cart if item.product.product_id == product_id), None)

    def view_products(self):
        if not self.products:
            print("\n[!] No Products in inventory!")
            return

        print("\n" + "=" * 110)
        print(f"{'Product ID':<15} {'Name':<25} {'Category':<20} {'Price':<25} {'Stock':<10}")
        print("=" * 110)
        for p in self.products:
            print(f"{p.product_id:<15} {p.name:<25} {p.category:<20} {self.format_currency(p.price):<25} {p.stock:<10}")
        print("=" * 110)

    def add_to_cart(self):
        try:
            product_id = int(input("\nEnter Product ID: "))
        except ValueError:
            print("[!] Invalid Product ID format!")
            return

        product = self.find_product_by_id(product_id)
        if not product:
            print("[!] Product not found!")
            return

        try:
            quantity = int(input(f"Enter quantity for '{product.name}': "))
            if quantity <= 0:
                print("[!] Quantity must be greater than 0.")
                return
        except ValueError:
            print("[!] Invalid quantity input!")
            return

        if product.stock < quantity:
            print(f"[!] Stock shortfall! Only {product.stock} items available.")
            return

        product.stock -= quantity
        cart_item = self.find_cart_item_by_id(product_id)

        if cart_item:
            cart_item.quantity += quantity
        else:
            self.cart.append(CartItem(product, quantity))

        self.save_products()
        self.save_cart()
        print(f"[✓] Added {quantity}x '{product.name}' to cart successfully!")

    def remove_from_cart(self):
        if not self.cart:
            print("\n[!] Cart is empty!")
            return

        try:
            product_id = int(input("\nEnter Product ID to remove: "))
        except ValueError:
            print("[!] Invalid Product ID!")
            return

        cart_item = self.find_cart_item_by_id(product_id)
        if not cart_item:
            print("[!] Item not found in cart!")
            return

        confirm = input(f"Remove '{cart_item.product.name}' from cart? (y/n): ")
        if confirm.lower() == 'y':
            cart_item.product.stock += cart_item.quantity
            self.cart.remove(cart_item)
            self.save_cart()
            self.save_products()
            print("[✓] Item removed successfully!")
        else:
            print("[*] Removal cancelled.")

    def view_cart(self):
        if not self.cart:
            print("\n" + "=" * 30)
            print("         Cart is Empty!        ")
            print("=" * 30)
            return

        print("\n" + "-" * 55 + " CART OVERVIEW " + "-" * 55)
        print("=" * 120)
        print(f"{'Product ID':<15} {'Name':<25} {'Category':<20} {'Price':<20} {'Quantity':<15} {'Total':<15}")
        print("=" * 120)
        for item in self.cart:
            print(f"{item.product.product_id:<15} {item.product.name:<25} {item.product.category:<20} "
                  f"{self.format_currency(item.product.price):<20} {item.quantity:<15} {self.format_currency(item.subtotal()):<15}")
        print("=" * 120)
        self.calculate_total()

    def update_cart(self):
        if not self.cart:
            print("\n[!] Cart is Empty! Nothing to update.")
            return

        self.view_cart()
        try:
            product_id = int(input("\nEnter Product ID to update: "))
        except ValueError:
            print("[!] Invalid Product ID!")
            return

        cart_item = self.find_cart_item_by_id(product_id)
        if not cart_item:
            print("[!] Product not found in cart!")
            return

        try:
            new_quantity = int(input(f"Enter new quantity for '{cart_item.product.name}': "))
            if new_quantity <= 0:
                print("[!] Quantity must be positive. Use Remove option to delete item.")
                return
        except ValueError:
            print("[!] Invalid quantity!")
            return

        available_stock = cart_item.product.stock + cart_item.quantity
        if new_quantity > available_stock:
            print(f"[!] Stock shortfall! Maximum available is {available_stock}.")
            return

        cart_item.product.stock = available_stock - new_quantity
        cart_item.quantity = new_quantity

        self.save_products()
        self.save_cart()
        print("[✓] Cart updated successfully!")

    def calculate_total(self) -> float:
        grand_total = sum(item.subtotal() for item in self.cart)
        print("-" * 120)
        print(f"Grand Total: {self.format_currency(grand_total):>60}")
        print("-" * 120)
        return grand_total

    def checkout(self, customer_name="Guest"):
        if not self.cart:
            print("\n[!] Cannot checkout. Your cart is empty!")
            return

        self.view_cart()
        grand_total = sum(item.subtotal() for item in self.cart)

        phone = input("\nEnter customer phone number (optional): ").strip()
        confirm = input(f"Proceed to checkout for '{customer_name}'? (y/n): ")
        if confirm.lower() != 'y':
            print("[*] Checkout cancelled.")
            return

        lines = [
            "\n" + "=" * 60,
            f"{'SHOPPING CART - RECEIPT':^60}",
            "=" * 60,
            f"Customer : {customer_name}"
        ]
        if phone:
            lines.append(f"Phone    : {phone}")

        lines.extend([
            f"DateTime : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "-" * 60,
            f"{'ID':<6} {'Name':<22} {'Qty':>6} {'Subtotal':>22}",
            "-" * 60
        ])

        for item in self.cart:
            lines.append(f"{item.product.product_id:<6} {item.product.name[:20]:<22} {item.quantity:>6} {self.format_currency(item.subtotal()):>22}")

        lines.extend([
            "-" * 60,
            f"{'Grand Total:':>36} {self.format_currency(grand_total):>22}",
            "=" * 60
        ])

        print("\n".join(lines))
        print("\n[✓] Checkout complete! Receipt generated.")

        self.cart.clear()
        self.save_cart()
        self.save_products()
        print("Thank you for shopping with us!")

    def add_new_product(self):
        print("\n--- ADMIN: Add New Product ---")
        try:
            p_id = int(input("Enter Product ID: "))
            if self.find_product_by_id(p_id):
                print("[!] Product ID already exists!")
                return
            
            name = input("Enter Product Name: ").strip()
            category = input("Enter Category: ").strip()
            price = float(input("Enter Price: "))
            stock = int(input("Enter Initial Stock: "))

            if price <= 0 or stock < 0:
                print("[!] Price and Stock must be valid numbers!")
                return

            new_prod = Product(p_id, name, category, price, stock)
            self.products.append(new_prod)
            self.save_products()
            print(f"[✓] Product '{name}' added to inventory successfully!")
        except ValueError:
            print("[!] Invalid input format. Product creation failed.")

    def update_stock(self):
        print("\n--- ADMIN: Update Inventory Stock ---")
        try:
            p_id = int(input("Enter Product ID: "))
            product = self.find_product_by_id(p_id)
            if not product:
                print("[!] Product not found!")
                return

            print(f"Current Stock for '{product.name}': {product.stock}")
            add_qty = int(input("Enter quantity to add to stock: "))
            if add_qty <= 0:
                print("[!] Added quantity must be positive.")
                return

            product.stock += add_qty
            self.save_products()
            print(f"[✓] Stock updated! New stock for '{product.name}' is {product.stock}.")
        except ValueError:
            print("[!] Invalid number format.")

    def delete_product(self):
        print("\n--- ADMIN: Delete Product ---")
        try:
            p_id = int(input("Enter Product ID to delete: "))
            product = self.find_product_by_id(p_id)
            if not product:
                print("[!] Product not found!")
                return

            confirm = input(f"Are you sure you want to PERMANENTLY delete '{product.name}'? (y/n): ")
            if confirm.lower() == 'y':
                self.products.remove(product)
                self.save_products()
                print("[✓] Product deleted from inventory.")
            else:
                print("[*] Action cancelled.")
        except ValueError:
            print("[!] Invalid Product ID.")


def admin_menu(manager: ShoppingCartManager, admin_user: User):
    while True:
        print(f"\n================ ADMIN PANEL ========================")
        print("1. View Inventory Products")
        print("2. Add New Product to Inventory")
        print("3. Update Inventory Stock")
        print("4. Delete Product from Inventory")
        print("0. Logout")
        print("=========================================================")

        choice = input("Select option (0-4): ").strip()

        if choice == "1":
            manager.view_products()
        elif choice == "2":
            manager.add_new_product()
        elif choice == "3":
            manager.update_stock()
        elif choice == "4":
            manager.delete_product()
        elif choice == "0":
            print(f"\n[*] Admin '{admin_user.username}' logged out successfully.")
            break
        else:
            print("[!] Invalid option choice!")


def customer_menu(manager: ShoppingCartManager, customer_name: str):

    while True:
        print(f"\n=============== CUSTOMER STORE =====================")
        print("1. View Available Products")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart & Summary")
        print("5. Update Quantity in Cart")
        print("6. Calculate Total Price")
        print("7. Complete Checkout")
        print("0. Exit Store")
        print("========================================================")

        choice = input("Select option (0-7): ").strip()

        if choice == "1":
            manager.view_products()
        elif choice == "2":
            manager.add_to_cart()
        elif choice == "3":
            manager.remove_from_cart()
        elif choice == "4":
            manager.view_cart()
        elif choice == "5":
            manager.update_cart()
        elif choice == "6":
            manager.calculate_total()
        elif choice == "7":
            manager.checkout(customer_name=customer_name)
        elif choice == "0":
            print(f"\n[*] Customer '{customer_name}' exited from store.")
            break
        else:
            print("[!] Invalid option choice!")


def main():
    manager = ShoppingCartManager()

    while True:
        print("\n============ WELCOME TO SHOPPING CART SYSTEM =============")
        print("1. Continue as Customer")
        print("2. Login as Admin")
        print("0. Exit System")
        print("=============================================================")

        choice = input("Select option: ").strip()

        if choice == "1":
            name_input = input("\nEnter your name (Press Enter for 'Guest'): ").strip()
            customer_name = name_input.title() if name_input else "Guest"
            
            print(f"\n[✓] Welcome to the store, {customer_name}!")
            customer_menu(manager, customer_name)

        elif choice == "2":
            print("\n================== ADMIN LOGIN ==================")
            username = input("Enter Admin Username: ").strip().lower()
            password = input("Enter Admin Password: ").strip()
            print("==================================================")

            admin_user = next((u for u in manager.users if u.username == username and u.password == password and u.role == "admin"), None)

            if admin_user:
                print(f"\n[✓] Login successful! Welcome {admin_user.username.title()} (ADMIN)")
                admin_menu(manager, admin_user)
            else:
                print("[!] Invalid Admin Credentials!")

        elif choice == "0":
            print("\n============================================================")
            print("          Thank you for using Shopping Cart System!           ")
            print("                  Good Bye! Have a nice day!                  ")
            print("=============================================================")
            sys.exit()
        else:
            print("[!] Invalid Choice! Please enter 1, 2, or 0.")


if __name__ == "__main__":
    main()