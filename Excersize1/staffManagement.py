class StaffManagement:
    def __init__(self):
        self.persons = []

    def hire(self, name, location):
        self.persons.append({"name": name, "location": location})
        return f"{name} hired as {location}"

    def show_all_staff(self):
        staff = ""
        for member in self.persons:
            staff += f"{member['name']} _ {member['location']}\n"
        return staff

    def output(self, name, location):
        self.persons.remove({"name": name, "location": location})
