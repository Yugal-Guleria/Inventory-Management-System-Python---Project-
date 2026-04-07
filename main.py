# ADVANCED INVENTORY MANAGEMENT SYSTEM

#Created and data storage disc named inventory 

inventory = {
    "vegetables": {
        "Tomato": {"price": 20, "qty": 50},
        "Potato": {"price": 15, "qty": 80},
        "Onion": {"price": 18, "qty": 60},
        "Carrot": {"price": 25, "qty": 40},
        "Cabbage": {"price": 22, "qty": 35},
        "Spinach": {"price": 10, "qty": 30}
    },
    "fruits": {
        "Apple": {"price": 120, "qty": 25},
        "Banana": {"price": 40, "qty": 100},
        "Mango": {"price": 80, "qty": 45},
        "Orange": {"price": 60, "qty": 50},
        "Grapes": {"price": 90, "qty": 30}
    },
    "dairy": {
        "Milk": {"price": 60, "qty": 40},
        "Curd": {"price": 50, "qty": 20},
        "Butter": {"price": 120, "qty": 15},
        "Cheese": {"price": 200, "qty": 10}
    },
    "snacks": {
        "Chips": {"price": 20, "qty": 100},
        "Biscuits": {"price": 30, "qty": 80},
        "Chocolate": {"price": 50, "qty": 60},
        "Cookies": {"price": 70, "qty": 40}
    },
    "beverages": {
        "Tea": {"price": 10, "qty": 200},
        "Coffee": {"price": 15, "qty": 150},
        "Juice": {"price": 30, "qty": 90},
        "Cold Drink": {"price": 40, "qty": 70}
    }
}

# Creating input functions 

def get_category():
    return input("Enter category: ").lower()

def get_item():
    return input("Enter item name: ")

#Checking validations 

def is_valid_category(category):
    return category in inventory

#Creating functions to view item 

def view_items():
    for category in inventory:
        print(f"\n {category.upper()} ")
        for item, details in inventory[category].items():
            print(f"{item} | Price: {details['price']} | Qty: {details['qty']}")

#Creating fucntion to add item 
def add_item():
    category = get_category()
    item = get_item()
    price = int(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    if is_valid_category(category):
        inventory[category][item] = {"price": price, "qty": qty}
        print("Item added successfully")
    else:
        print("Invalid category")

#creating function to check item 
def check_item():
    category = get_category()
    item = get_item()

    if is_valid_category(category):
        if item in inventory[category]:
            details = inventory[category][item]
            print(f"Available | Price: {details['price']} | Qty: {details['qty']}")
        else:
            print("Out of stock")
    else:
        print("Invalid category")

#creating function to update quantity 
def update_quantity():
    category = get_category()
    item = get_item()

    if is_valid_category(category) and item in inventory[category]:
        qty = int(input("Enter new quantity: "))
        inventory[category][item]["qty"] = qty
        print("Quantity updated")
    else:
        print("Item not found")

#Creating function for Low stock warning 
def low_stock():
    print("\n LOW STOCK ITEMS (<20)")
    for category in inventory:
        for item, details in inventory[category].items():
            if details["qty"] < 20:
                print(f"{item} ({category}) → Qty: {details['qty']}")

#Creating function to delete item 
def delete_item():
    category = get_category()
    item = get_item()

    if is_valid_category(category) and item in inventory[category]:
        del inventory[category][item]
        print("Item deleted")
    else:
        print("Item not found")

#Creating loop for funtions 
while True:
    print("\n (:) INVENTORY SYSTEM (ADVANCED) (:)")
    print("1. View Items")
    print("2. Add Item")
    print("3. Check Item")
    print("4. Update Quantity")
    print("5. Low Stock Alert")
    print("6. Delete Item")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_items()
    elif choice == "2":
        add_item()
    elif choice == "3":
        check_item()
    elif choice == "4":
        update_quantity()
    elif choice == "5":
        low_stock()
    elif choice == "6":
        delete_item()
    elif choice == "7":
        print("Exiting system...")
        break
    else:
        print("Invalid choice")