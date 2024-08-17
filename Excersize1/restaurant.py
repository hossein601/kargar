from orderManagement import OrderManagement
from menu import Menu
from reservationManagement import ReservationManagement
from staffManagement import StaffManagement


class Restaurant:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.menu = Menu()
        self.staff = StaffManagement()
        self.reservations = ReservationManagement()
        self.order_management = OrderManagement()

    def __str__(self):
        return f"Restaurant Name: {self.name}, Address: {self.address}"

    def show_menu(self):
        return self.menu.display_menu()

    def hire_staff(self, name, position):
        return self.staff.hire(name, position)

    def make_reservation(self, customer_name, number_of_people, time):
        return self.reservations.book(customer_name, number_of_people, time)

    def show_reservations(self):
        return self.reservations.show_all_reservations()

    def show_staff(self):
        return self.staff.show_all_staff()

    def take_order(self, customer_name, items):
        return self.order_management.place_order(customer_name, items, self.menu)

    def show_orders(self):
        return self.order_management.show_all_orders()

    def check_receipt(self, order_id):
        return self.order_management.generate_receipt(order_id)

