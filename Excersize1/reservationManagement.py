class ReservationManagement:
    def __init__(self):
        self.reservations = []

    def book(self, customer_name, number_of_people, time):
        self.reservations.append({
            "customer_name": customer_name,
            "number_of_people": number_of_people,
            "time": time
        })
        return f"Reservation made for {customer_name} at {time} for {number_of_people} people"

    def show_all_reservations(self):
        reservations = ""
        for reservation in self.reservations:
            reservations += (f"Customer: {reservation['customer_name']}, "
                             f"People: {reservation['number_of_people']}, "
                             f"Time: {reservation['time']}\n")
        return reservations
