class PhoneBook:
    """
    Phone book class that allow you to create search and
    delete contacts
    """

    def __init__(self):
        #Dummy data
        self.contact_List = {
            "John Doe": 248789153,
            "David Jacobs":  789453783,
            "Nana Kofi": 2023586482,
            "Mo Salah": 268985367,
        }
    def searchContact(self, name):
        """
        search for contact using name
        """
        for i in self.contact_List:
            if name.lower() == i.lower():
                return f"The contact of {name.capitalize()} is 0{self.contact_List[i]}"
    def addContact(self, name, number):
        """
        add contact to dummy data list taking name and number
        """
        # check if name exist
        if self.searchContact(name):
            print("This contact already exists!")
        else:
            self.contact_List[name] = number
            return 1

    def displayContacts(self):
        """
        display all saved contacts
        """
        table_of_contact = ""
        for i in self.contact_List:
            table_of_contact += f"{i.capitalize()}   ->    0{self.contact_List[i]}\n"

        return table_of_contact