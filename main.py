class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = []


class Supplier(Contact):
    all_orders = {}

    def order(self, string):
        Supplier.all_orders[self.name] = string


class ContactList(list):
    def search(self, string):
        return_list = []
        for contact in self:
            if string in contact.name:
                return_list.append(contact)
        return return_list