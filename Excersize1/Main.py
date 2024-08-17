from restaurant import Restaurant

restaurant = Restaurant("The Python Eatery", "123 Coding Lane")
#Set Menu
restaurant.menu.add_item("Spaghetti Bolognese", 12)
restaurant.menu.add_item("Margherita Pizza", 8)
restaurant.menu.add_item("Caesar Salad", 6)
#Set Staff
restaurant.hire_staff("Alice", "Chef")
restaurant.hire_staff("Bob", "Waiter")
#Set reservation
restaurant.make_reservation("John Doe", 4, "7:00 PM")
#Set Order
items_to_order = ["Spaghetti Bolognese", "Caesar Salad"]
restaurant.take_order("John Doe", items_to_order)

print("Orders:")
print(restaurant.show_orders())

# Check a receipt
print("\nReceipt for Order ID 1:")
print(restaurant.check_receipt(1))
