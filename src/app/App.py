from src.models.address_book import AddressBook
from src.services.console_models_filler import fill_new_book_record, EMPTY_FIELD_COMMAND, CANCEL_FILLING_COMMAND, \
    fill_phone_number, fill_user_name, fill_address, fill_email, fill_birthdate
from src.services.pretty_output import ConsoleTextDesigner
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

class App:
    def __init__(self):
        self.__designer = ConsoleTextDesigner()
        pass

    def run(self):
        book = AddressBook()
        book.load_data()
        commands = ["close","exit","hello","add","add_phone","change_phone","delete_phone",
                    "update_address","update_email","add_birthday","show_upcoming_birthday",
                    "all","show_by_name","show_by_part_name","birthdays"]
        command_completer = WordCompleter(commands)
        session = PromptSession(completer=command_completer)
        style = Style.from_dict({'prompt': 'ansiblue'})
        self.__designer.print_info("Welcome to the assistant bot!")

        while True:
            command = session.prompt('Enter a command: ', style = style)
            output = ''
            if command in ["close", "exit"]:
                self.__designer.print_info("Good bye!")
                break
            elif command == "hello":
                self.__designer.print_info("How can I help you?")
            elif command == "add":
                self.command_control_tip()
                person = fill_new_book_record()
                book.add_new_record(person)
            elif command == "add_phone":
                name = fill_user_name()
                phone = fill_phone_number()
                book.add_new_phone(name, phone)
            elif command == "change_phone":
                name = fill_user_name()
                phone_old = fill_phone_number()
                phone_new = fill_phone_number()
                book.change_phone(name, phone_old, phone_new)
            elif command == "delete_phone":
                name = fill_user_name()
                phone_to_delete = fill_phone_number()
                book.delete_phone(name, phone_to_delete)
            elif command == "update_address":
                name = fill_user_name()
                address = fill_address()
                book.update_address(name, address)
            elif command == "update_email":
                name = fill_user_name()
                email = fill_email()
                book.update_email(name, email)
            elif command == "add_birthday":
                name = fill_user_name()
                birthdate = fill_birthdate()
                book.add_birthday(name, birthdate)
            elif command == "show_upcoming_birthday":
                days = self.__designer.print_input("write days amount") # TODO edit "write days amount" to something better
                # days_as_int = convert and validate input_days
                # book.get_upcoming_birthdays(days_as_int) TODO !!!!!!!
            elif command == "all":
                records = list(book.get_all()) # TODO !!!!!!!
                # self.__designer.print_table(records)
            elif command == "show_by_name":
                name = fill_user_name()
                # book.get_by_name(name) TODO !!!!!!!
                # self.__designer.print_table(records)
                pass
            elif command == "show_by_part_name":
                part_name = self.__designer.print_input("write part of name")  # TODO edit "write days amount" to something better
                # book.get_by_part_name(part_name) TODO !!!!!!!
                self.__designer.print_table(records)
            # elif command == "add-note":
            #     print(add_note(args, notebook))

            # elif command == "find-note":
            #     print(find_note(args, notebook))

            # elif command == "delete-note":
            #     print(delete_note(args, notebook))

            # elif command == "add-birthday":
            #     print("Need to do.")
            # elif command == "show-birthday":
            #     print("Need to do.")
            # elif command == "birthdays":
            #     print("Need to do.")
            else:
                self.__designer.print_error("Invalid command.")

            self.__designer.print_info(output)

        book.save_data()



    def command_control_tip(self):
        self.__designer.print_info(f"Use '{EMPTY_FIELD_COMMAND}' for skip property and '{CANCEL_FILLING_COMMAND}' to cancel command")