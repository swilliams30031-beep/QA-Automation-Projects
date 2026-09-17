contacts = {}

def add_contact(name, phone):
    contacts[name.strip().title()] = phone.strip()
    print(f"SUCCESS: Saved {name.strip().title()}.")

def find_contact(name):
        formatted_name = name.strip().title()
        if formatted_name in contacts:
             print(f"FOUND: {formatted_name} - {contacts[formatted_name]}")
        else:
            print(f"ERROR: No contact found for '{formatted_name}'.")



def show_all():
    if not contacts:
        print("INFO: Contact book is empty.")
    else:
        print("\n---CONTACT LIST ---")
        for name, phone in contacts.items():
             print(f". {name}: {phone}")
        print("---------------------")

# Application Loop
while True:
    print("\n[1] Add Contact [2] Find Contact [3] View All [4] Exit")
    choice = input("Select an option (1-4): ").strip()

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)    
    elif choice == "2":
        name = input("Enter name to search: ")
        find_contact(name)
    elif choice == "3":
        show_all()
    elif choice == "4":
        print("Exiting application. Goodbye!")
        break
    else:
        print("INVALID: pLEASE ENTER 1, 2, 3, OR 4.")
    





     
    

    
                   