contacts = []

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts recorded.")
        return
    else:
        for index, contact in enumerate(contacts):
            print("=" * 70)
            print(f"{index + 1}. Contact details: {contact['name']}")
            print("=" * 70)
            print(f" Phone: {contact['phone']} \n Email: {contact['email']}")
        print("=" * 70)

def delete_contact():
    view_contacts()
    if not contacts:
        return
    index = int(input("Enter the index of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"Deleted contact: {deleted_contact['name']}")
    else:
        print("Invalid index. Please try again.")

def main():
    print("Welcome to the Contact Book!")
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


