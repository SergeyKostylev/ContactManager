from src.models.address_book import AddressBook
from src.services.console_models_filler import fill_new_book_record
from src.services.pretty_output import ConsoleTextDesigner


class App:
    def __init__(self):
        self.__designer = ConsoleTextDesigner()
        pass

    def run(self):
        book = AddressBook()  # TODO create separate method for load_data()
        self.__designer.print_info("Welcome to the assistant bot!")


        while True:
            user_input = self.__designer.print_info("Enter a command: ")
            command, *args = parse_input(user_input)
            output = ''

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                self.__designer.print_info("How can I help you?")

            elif command == "add":
                person = fill_new_book_record()

                print("Need to do.")
            elif command == "change_phone":
                print("Need to do.")
            elif command == "add_phone":
                print("Need to do.")
            elif command == "delete_phone":
                print("Need to do.")
            elif command == "show_all":
                print("Need to do.")
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

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
