'''5. Shopping Cart
   - Create a program to simulate a shopping cart:
     - Add items (item name and price).
     - View cart items.
     - Calculate the total price.
     - Exit.
   - Use functions and a loop to allow multiple actions.
'''
def add_item(cart):
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    cart.append({"name": item_name, "price": item_price})
    print(f"'{item_name}' added to the cart.")

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item['name']} - {item['price']:.2f}")
        print()

def calculate_total(cart):
    total = sum(item["price"] for item in cart)
    print(f"Total price: {total:.2f}")

def shopping_cart():
    cart = []
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_item(cart)
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            calculate_total(cart)
        elif choice == "4":
            print("Exiting the shopping cart. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
shopping_cart()
