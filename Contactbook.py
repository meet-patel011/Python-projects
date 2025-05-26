def display_menu():
    print("Contact book")
    print("1. add contacts")
    print("2. delete contacts")
    print("3. show all contacts")
    print("4. Exit")

def add_contact(contacts):
    name = input("Enter the name:")
    phone = int(input("Enter contact no.: "))
    contacts[name] = phone
    print("Contact Added")

def del_contact(contacts):
    name = input("Enter the name:")
    if name in contacts:
        del name,contacts[name]
    print("Contact Deleted")        

def show_contacts(contacts):
    if not contacts:
        print("No contacts to show")
    else:
        print("Here are all the contacts")
        for name, contacts[name] in contacts.items():
            print(name, ":", contacts[name])

def contact_book():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option from 1-4: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            del_contact(contacts)    
        elif choice == "3":
            show_contacts(contacts)
        elif choice == "4":
            print("Exiting contact book")
            break

contact_book()        


