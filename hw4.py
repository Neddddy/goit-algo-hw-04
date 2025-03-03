def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed"
    elif name not in contacts:
        return "Contact does not exist"

def show_number(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}\'s phone: {contacts[name]}"
    elif name not in contacts:
        return "Contact does not exist"

    pass
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "change":
            print(change_phone(args,contacts))
        elif command == "phone":
            print(show_number(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()