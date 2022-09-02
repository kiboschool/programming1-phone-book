# Phonebook command-line application
def add_contact(phonebook, name, number):
    if name in phonebook:
        return f"{name} is already in phonebook"
    else:
        phonebook[name] = number
        return f"{name} added"

def find_contact(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    else:
        return f"{name} not found"

def update_contact(phonebook, name, number):
    if name in phonebook:
        phonebook[name] = number
        return f"{name} updated"
    else:
        return f"{name} not found"

def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        return f"{name} deleted"
    else:
        return f"{name} not found"
    
def list_contacts(phonebook):
    result = ""
    for name in phonebook:
        number = phonebook[name]
        result += f"{name}: {number}\n"
    return result

def run_interface():
    phonebook = {}
    while True:
        print('\nMenu')
        print('1. Add a contact')
        print('2. Search a contact')
        print('3. Change a contact')
        print('4. Delete a contact')
        print('5. List all contacts')
        print('6. Exit')
    
        choice = input('Enter your choice: ')
        if choice.isnumeric():
            choice = int(choice)

        if choice in [1,2,3,4]:
            name = input('Enter name: ')
    
        if choice == 1:
            number = input('Enter a phone number: ')
            print(add_contact(phonebook, name, number))
        elif choice == 2:
            print(find_contact(phonebook, name))
        elif choice == 3:
            number = input('Enter new phone number: ')
            print(update_contact(phonebook, name, number))
        elif choice == 4:
            print(delete_contact(phonebook, name))
        elif choice == 5:
            print(list_contacts(phonebook))
        elif choice == 6:
            print("Thank you!")
            exit()
        else:
            print("Unrecognized option.")

        input("Press Enter to continue.")

if __name__ == "__main__":
    run_interface()
