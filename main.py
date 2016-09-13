
class Contact:

    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contact(cls):
        cls.all_contacts = []


class Supplier(Contact):
    all_orders = {}

    def order(self, string):
        Supplier.all_orders[self.name] = string


class ContactList(Contact):
    @classmethod
    def search(cls):
        pass


