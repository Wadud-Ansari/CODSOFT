class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        return [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]

    def update_contact(self, index, updated_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = updated_contact
        else:
            print("Invalid index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
        else:
            print("Invalid index.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            contact_book.view_contacts()
            input("Press Enter to continue...")

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ").strip()
            results = contact_book.search_contact(search_term)
            if results:
                for contact in results:
                    print(contact)
            else:
                print("No contacts found.")
            input("Press Enter to continue...")

        elif choice == '4':
            contact_book.view_contacts()
            try:
                index = int(input("Enter the index of the contact to update: ").strip()) - 1
                name = input("Enter new name: ").strip()
                phone = input("Enter new phone number: ").strip()
                email = input("Enter new email: ").strip()
                address = input("Enter new address: ").strip()
                updated_contact = Contact(name, phone, email, address)
                contact_book.update_contact(index, updated_contact)
                print("Contact updated successfully!")
            except ValueError:
                print("Invalid input. Please enter numeric values for the index.")
            input("Press Enter to continue...")

        elif choice == '5':
            contact_book.view_contacts()
            try:
                index = int(input("Enter the index of the contact to delete: ").strip()) - 1
                contact_book.delete_contact(index)
                print("Contact deleted successfully!")
            except ValueError:
                print("Invalid input. Please enter numeric values for the index.")
            input("Press Enter to continue...")

        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
