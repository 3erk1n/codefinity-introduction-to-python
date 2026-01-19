vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")

vegetables.sort()

print("Updated Vegetable Inventory:", vegetables)

if "carrots" in vegetables == 1:
    print("Carrots are already in the list.")
elif "cucumbers" in vegetables == 1:
    print("Cucumbers are already in the list.")

