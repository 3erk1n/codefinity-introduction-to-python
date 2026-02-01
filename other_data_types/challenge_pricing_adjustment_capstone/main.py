grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

eggs_price = grocery_inventory["Eggs"][1]

if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    new_price = eggs_price - 1
    grocery_inventory["Eggs"] = (
    grocery_inventory["Eggs"][0],
    new_price,
    grocery_inventory["Eggs"][2]
    )
else:
    print("The price of Eggs is reasonable")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

check_stock = grocery_inventory["Milk"][2]

if check_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    new_stock = check_stock + 12
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        new_stock,
        grocery_inventory["Milk"][2]
    )
else: 
    print("Milk has sufficient stock.")

check_apple = grocery_inventory["Apples"][1]

if check_apple > 2: 
    print("Apples removed from inventory due to high price")

print("Updated inventory:", grocery_inventory)

      