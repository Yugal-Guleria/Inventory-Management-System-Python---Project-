# Advanced Inventory Management System (Python CLI)

## Overview

This is a command-line based Inventory Management System built using Python.
It simulates a basic real-world shop system with multiple categories, item tracking, and stock management.

The project is structured using functions, nested dictionaries, and clear modular logic.

---

## Features

* View all inventory items category-wise
* Add new items with price and quantity
* Check item availability
* Update item quantity
* Low stock alert system
* Delete items from inventory
* Exit the system

---

## Concepts Used

* if-elif-else for decision making
* while loop for continuous execution
* functions for modular and reusable code
* nested dictionaries for structured data storage
* for loops for iteration
* f-strings for formatted output

---

## Data Structure

```python
inventory = {
    "category": {
        "item_name": {
            "price": int,
            "qty": int
        }
    }
}
```

Example:

```python
"Apple": {"price": 120, "qty": 25}
```

---
## Menu System

```
===== INVENTORY SYSTEM (ADVANCED) =====
1. View Items
2. Add Item
3. Check Item
4. Update Quantity
5. Low Stock Alert
6. Delete Item
7. Exit
```

---

## Functional Breakdown

View Items
Displays all categories with item name, price, and quantity

Add Item
Adds a new item with category, price, and quantity

Check Item
Checks if an item exists and shows its details

Update Quantity
Updates the stock quantity of an existing item

Low Stock Alert
Displays items with quantity less than 20

Delete Item
Removes an item from inventory

---

## Limitations

* Data is stored in memory and is not persistent
* No validation for invalid numeric inputs
* Command-line interface only

---

## Author

Beginner to intermediate level project focused on practical Python development.

---

## Output
<img width="285" height="794" alt="Screenshot 2026-04-07 181455" src="https://github.com/user-attachments/assets/bcc8afb9-cd84-406b-aad0-572de04a9f7e" />

