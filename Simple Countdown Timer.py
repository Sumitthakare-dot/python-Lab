def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Contact for {name} added!")

def view_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def contact_book():
    contacts = {}
    while True:
        print("\nOptions: 'add', 'view', 'quit'")
        choice = input("What would you like to do? ").lower()
        if choice == "add":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(contacts, name, phone)
        elif choice == "view":
            view_contacts(contacts)
        elif choice == "quit":
            break
        else:
            print("Invalid option.")

contact_book()
