class ContactManager:
    def __init__(self):
        self.contacts = []

    def _validate_phone(self, phone):
        if not phone:
            return True
        if phone.startswith("+"):
            phone = phone[1:]
        allowed = set("0123456789-")
        return bool(phone) and all(char in allowed for char in phone)

    def _validate_email(self, email):
        if not email:
            return True
        return "@" in email and "." in email

    def _find_contact_index(self, name):
        for index, contact in enumerate(self.contacts):
            if contact["name"].lower() == name.lower():
                return index
        return None

    def _format_contact(self, contact, position=None):
        prefix = f"{position}. " if position is not None else ""
        return (
            f"{prefix}Name: {contact['name']} | Phone: {contact['phone']} | "
            f"Email: {contact['email']}"
        )

    def _print_contacts(self, contacts, title="Contacts"):
        print(f"\n=== {title} ===")
        if not contacts:
            print("No contacts found.")
            return
        for position, contact in enumerate(contacts, start=1):
            print(self._format_contact(contact, position))

    def add_contact(self, name, phone, email=""):
        if not self._validate_phone(phone):
            print("Error: Phone number can only contain digits and hyphens.")
            return False
        if not self._validate_email(email):
            print("Error: Email must contain both '@' and '.' if provided.")
            return False

        if self._find_contact_index(name) is not None:
            print("Error: A contact with that name already exists.")
            return False

        self.contacts.append({"name": name, "phone": phone, "email": email})
        print("Contact added successfully.")
        return True

    def view_contact(self, name):
        index = self._find_contact_index(name)
        if index is None:
            print("Contact not found.")
            return None
        contact = self.contacts[index]
        self._print_contacts([contact], title="Contact Details")
        return contact

    def update_contact(self, name, new_phone=None, new_email=None):
        index = self._find_contact_index(name)
        if index is None:
            print("Contact not found.")
            return False

        if new_phone is not None and not self._validate_phone(new_phone):
            print("Error: Phone number can only contain digits and hyphens.")
            return False
        if new_email is not None and not self._validate_email(new_email):
            print("Error: Email must contain both '@' and '.' if provided.")
            return False

        if new_phone is not None:
            self.contacts[index]["phone"] = new_phone
        if new_email is not None:
            self.contacts[index]["email"] = new_email

        print("Contact updated successfully.")
        return True

    def delete_contact(self, name):
        index = self._find_contact_index(name)
        if index is None:
            print("Contact not found.")
            return False

        deleted_contact = self.contacts.pop(index)
        print(f"Deleted contact: {deleted_contact['name']}")
        return True

    def Contactss(self, query):
        query = query.lower().strip()
        results = []
        for contact in self.contacts:
            if (
                query in contact["name"].lower()
                or query in contact["phone"].lower()
                or query in contact["email"].lower()
            ):
                results.append(contact)

        self._print_contacts(results, title=f"Search Results for '{query}'")
        return results

    def search_contacts(self, query):
        return self.Contactss(query)

    def list_all_contacts(self):
        self._print_contacts(self.contacts, title="All Contacts")
        return self.contacts


def prompt_required(prompt_text):
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("This field cannot be blank.")


def prompt_optional(prompt_text):
    value = input(prompt_text).strip()
    return value


def main():
    manager = ContactManager()

    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            name = prompt_required("Enter name: ")
            phone = prompt_required("Enter phone number: ")
            email = prompt_optional("Enter email (optional): ")
            manager.add_contact(name, phone, email)

        elif choice == "2":
            name = prompt_required("Enter the contact name to view: ")
            manager.view_contact(name)

        elif choice == "3":
            name = prompt_required("Enter the contact name to update: ")
            print("Leave a field blank to keep the current value.")
            new_phone = prompt_optional("Enter new phone number: ")
            new_email = prompt_optional("Enter new email: ")
            manager.update_contact(
                name,
                new_phone if new_phone else None,
                new_email if new_email else None,
            )

        elif choice == "4":
            name = prompt_required("Enter the contact name to delete: ")
            manager.delete_contact(name)

        elif choice == "5":
            query = prompt_required("Enter a name, phone number, or email to search: ")
            manager.search_contacts(query)

        elif choice == "6":
            manager.list_all_contacts()

        elif choice == "7":
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
