from src.models.address_book import AddressBook
from src.services.console_text_designer import ConsoleTextDesigner
from src.services.validator import validate_user_name, validate_phone_number


class App:
    def __init__(self):
        # TODO init properties ???
        pass

    def run(self):
        book = AddressBook()  # TODO create separate method for load_data()
        console_text_designer = ConsoleTextDesigner()

        console_text_designer.print_info("Welcome to the assistant bot!")

        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            output = ''

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                person = fill_new()
                print("Need to do.")
            # elif command == "change":
            #     print("Need to do.")
            # elif command == "phone":
            #     print("Need to do.")
            # elif command == "all":
            #     print("Need to do.")
            # elif command == "add-birthday":
            #     print("Need to do.")
            # elif command == "show-birthday":
            #     print("Need to do.")
            # elif command == "birthdays":
            #     print("Need to do.")
            else:
                print("Invalid command.")

            print(output)

        # TODO: save_data(book)


def fill_new():
    properties = ["name", "phone_number"]

    name = None
    phone_number = None

    while True:
        if len(properties) == 0:
            break

        prop = properties[0]

        if prop == "name":
            input_name = input("print name: ")
            if not validate_user_name(input_name):  # is not valid
                print("name is not valid")
                continue
            name = input_name

        if prop == "phone_number":
            input_phone = input("print phone: ")
            if not validate_phone_number(input_phone):
                print("phone is not valid")
                continue
            phone_number = input_phone

        properties.pop(0)

    print('__________')
    print(name, phone_number)
    print('__________')




def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
