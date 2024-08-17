class OrderManagement:
    def __init__(self):
        self.orders = []
        self.counter_id = 1

    def place_order(self, customer_name, items, menu):
        order_items = []
        total_price = 0.0

        for item_name in items:
            menu_item = menu.get_item(item_name)
            if menu_item:
                order_items.append(menu_item)
                total_price += menu_item['price']

        order = {
            "order_id": self.counter_id,
            "customer_name": customer_name,
            "items": order_items,
            "total_price": total_price
        }
        self.orders.append(order)
        self.counter_id += 1

        return f"Order placed for {customer_name}. Order ID: {order['order_id']}"

    def show_all_orders(self):
        orders = ""
        for order in self.orders:
            orders += f"Order ID: {order['order_id']}, Customer: {order['customer_name']}, Total: ${order['total_price']:.2f}\n"
        return orders

    def generate_receipt(self, order_id):
        for order in self.orders:
            if order['order_id'] == order_id:
                receipt = f"Receipt for Order ID: {order_id}\n"
                receipt += f"Customer: {order['customer_name']}\n"
                receipt += "Items:\n"
                for item in order['items']:
                    receipt += f"{item['name']} - ${item['price']:.2f}\n"
                receipt += f"Total: ${order['total_price']:.2f}\n"
                return receipt
        return "Order not found."
