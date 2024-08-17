from restaurant import Restaurant
restaurant = Restaurant("The Python Eatery", "123 Coding Lane")

# Add menu items
restaurant.menu.add_item("Spaghetti Bolognese", 12)
restaurant.menu.add_item("Margherita Pizza", 8)
restaurant.menu.add_item("Caesar Salad", 6)

# Hire staff
restaurant.hire_staff("Alice", "Chef")
restaurant.hire_staff("Bob", "Waiter")

# Make a reservation
restaurant.make_reservation("John Doe", 4, "7:00 PM")

# Place an order
items_to_order = ["Spaghetti Bolognese", "Caesar Salad"]
restaurant.take_order("John Doe", items_to_order)

# Show all orders
print("Orders:")
print(restaurant.show_orders())

# Check a receipt
print("\nReceipt for Order ID 1:")
print(restaurant.check_receipt(1))
restaurant = Restaurant(input('please enter your restaurant name'), input('please input your restaurant address'))
restaurant.menu.add_item(input('please enter your order'), int(input('please input your restaurant address')))