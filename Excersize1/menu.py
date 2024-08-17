class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def display_menu(self):
        menu = ""
        for item in self.items:
            menu += f"{item['name']} - ${item['price']:.2f}\n"
        return menu

    def get_item(self, name):
        for item in self.items:
            if item['name'].lower() == name.lower():
                return item
        return None



