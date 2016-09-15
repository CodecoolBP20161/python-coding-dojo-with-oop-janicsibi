class ContactList(list):
    def search(self, string):
        return_list = []
        for contact in self:
            if string in contact.name:
                return_list.append(contact)
        return return_list

    def longest_name(self):
        if len(self) == 0:
            return None
        longest = []
        for i in self:
            if len(i.name) >= len(longest):
                longest = i.name
        return longest






class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts.clear()


class Supplier(Contact):
    all_orders = {}

    def order(self, string):
        Supplier.all_orders[self.name] = string
        return self.all_orders


