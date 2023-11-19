def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner

@input_error
def hello_handler():
    return 'How can I help you?'

@input_error
def add_handler(contact_info, contacts):
    name, phone_number = contact_info.split()
    contacts[name] = phone_number
    return f"Contact {name} added successfully"

@input_error
def change_handler(contact_info, contacts):
    name, phone_number = contact_info.split()
    if name in contacts:
        contacts[name] = phone_number
        return f"Phone number for {name} was changed!"
    else:
        raise KeyError("No user with this name")

@input_error
def phone_handler(name, contacts):
    if name in contacts:
        return f"Phone number for {name} is {contacts[name]}"
    else:
        raise KeyError("No user with this name")

@input_error
def show_all_handler(contacts):
    result = "Contacts: \n"
    for name, phone_number in contacts.items():
        result += f"{name}: {phone_number}\n"
    return result.strip()

def main():
    contacts = {}
    while True:
        command = input("Enter the command: ").lower()
        if command.startswith("hello"):
            print(hello_handler())
        elif command.startswith("add"):
            contacts_info = input("input name and phone number separated by space: ")
            print(add_handler(contacts_info, contacts))
        elif command.startswith("change"):
            contacts_info = input("Input name and new phone number separated by space: ")
            print(change_handler(contacts_info, contacts))
        elif command.startswith("phone"):
            name = input("Input name: ")
            print(phone_handler(name, contacts))
        elif command.startswith("show all"):
            print(show_all_handler(contacts))
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Not correct command. Please write again: ")

if __name__ == "__main__":
    main()
